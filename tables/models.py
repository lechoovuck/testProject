from django.db import models


class LogProc(models.Model):
    seq_id = models.AutoField(
        verbose_name='ID Log',
        db_column='seq_id',
        primary_key=True,
        null=False,
    )
    eventtime = models.DateTimeField(
        verbose_name='Время события',
        auto_now_add=True,
        db_column='eventtime',
        null=True,
        blank=True
    )
    proc = models.TextField(
        verbose_name='Процедура',
        db_column='proc',
        null=False,
    )
    err_code = models.CharField(
        verbose_name='Код ошибки',
        db_column='err_code',
        max_length=50,
        null=True,
        blank=True
    )
    text = models.TextField(
        verbose_name='Текст ошибки',
        db_column='text',
        null=True,
        blank=True
    )
    obj_id = models.TextField(
        verbose_name='Идентификатор объекта',
        db_column='obj_id',
        null=True,
        blank=True
    )
    obj_type = models.TextField(
        verbose_name='Объект',
        db_column='obj_type',
        null=True,
        blank=True
    )
    message_type = models.TextField(
        verbose_name='Тип события',
        db_column='message_type',
        null=False
    )
    err_dtl = models.TextField(
        verbose_name='err_dtl',
        db_column='err_dtl',
        null=True,
        blank=True
    )
    err_hint = models.TextField(
        verbose_name='err_hint',
        db_column='err_hint',
        null=True,
        blank=True
    )

    class Meta:
        db_table = '"voiceman"."logproc"'

    def get_logproclist(user):
        if user.is_authenticated:
            return LogProc.objects.all().order_by('seq_id')
        else:
            return []

    def __str__(self):
        return str(self.proc)


class VDevList(models.Model):
    dev_id = models.AutoField(
        verbose_name='ID устройства',
        db_column='dev_id',
        null=False,
        primary_key=True,
    )
    dev_manufacture_id = models.CharField(
        verbose_name='Заводской номер',
        db_column='dev_manufacture_id',
        max_length=50,
        null=True,
    )
    dev_uid = models.CharField(
        verbose_name='Инвентарный номер',
        db_column='dev_uid',
        max_length=20,
        null=True,
    )
    dev_name = models.CharField(
        verbose_name='Имя устройства',
        db_column='dev_name',
        max_length=50,
        null=False,
    )
    dev_type_name = models.CharField(
        verbose_name='Тип устройства',
        db_column='dev_type_name',
        max_length=50,
        null=False,
    )
    dev_type = models.CharField(
        verbose_name='Тип устройства',
        db_column='dev_type',
        max_length=20,
        null=False,
    )
    dev_state = models.CharField(
        verbose_name='Статус устройства',
        db_column='dev_state',
        max_length=20,
        null=False,
    )
    dev_state_name = models.CharField(
        verbose_name='Статус устройства',
        db_column='dev_state_name',
        max_length=50,
        null=False,
    )
    dev_state_color = models.CharField(
        verbose_name='Статус устройства',
        db_column='dev_state_color',
        max_length=50,
        null=False,
    )
    add_who = models.CharField(
        verbose_name='Кто добавил',
        db_column='add_who',
        max_length=20,
        null=False,
    )
    owner_name = models.CharField(
        verbose_name='Склад',
        db_column='owner_name',
        max_length=50,
        null=False,
    )
    add_date = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_column='add_date',
        null=False
    )
    last_change_id = models.IntegerField(
        verbose_name='Последнее изменение',
        db_column='last_change_id',
        null=False,
    )
    last_change_date = models.DateTimeField(
        verbose_name='Дата последнего изменения',
        auto_now_add=True,
        db_column='last_change_date',
        null=False
    )
    last_use_date = models.DateTimeField(
        verbose_name='Кто последний использовал',
        auto_now_add=True,
        db_column='last_use_date',
        null=False
    )
    last_use_who = models.CharField(
        verbose_name='Кто использовал',
        db_column='last_use_who',
        max_length=20,
        null=False,
    )
    ref_dev_id = models.IntegerField(
        verbose_name='ref_dev_id',
        db_column='ref_dev_id',
        null=False,
    )
    last_event_date = models.DateTimeField(
        verbose_name='Дата события',
        auto_now_add=True,
        db_column='last_event_date',
        null=False
    )

    dev_owner = models.IntegerField(
        verbose_name='Склад устройства',
        db_column='dev_owner',
        null=False,
    )
    last_event_id = models.IntegerField(
        verbose_name='№ последнего события',
        db_column='last_event_id',
        null=False,
    )
    used = models.TextField(blank=True, null=True)
    ready = models.TextField(blank=True, null=True)
    not_working = models.TextField(blank=True, null=True)
    can_be_send = models.BooleanField(default=False)
    is_managed = models.BooleanField(default=False)
    use_start = models.DateTimeField(
        verbose_name='В эксплуатации с',
        auto_now_add=False,
        db_column='use_start',
        null=True
    )
    op_state_name = models.CharField(
        verbose_name='Эксплуатационное состояние',
        db_column='op_state_name',
        max_length=20,
        null=True,
    )
    dev_const = models.DecimalField(
        verbose_name='Стоимость устройства',
        max_digits=20,
        decimal_places=2,
        db_column='dev_const',
        null=True,
        blank=True,
    )
    write_off_reason_name = models.CharField(
        verbose_name='Причина списания',
        db_column='write_off_reason_name',
        max_length=20,
        null=True,
    )
    device_version = models.CharField(
        verbose_name='device_version',
        db_column='device_version',
        max_length=50,
        null=True,
    )
    bporcess_version = models.IntegerField(
        verbose_name='bporcess_version',
        db_column='bporcess_version',
        null=False,
    )

    class Meta:
        managed = False
        db_table = '"webface"."v_dev_list"'

    def get_devlistlist(user):
        if user.is_authenticated:
            return VDevList.objects.all().order_by('dev_id')
        else:
            return []

    def __str__(self):
        return str(self.dev_uid)


class FacilityProperties(models.Model):
    prop_id = models.AutoField(
        verbose_name='prop_id',
        db_column='prop_id',
        null=False,
        primary_key=True,
    )
    prop_name = models.CharField(
        verbose_name='prop_name',
        max_length=50,
        db_column='prop_name',
        null=False,
    )
    prop_type = models.CharField(
        verbose_name='prop_type',
        max_length=1,
        db_column='prop_type',
        null=False,
    )
    def_str = models.CharField(
        verbose_name='Значение параметра',
        max_length=255,
        db_column='def_str',
        null=False,
    )
    prop_desc = models.CharField(
        verbose_name='prop_desc',
        db_column='prop_desc',
        max_length=255,
        blank=True,
        null=True
    )
    def_bool = models.BooleanField(default=False)
    def_date = models.DateTimeField(blank=True, null=True)
    def_num = models.DecimalField(max_digits=6, decimal_places=3, blank=True, verbose_name='Значение параметра',
                                  null=True)

    class Meta:
        db_table = '"bpdata"."facility_properties"'

    def __str__(self):
        return self.prop_desc


class FacilityProps(models.Model):
    seq_id = models.AutoField(
        verbose_name='seq_id',
        db_column='seq_id',
        null=False,
        primary_key=True,
    )
    prop_id = models.ForeignKey(
        'FacilityProperties',
        on_delete=models.CASCADE,
        verbose_name='prop_id',
        db_column='prop_id',
        null=False,
    )
    facility_id = models.IntegerField(
        verbose_name='facility_id',
        db_column='facility_id',
        null=False,
        default=0,
    )
    val_num = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    val_str = models.CharField(
        verbose_name='val_str',
        db_column='val_str',
        max_length=255,
        blank=True,
        null=True
    )
    val_bool = models.BooleanField(default=False)
    val_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = '"bpdata"."facility_props"'

    def __str__(self):
        return self.prop_id


class VFacilityProps(models.Model):
    seq_id = models.AutoField(
        verbose_name='seq_id',
        db_column='seq_id',
        null=False,
        primary_key=True,
    )
    prop_type = models.CharField(
        verbose_name='prop_type',
        max_length=1,
        db_column='prop_type',
        null=False,
    )
    facility_name = models.CharField(
        verbose_name='facility_name',
        max_length=50,
        db_column='facility_name',
        null=False,
    )
    prop_desc = models.CharField(
        verbose_name='prop_desc',
        db_column='prop_desc',
        max_length=255,
        blank=True,
        null=True
    )
    prop_id = models.IntegerField(
        verbose_name='prop_id',
        db_column='prop_id',
        null=False,
        default=0,
    )
    facility_id = models.IntegerField(
        verbose_name='facility_id',
        db_column='facility_id',
        null=False,
        default=0,
    )
    val_num = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    val_str = models.CharField(
        verbose_name='val_str',
        db_column='val_str',
        max_length=255,
        blank=True,
        null=True
    )
    val_bool = models.BooleanField(default=False)
    val_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"webface"."v_facility_props"'

    def __str__(self):
        return self.prop_desc


class VMonitDevinWay(models.Model):
    seq_id = models.AutoField(
        verbose_name='ID устройства',
        db_column='seq_id',
        null=False,
        primary_key=True,
    )
    dev_manufacture_id = models.CharField(
        verbose_name='Заводской номер',
        db_column='dev_manufacture_id',
        max_length=50,
        null=True,
    )
    dev_uid = models.CharField(
        verbose_name='Инвентарный номер',
        db_column='dev_uid',
        max_length=20,
        null=True,
    )
    dev_name = models.CharField(
        verbose_name='Имя устройства',
        db_column='dev_name',
        max_length=50,
        null=False,
    )
    dev_type_name = models.CharField(
        verbose_name='Тип устройства',
        db_column='dev_type_name',
        max_length=50,
        null=False,
    )
    dev_state_name = models.CharField(
        verbose_name='Статус устройства',
        db_column='dev_state_name',
        max_length=50,
        null=False,
    )
    dev_state_color = models.CharField(
        verbose_name='Статус устройства',
        db_column='dev_state_color',
        max_length=50,
        null=False,
    )
    add_who = models.CharField(
        verbose_name='Кто добавил',
        db_column='add_who',
        max_length=20,
        null=False,
    )
    add_date = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_column='add_date',
        null=False
    )
    own_change_id = models.IntegerField(
        verbose_name='own_change_id',
        db_column='own_change_id',
        null=False,
    )
    dev_id = models.IntegerField(
        verbose_name='dev_id',
        db_column='dev_id',
        null=False,
    )
    own_from = models.IntegerField(
        verbose_name='own_from',
        db_column='own_from',
        null=False,
    )
    own_to = models.IntegerField(
        verbose_name='own_to',
        db_column='own_to',
        null=False,
    )
    dev_state = models.IntegerField(
        verbose_name='dev_state',
        db_column='dev_state',
        null=False,
    )
    task_state = models.CharField(
        verbose_name='task_state',
        db_column='task_state',
        max_length=20,
        null=True,
    )
    task_state_color = models.CharField(
        verbose_name='task_state_color',
        db_column='task_state_color',
        max_length=20,
        null=True,
    )
    own_from_name = models.CharField(
        verbose_name='own_from_name',
        db_column='own_from_name',
        max_length=50,
        null=True,
    )
    own_to_name = models.CharField(
        verbose_name='own_to_name',
        db_column='own_to_name',
        max_length=50,
        null=True,
    )
    send_doc_id = models.CharField(
        verbose_name='№ Документа',
        db_column='send_doc_id',
        max_length=50,
        null=False
    )

    class Meta:
        managed = False
        db_table = '"webface"."v_monitor_dev_in_way"'

    def get_devlist_list(user):
        if user.is_authenticated:
            return VMonitDevinWay.objects.all().order_by('dev_id')
        else:
            return []

    def __str__(self):
        return str(self.dev_name)


class VMonitorTransp(models.Model):
    seq_id = models.IntegerField(primary_key=True, blank=True, null=False)
    transp_direction = models.TextField(blank=True, null=True)
    facility_id = models.IntegerField(blank=True, null=True)
    tknum = models.CharField(max_length=20, blank=True, null=True)
    tsnum = models.CharField(max_length=20, blank=True, null=True)
    route = models.CharField(max_length=100, blank=True, null=True)
    dat_end = models.DateTimeField(
        verbose_name='Дата Завершения плановая',
        db_column='dat_end',
        null=True,
        blank=True,
    )
    tim_begin_old = models.DateTimeField(
        verbose_name='Дата начала плановая',
        db_column='tim_begin_old',
        null=True,
        blank=True,
    )
    dat_begin = models.CharField(max_length=50, blank=True, null=True)
    # tim_begin = models.CharField(max_length=50, blank=True, null=True)
    # dat_end = models.CharField(max_length=50, blank=True, null=True)
    # tim_end = models.CharField(max_length=50, blank=True, null=True)
    car_num = models.CharField(max_length=100, blank=True, null=True)
    fio_driver1 = models.CharField(max_length=100, blank=True, null=True)
    phone_driver1 = models.CharField(max_length=50, blank=True, null=True)
    fio_driver2 = models.CharField(max_length=100, blank=True, null=True)
    phone_driver2 = models.CharField(max_length=50, blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    volum = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    pr_usr = models.CharField(max_length=255, blank=True, null=True)
    dat_begin_f = models.CharField(max_length=50, blank=True, null=True)
    # tim_begin_f = models.CharField(max_length=50, blank=True, null=True)
    dat_end_f = models.CharField(max_length=50, blank=True, null=True)
    # tim_end_f = models.CharField(max_length=50, blank=True, null=True)
    pandus = models.CharField(max_length=10, blank=True, null=True)
    holded = models.CharField(max_length=10, blank=True, null=True)
    load_wgt = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    load_vol = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    can_set_pandus = models.BooleanField(default=False)
    priority = models.IntegerField(blank=True, verbose_name='Приоритет', null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'v_monitor_transp'


class VMonitorHuForAnpack(models.Model):
    seq_id = models.IntegerField(primary_key=True, blank=True, null=False)
    o_hu_bc = models.CharField(max_length=50, blank=True, null=True)
    lichn = models.CharField(max_length=50, blank=True, null=True)
    o_hu_type_short = models.CharField(max_length=50, blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    hu_color = models.TextField(blank=True, null=True)
    facility_id = models.IntegerField(blank=True, null=True)
    dur_tz = models.DateTimeField(
        verbose_name='Дата',
        db_column='dur_tz',
        null=True,
        blank=True,
    )

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = '"webface"."v_monitor_hu_for_unpack"'


class VMonitorHuForUnpack(models.Model):
    seq_id = models.IntegerField(primary_key=True, blank=True, null=False)
    o_hu_bc = models.CharField(max_length=50, blank=True, null=True)
    lichn = models.CharField(max_length=50, blank=True, null=True)
    o_hu_type_short = models.CharField(max_length=50, blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    hu_color = models.TextField(blank=True, null=True)
    facility_id = models.IntegerField(blank=True, null=True)
    dur_tz = models.DateTimeField(
        verbose_name='Дата',
        db_column='dur_tz',
        null=True,
        blank=True,
    )

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = '"webface"."v_monitor_hu_for_unpack"'


class VMonitorTaskWork(models.Model):
    facility = models.IntegerField(blank=True, primary_key=True, null=False)
    task_id = models.IntegerField(blank=True, null=True)
    task_type = models.IntegerField(blank=True, null=True)
    task_type_name = models.CharField(max_length=20, blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    status_name = models.CharField(max_length=50, blank=True, null=True)
    status_color = models.CharField(max_length=50, blank=True, null=True)
    loc = models.CharField(max_length=255, blank=True, null=True)
    human_uid = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    dur_not_moved = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'v_monitor_task_in_work'


class VMonitorDirections(models.Model):
    facility_id = models.IntegerField(primary_key=True, verbose_name='id', db_column='facility_id', null=False)
    uid = models.IntegerField(verbose_name='uid', db_column='uid', null=True)
    dir_id = models.CharField(max_length=20, blank=True, null=True)
    dir_name = models.CharField(max_length=50, blank=True, null=True)
    dir_code = models.CharField(max_length=50, blank=True, null=True)
    dir_color = models.TextField(blank=True, null=True)
    v_on_soh = models.IntegerField(verbose_name='v_on_soh', db_column='v_on_soh', null=True)
    w_on_soh = models.IntegerField(verbose_name='w_on_soh', db_column='w_on_soh', null=True)
    v_appt_qty = models.IntegerField(verbose_name='v_appt_qty', db_column='v_appt_qty', null=True)
    w_appt_qty = models.IntegerField(verbose_name='w_appt_qty', db_column='w_appt_qty', null=True)
    v_in_transit = models.IntegerField(verbose_name='v_in_transit', db_column='v_in_transit', null=True)
    w_in_transit = models.IntegerField(verbose_name='w_in_transit', db_column='w_in_transit', null=True)
    v_total = models.IntegerField(verbose_name='v_total', db_column='v_total', null=True)
    w_total = models.IntegerField(verbose_name='w_total', db_column='w_total', null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = '"webface"."v_monitor_directions"'


class VTrucks(models.Model):
    seq_id = models.AutoField(
        verbose_name='ID',
        db_column='seq_id',
        primary_key=True,
        null=False,
    )
    direction = models.CharField(verbose_name='Направление', max_length=20)
    loc_type = models.CharField(verbose_name='loc_type', max_length=20)
    facility_id = models.IntegerField(
        verbose_name='facility',
        db_column='facility_id',
        null=False,
        default=0,
    )
    tknum = models.CharField(verbose_name='tknum', max_length=20)
    tsnum = models.CharField(verbose_name='tsnum', max_length=20)
    route = models.CharField(verbose_name='route', max_length=50)
    dir_id = models.CharField(verbose_name='dir_id', max_length=20)
    loc_id = models.CharField(verbose_name='loc_id', max_length=20)
    status = models.IntegerField(
        verbose_name='status',
        db_column='status',
        null=False,
        default=0,
    )
    status_name = models.CharField(verbose_name='status_name', max_length=50)
    status_color = models.CharField(verbose_name='status_color', max_length=50)
    can_ship_load = models.BooleanField(default=False)
    dir_name = models.CharField(verbose_name='dir_name', max_length=50)
    car_num = models.CharField(verbose_name='car_num', max_length=60)
    add_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    add_who = models.CharField(verbose_name='add_who', max_length=20)
    task_bc = models.CharField(verbose_name='task_bc', max_length=50)
    start_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    complete_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    responsible_who = models.CharField(max_length=20, blank=True, null=True)
    responsible_name = models.CharField(max_length=120, blank=True, null=True)

    map_loc_truck_seq_id = models.IntegerField(
        verbose_name='map_loc_truck_seq_id',
        db_column='map_loc_truck_seq_id',
        null=False,
        default=0,
    )
    map_loc_truck_ext_id = models.CharField(max_length=50, blank=True, null=True)
    ttransp_data_seq_id = models.IntegerField(
        verbose_name='ttransp_data_seq_id',
        db_column='ttransp_data_seq_id',
        null=False,
        default=0,
    )
    dat_begin_plan = models.DateTimeField(
        verbose_name='Дата план начало',
        auto_now_add=False,
        db_column='dat_begin_plan',
        null=True,
        blank=True
    )
    dat_end_plan = models.DateTimeField(
        verbose_name='Дата план завершение',
        auto_now_add=False,
        db_column='dat_end_plan',
        null=True,
        blank=True,
    )
    fio_driver1 = models.CharField(max_length=100, blank=True, null=True)
    fio_driver2 = models.CharField(max_length=100, blank=True, null=True)
    phone_driver1 = models.CharField(max_length=100, blank=True, null=True)
    phone_driver2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_trucks'


class VgoogleKeyMonitor(models.Model):
    seq_id = models.IntegerField(
        verbose_name='seq_id',
        db_column='seq_id',
        primary_key=True,
        null=False,
    )
    column_0 = models.TextField(blank=True, null=True)
    column_1 = models.TextField(blank=True, null=True)
    column_2 = models.IntegerField(
        verbose_name='column_2',
        db_column='column_2',
        null=False,
    )
    column_3 = models.TextField(blank=True, null=True)
    # column_4 = models.TextField(blank=True, null=True)
    column_4 = models.IntegerField(
        verbose_name='column_4',
        db_column='column_4',
        null=False,
    )
    column_5 = models.TextField(blank=True, null=True)
    column_6 = models.TextField(blank=True, null=True)
    column_7 = models.TextField(blank=True, null=True)
    column_8 = models.TextField(blank=True, null=True)
    column_9 = models.TextField(blank=True, null=True)
    column_10 = models.TextField(blank=True, null=True)
    column_11 = models.TextField(blank=True, null=True)
    column_12 = models.TextField(blank=True, null=True)
    column_13 = models.TextField(blank=True, null=True)
    column_14 = models.TextField(blank=True, null=True)
    column_15 = models.TextField(blank=True, null=True)
    column_16 = models.TextField(blank=True, null=True)
    column_17 = models.TextField(blank=True, null=True)
    column_18 = models.TextField(blank=True, null=True)
    column_19 = models.TextField(blank=True, null=True)
    column_20 = models.TextField(blank=True, null=True)
    column_21 = models.TextField(blank=True, null=True)
    column_22 = models.TextField(blank=True, null=True)
    column_23 = models.TextField(blank=True, null=True)
    column_24 = models.TextField(blank=True, null=True)
    column_25 = models.TextField(blank=True, null=True)
    column_26 = models.TextField(blank=True, null=True)
    column_27 = models.TextField(blank=True, null=True)
    column_28 = models.TextField(blank=True, null=True)
    column_29 = models.TextField(blank=True, null=True)
    column_30 = models.TextField(blank=True, null=True)
    column_31 = models.TextField(blank=True, null=True)
    column_32 = models.TextField(blank=True, null=True)
    column_33 = models.TextField(blank=True, null=True)
    column_34 = models.TextField(blank=True, null=True)
    column_35 = models.TextField(blank=True, null=True)
    column_36 = models.TextField(blank=True, null=True)
    column_37 = models.TextField(blank=True, null=True)
    column_38 = models.TextField(blank=True, null=True)
    column_39 = models.TextField(blank=True, null=True)
    column_40 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"webface"."v_google_key_monitor"'


class VgoogleFines(models.Model):
    seq_id = models.IntegerField(
        verbose_name='seq_id',
        db_column='seq_id',
        primary_key=True,
        null=False,
    )
    column_0 = models.TextField(blank=True, null=True)
    column_1 = models.TextField(blank=True, null=True)
    column_2 = models.TextField(blank=True, null=True)
    column_3 = models.TextField(blank=True, null=True)
    column_4 = models.TextField(blank=True, null=True)
    column_5 = models.TextField(blank=True, null=True)
    column_6 = models.TextField(blank=True, null=True)
    column_7 = models.TextField(blank=True, null=True)
    column_8 = models.TextField(blank=True, null=True)
    column_9 = models.TextField(blank=True, null=True)
    column_10 = models.TextField(blank=True, null=True)
    column_12 = models.DateField(blank=True, null=True)
    column_11 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"webface"."v_google_fines"'


class VgoogleFinesInfo(models.Model):
    seq_id = models.IntegerField(
        verbose_name='seq_id',
        db_column='seq_id',
        primary_key=True,
        null=False,
    )
    column_0 = models.TextField(blank=True, null=True)
    column_1 = models.TextField(blank=True, null=True)
    column_2 = models.TextField(blank=True, null=True)
    column_3 = models.TextField(blank=True, null=True)
    column_4 = models.TextField(blank=True, null=True)
    column_5 = models.TextField(blank=True, null=True)
    column_6 = models.TextField(blank=True, null=True)
    column_7 = models.TextField(blank=True, null=True)
    column_8 = models.TextField(blank=True, null=True)
    column_9 = models.TextField(blank=True, null=True)
    column_10 = models.TextField(blank=True, null=True)
    column_11 = models.TextField(blank=True, null=True)
    column_12 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"webface"."v_google_fines_info"'


class VgoogleThresholdFines(models.Model):
    seq_id = models.IntegerField(
        verbose_name='seq_id',
        db_column='seq_id',
        primary_key=True,
        null=False,
    )
    column_0 = models.TextField(blank=True, null=True)
    column_1 = models.TextField(blank=True, null=True)
    column_2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"webface"."v_google_threshold_fines"'


class Responsible(models.Model):
    seq_id = models.IntegerField(
        verbose_name='seq_id',
        db_column='seq_id',
        primary_key=True,
        null=False,
    )
    facility_id = models.IntegerField(
        verbose_name='Склад',
        db_column='facility_id',
        default=0,
        null=False,
    )
    user_id = models.CharField(
        null=False,
        max_length=20,
        verbose_name='Код',
    )
    user_name = models.CharField(
        null=False,
        max_length=100,
        verbose_name='Ответственный',
    )

    class Meta:
        managed = False
        db_table = '"webface"."v_fc_responsible"'

    def __str__(self):
        return str(self.user_name)

class Yard(models.Model):
    id = models.AutoField(
        verbose_name='ID двора',
        db_column='id',
        null=False,
        primary_key=True,
    )
    yard_name = models.CharField(
        verbose_name='Название двора',
        max_length=20,
        db_column='yard_name',
        null=False,
    )
    status = models.IntegerField(
        verbose_name='Cтатус',
        db_column='status',
        null=False,
        default=0,
    )

    class Meta:
        db_table = '"bpdata"."yard"'

    def get_yardlist(user):
        if user.is_authenticated:
            return Yard.objects.all().order_by('id')
        else:
            return []

    def get_yard_by_id(request, id):
        # Если пользователь авторизирован
        if request.user.is_authenticated:
            res = Yard.objects.filter(id=id)
        # Иначе возвращаем пустую корзину
        else:
            res = []
        return res

    def __str__(self):
        return self.yard_name


class Facility(models.Model):
    facility_id = models.AutoField(
        verbose_name='ID склада',
        db_column='facility_id',
        null=False,
        blank=True,
        primary_key=True,
    )
    facility_name = models.CharField(
        verbose_name='Название склада',
        max_length=20,
        db_column='facility_name',
        null=True,
        blank=True,
    )
    status = models.IntegerField(
        verbose_name='Статус',
        db_column='status',
        blank=True,
        null=True,
        default=0,
    )
    ext_id = models.CharField(
        verbose_name='Внешний ID склада',
        max_length=20,
        db_column='ext_id',
        blank=True,
        null=True,
    )
    ext_id2 = models.CharField(
        verbose_name='Внешний ID склада 2',
        max_length=50,
        db_column='ext_id2',
        blank=True,
        null=True,
    )
    yard_id = models.ForeignKey(
        'Yard',
        on_delete=models.CASCADE,
        verbose_name='Двор',
        db_column='yard_id',
        blank=True,
        null=True,
    )
    city_code = models.CharField(
        verbose_name='Код города',
        db_column='city_code',
        max_length=20,
        blank=True,
        null=True
    )

    owner = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Владелец',
        db_column='owner',
    )

    def_time_zone = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Часовой пояс',
        db_column='def_time_zone',
    )

    sqr_usable = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Площадь полезная',
        db_column='sqr_usable',
    )

    sqr_tech = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='площадь проездов/техническая зона',
        db_column='sqr_tech',
    )

    doors_qty = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='Кол-во ворот',
        db_column='doors_qty',
    )

    pandus_dtl = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='Наличие пандуса, длина (под какое количество ТС)',
        db_column='pandus_dtl',
    )

    wh_class = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Класс склада, Теплый/холодный',
        db_column='wh_class',
    )

    video_exists = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Наличие видеонаблюдения',
        db_column='video_exists',
    )

    floor_dtl = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name='Качество и покрытие пола',
        db_column='floor_dtl',
    )

    cells_qty = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Кол-во паллетомест на стеллажах выдачи (при наличии)',
        db_column='cells_qty',
    )

    height_ceiling = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Высота потолков',
        db_column='height_ceiling',
    )

    wifi_exists = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Наличие WIFI на складе',
        db_column='wifi_exists',
    )

    sqr_office = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Площадь офисных помещений',
        db_column='sqr_office',
    )

    office_dist = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Удаленность офиса от склада',
        db_column='office_dist',
    )

    warm_curtain = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Наличие тепловых завес',
        db_column='warm_curtain',
    )

    access_system = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Пропускная система на территорию, учет автотранспорта',
        db_column='access_system',
    )

    park_client = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Парковок	ТС клиентов',
        db_column='park_client',
    )

    park_adm = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Парковок ТС сотрудников',
        db_column='park_adm',
    )

    park_track = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Парковок Большегрузный транспорт',
        db_column='park_track',
    )

    park_own_transp = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Парковок Машины ГЛ (собственный транспорт)',
        db_column='park_own_transp',
    )

    equip_dizel = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Кол-во погрузчиков дизель',
        db_column='equip_dizel',
    )

    equip_el = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Электрические погрузчики',
        db_column='equip_el',
    )

    equip_rohl_el = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Электротележки',
        db_column='equip_rohl_el',
    )

    equip_rohl = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Кол-во рохлей',
        db_column='equip_rohl',
    )

    wgt_floor = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Весы Напольные',
        db_column='wgt_floor',
    )

    wgt_rohl = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Весовые рохли',
        db_column='wgt_rohl',
    )

    light_pandus = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Освещение	Пандус/ТС',
        db_column='light_pandus',
    )

    light_wh = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Освещение Склад',
        db_column='light_wh',
    )

    class Meta:
        db_table = '"bpdata"."facility"'

    def get_facilitylist(user):
        if user.is_authenticated:
            return Facility.objects.all().order_by('facility_id')
        else:
            return []

    def get_facility_by_id(request, facility_id):
        # Если пользователь авторизирован
        if request.user.is_authenticated:
            res = Facility.objects.filter(facility_id=facility_id)
        # Иначе возвращаем пустую корзину
        else:
            res = []
        return res

    def get_webuser_facility_list(request):
        if request.user.is_authenticated:
            res = Facility.objects.filter(facility_id__in=request.user.get_facility_list())
        else:
            res = []
        return res

    def get_webuser_facility(request):
        if request.user.is_authenticated:
            res = Facility.objects.filter(facility_id=request.user.get_current_facility_id())
        else:
            res = []
        return res

    def __unicode__(self):
        return self.facility_name

    def __str__(self):
        return self.facility_name
