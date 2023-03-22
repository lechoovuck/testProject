import csv

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .breadcrumb import get_bread_crumb
from tables.filters import ProcessLogFilter
from tables.models import LogProc


def get_param_with_default(request, key, default):
    if key in request.GET:
        return default if request.GET[key] == '' else request.GET[key]
    else:
        return default


def index(request):
    return render(request, 'tables/index.html', {'title': 'tables'})


# @login_required
# @permission_required('mainapp.view_logproc', login_url='mainapp:main')
def log_proc(request):
    context = dict()
    sort = get_param_with_default(request, "sort", "-seq_id")
    page = get_param_with_default(request, "page", 1)
    date_from = get_param_with_default(request, "datefrom",
                                      (timezone.now() - timezone.timedelta(1)).strftime("%Y-%m-%d %H:%M"))
    date_to = get_param_with_default(request, "dateto",
                                    (timezone.now() + timezone.timedelta(1)).strftime("%Y-%m-%d %H:%M"))

    title = 'Логирование',
    navcurtab = '/logproc/',
    logproc = LogProc.objects.all()

    filters = ProcessLogFilter(request.GET, queryset=logproc)
    context.update({
        'filters': filters
    })

    paginator = Paginator(filters.qs, per_page=30)

    if int(page) > paginator.num_pages:
        page = paginator.num_pages

    page_object = paginator.get_page(page)
    page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)
    page_object.sort = sort
    page_object.date_from = date_from
    page_object.date_to = date_to

    context.update({
        'title': title,
        'navcurtab': navcurtab,
        'page_object': page_object,
        'breadcrumb': get_bread_crumb('mainapp:logproc')
    })

    if request.method == 'POST' and request.POST.get("export_csv") == 'export_csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=data.csv'
        writer = csv.writer(response)
        writer.writerow(
            ['id', 'datetime', 'procedure', 'error_code', 'error_text', 'object_id', 'object_type', 'message_type',
             'err_dtl', 'err_hint'])

        for event in filters.qs:
            writer.writerow(
                [event.seq_id, event.eventtime, event.proc, event.err_code, event.text, event.obj_id, event.obj_type,
                 event.message_type, event.err_dtl, event.err_hint])
        return response

    return render(request, 'tables/logproc.html', context)
