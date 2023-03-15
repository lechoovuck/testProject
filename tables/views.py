from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required, permission_required
import os, json, datetime
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse


from tables.models import LogProc


def getparamwithdefault(request, key, default):
    if key in request.GET:
        page = request.GET[key]
        if page == "":
            page = default
    else:
        page = default
    return page


def index(request):
    return render(request, 'tables/index.html', {'title': 'tables'})


# @login_required
# @permission_required('mainapp.view_logproc', login_url='mainapp:main')
def logproc(request):
    page = getparamwithdefault(request, "page", 1);
    sort = getparamwithdefault(request, "sort", "-seq_id")
    search = getparamwithdefault(request, "search", "")
    datefrom = getparamwithdefault(request, "datefrom",
                                   (timezone.now() - timezone.timedelta(1)).strftime("%Y-%m-%d %H:%M"))
    dateto = getparamwithdefault(request, "dateto", (timezone.now() + timezone.timedelta(1)).strftime("%Y-%m-%d %H:%M"))

    title = 'Логирование',
    navcurtab = '/logproc/',
    logproc = LogProc.objects.filter(Q(eventtime__range=(datetime.datetime.strptime(datefrom, "%Y-%m-%d %H:%M"),
                                                         datetime.datetime.strptime(dateto, "%Y-%m-%d %H:%M"))) &
                                     (Q(seq_id__icontains=search) |
                                      Q(proc__icontains=search) |
                                      Q(err_code__icontains=search) |
                                      Q(text__icontains=search) |
                                      Q(obj_id__icontains=search) |
                                      Q(obj_type__icontains=search) |
                                      Q(message_type__icontains=search) |
                                      Q(err_dtl__icontains=search) |
                                      Q(err_hint__icontains=search))).order_by(sort)
    paginator = Paginator(logproc, per_page=30)

    if int(page) > paginator.num_pages:
        page = paginator.num_pages

    page_object = paginator.get_page(page)
    page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)
    page_object.sort = sort
    page_object.search = search
    page_object.datefrom = datefrom
    page_object.dateto = dateto

    context = {
        'title': title,
        'navcurtab': navcurtab,
        'page_object': page_object,
    }
    return render(request, 'tables/logproc.html', context)
