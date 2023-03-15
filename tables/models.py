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
