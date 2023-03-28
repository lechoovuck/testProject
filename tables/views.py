import csv
import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Max, Sum, Q, Count, QuerySet
from django.db import connection, transaction
from django.urls import reverse
from .forms import *
from .filters import ProcessLogFilter
from .models import *

from .breadcrumb import get_bread_crumb


def get_fc_time_zone(fc):
    fc_tz = ""
    for z in fc:
        fc_tz = z.def_time_zone
    if fc_tz == None:
        fc_tz = "UTC"
    if len(fc_tz) == 0:
        fc_tz = "UTC"
    return fc_tz

# @login_required
def facilityselectwebuser(request):
    if request.method == "POST":
        facility_id = request.POST.get('facility_name')
        request.user.set_current_facility_id(facility_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def loadDynamicDemo(request):
    fc = Facility.get_webuser_facility(request)
    data = VMonitorDirections.objects.filter(facility_id__in=fc).order_by('dir_name')
    return render(request, 'tables/index_directions.html', {'data': data})


def loadDynamicDemo2(request):
    fc = Facility.get_webuser_facility(request)
    data = VMonitorTransp.objects.filter(facility_id__in=fc).order_by('dat_begin')
    return render(request, 'tables/index_transport.html', {'data': data})


def loadDynamicDemo3(request):
    fc = Facility.get_webuser_facility(request)
    data = VMonitorHuForAnpack.objects.filter(facility_id__in=fc).order_by('dur_tz')
    return render(request, 'tables/index_hu_for_unpack.html', {'data': data})


def loadDynamicDemo4(request):
    fc = Facility.get_webuser_facility(request)
    data = VMonitorTaskWork.objects.filter(facility__in=fc).order_by('create_date')
    return render(request, 'tables/index_task_in_work.html', {'data': data, 'facility_tz': get_fc_time_zone(fc)})


def loadDynamicDemo5(request):
    fc = Facility.get_webuser_facility(request)
    data = VTrucks.objects.filter(facility_id__in=fc, loc_type='DOOR').order_by('-direction', '-status', 'add_date')
    datnow2 = datetime.datetime.now() + datetime.timedelta(hours=-12)
    datnow2 = datnow2.strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'tables/index_trucks.html', {'data': data, 'datnow': datnow2})


def loadDynamicDemo6(request):
    fc = Facility.get_webuser_facility(request)
    datat = VTrucks.objects.filter(facility_id__in=fc, loc_type='PARKING').order_by('-direction', '-status', 'add_date')
    return render(request, 'tables/index_trucksInLine.html', {'data': datat})


def loadDynamicDemo7(request):
    fc = Facility.get_webuser_facility(request)
    data = VMonitorTransp.objects.filter(facility_id__in=fc, priority__gte=0).order_by('dat_begin')
    return render(request, 'tables/index_trucks_transport_plan.html', {'data': data})


def facilityselectwebuser(request):
    if request.method == "POST":
        facility_id = request.POST.get('facility_name')
        request.user.set_current_facility_id(facility_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def userprofile(request):
    title = 'Профиль'
    if request.method == 'POST':
        form = ProfUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:userprofile'))
        else:
            return HttpResponseNotFound("<h2>'Форма заполнена некоректно!'</h2>")
    else:
        form = ProfUserForm(instance=request.user)
    formpass = PasswordChangeForm(request.user, request.POST)
    content = {'title': title, 'form': form, 'formpass': formpass}
    return render(request, 'tables/userprofile.html', content)



# @login_required
# @permission_required('mainapp.view_monitor', login_url='mainapp:main')
def index(request):
    title = 'Главная'
    navcurtab = '/'
    fc = Facility.get_webuser_facility(request)
    devlist2 = VDevList.objects.filter(dev_owner__in=fc).order_by('dev_id').exclude(dev_state=21)
    devlist21 = VDevList.objects.filter(dev_owner__in=fc).count()
    devlist3 = VMonitDevinWay.objects.filter(own_to__in=fc, dev_state=13).order_by('dev_id')
    devlist31 = VMonitDevinWay.objects.filter(own_to__in=fc, dev_state=13).count()
    # trucks = VTrucks.objects.filter(facility_id=fc).order_by('loc_id')
    # datnow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datnow2 = datetime.datetime.now() + datetime.timedelta(hours=-12)
    datnow2 = datnow2.strftime("%Y-%m-%d %H:%M:%S")
    data = VMonitorTransp.objects.filter(facility_id__in=fc, priority__gte=0).order_by('dat_begin')
    data2 = VMonitorTransp.objects.filter(facility_id__in=fc, priority__gte=0).count()
    data3 = VMonitorHuForUnpack.objects.filter(facility_id__in=fc).count()
    data4 = VMonitorTaskWork.objects.filter(facility__in=fc).count()
    data1 = VMonitorDirections.objects.filter(facility_id__in=fc).count()
    data5 = VTrucks.objects.filter(facility_id__in=fc, loc_type='PARKING').count()
    data6 = VTrucks.objects.filter(facility_id__in=fc, loc_type='DOOR').count()
    datatw = VTrucks.objects.filter(facility_id__in=fc, loc_type='DOOR').order_by('-direction', '-status', 'add_date')
    fc1 = fc.values_list('facility_id', flat=True)
    for i in fc1:
        fc1 = str(i)
    fc2 = fc.values_list('ext_id', flat=True)
    for i in fc2:
        fc2 = str(i)
    qualitylastweek = VgoogleKeyMonitor.objects.filter(column_1=fc2).values('column_1').annotate(
        Max('column_4')).order_by()
    value_max_items = set(
        row['column_4__max']
        for row in qualitylastweek
    )
    for i in value_max_items:
        value_max_items = str(i)
    if value_max_items == set():
        value_max_items = 0
    qualitylastweek = VgoogleKeyMonitor.objects.filter(column_4=value_max_items, column_1=fc2)
    qualitylastmonth = VgoogleKeyMonitor.objects.filter(column_1=fc2).values('column_1').annotate(
        Max('column_6')).order_by()
    value_max_items = set(
        row['column_6__max']
        for row in qualitylastmonth
    )

    if VgoogleFines and VgoogleFines._meta.db_table.split('.')[1][3:-1] in connection.introspection.table_names():
        fine = VgoogleFinesInfo.objects.all()
        fine2 = VgoogleFines.objects.filter(column_0=fc2).order_by('seq_id')
        fine3 = VgoogleFines.objects.filter(column_0=fc2).count()
        fine4 = VgoogleFines.objects.filter(column_0=fc2, column_5='Нарушение по системе ОКО').count()
        fine41 = VgoogleFines.objects.filter(column_0=fc2, column_5='Нарушение по системе ОКО').distinct(
            'column_6').count()
        fine4 = fine4 - fine41
        fine5 = VgoogleFines.objects.filter(column_0=fc2, column_5='Нарушение по системе ОКО (ЖУ)').count()
        fine51 = VgoogleFines.objects.filter(column_0=fc2, column_5='Нарушение по системе ОКО (ЖУ)').distinct(
            'column_6').count()
        fine5 = fine5 - fine51
        fine3 = fine3 - fine4 - fine5
        finenorm = VgoogleThresholdFines.objects.filter(column_1=fc2)
        finenorm2 = finenorm.values_list('column_2', flat=True)
        if not finenorm2.exists():
            finenorm2 = 0
            finenorm3 = 0
            finenorm4 = 0
        else:
            for i in finenorm2:
                finenorm2 = str(i)
            finenorm3 = int(finenorm2) / 2
            finenorm4 = int(finenorm2)
    else:
        fine = VgoogleFinesInfo.objects.all()
        fine2 = []
        fine3 = 0
        finenorm2 = 0
        finenorm3 = 0.0
        finenorm4 = 0

    if VgoogleKeyMonitor and VgoogleKeyMonitor._meta.db_table.split('.')[1][
                             3:-1] in connection.introspection.table_names():
        for i in value_max_items:
            value_max_items = str(i)
        qualitylastmonth = VgoogleKeyMonitor.objects.filter(column_6=value_max_items, column_1=fc2)
    else:
        qualitylastmonth = []
        qualitylastweek = []

    if request.method == "POST":
        seq_id = request.POST.get('load', None)
        form = {'loc_id': request.POST['loc_id'], 'user_name': request.POST['user_name']}
        if form['loc_id'] and form['user_name']:
            loc_id = form['loc_id']
            responsible1 = form['user_name']
            responsible2 = Responsible.objects.get(seq_id=responsible1)
            responsible = responsible2.user_id
            responsible_name = responsible2.user_name
            cursor = connection.cursor()
            cursor.execute(
                "select o_res2, o_res2_desc from webface.set_transport_door(" + fc1 + ", '" + request.user.username + "' :: varchar, " + str(
                    seq_id) + ", " + str(
                    loc_id) + ", '" + responsible + "' :: varchar, '" + responsible_name + "' :: varchar)")
            result = tuple(cursor.fetchone())
            o_res2, o_res2_desc = result
            ok = 0
            if o_res2 == ok:
                # return HttpResponseRedirect(reverse('mainapp:main',  {'facility_tz': get_fc_time_zone(fc)}))
                return HttpResponseRedirect(reverse('mainapp:main'))
            else:
                request.session['post_data'] = o_res2_desc
                errors = reverse('mainapp:errorsettransport', )
                return HttpResponseRedirect(errors)

    context = {
        'title': title,
        'facility_tz': get_fc_time_zone(fc),
        'devlist2': devlist2,
        'devlist21': devlist21,
        'devlist3': devlist3,
        'devlist31': devlist31,
        'data': data,
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'data4': data4,
        'data5': data5,
        'data6': data6,
        'fine': fine,
        'fine2': fine2,
        'fine3': fine3,
        'finenorm2': finenorm2,
        'finenorm3': finenorm3,
        'finenorm4': finenorm4,
        'datatw': datatw,
        'fc1': fc1,
        'datnow': datnow2,
        'qualitylastweek': qualitylastweek,
        'qualitylastmonth': qualitylastmonth,
        'navcurtab': navcurtab
    }
    return render(request, 'tables/index.html', context)


# @login_required
# @permission_required('mainapp.view_logproc', login_url='mainapp:main')
def log_proc(request):
    filter_is_used = request.get_full_path() != '/logproc/'
    context = dict()
    page = request.GET.get("page", 1)

    title = 'Логирование'
    order_by = request.GET.get('orderby', '-seq_id')
    logproc = LogProc.objects.all().order_by(order_by) if filter_is_used else QuerySet(
        LogProc.objects.all().first())

    filters = ProcessLogFilter(request.GET, queryset=logproc)
    context['filters'] = filters

    paginator = Paginator(filters.qs.order_by(order_by), per_page=30)

    if int(page) > paginator.num_pages:
        page = paginator.num_pages

    page_object = paginator.get_page(page)
    page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)

    context.update({
        'title': title,
        'page_object': page_object if filter_is_used else ['Заполните фильтр'],
        'breadcrumb': get_bread_crumb('tables:logproc'),
        'order_by': order_by
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
