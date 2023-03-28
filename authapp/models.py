from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.db import connection

# Create your models here.

# class UserRole(models.Model):
#     uid = models.IntegerField(verbose_name='UID роли', primary_key=True, serialize=True, db_column='uid')
#     name = models.CharField(verbose_name='Краткое название роли', max_length=64, unique=True, db_column='name')
#     description = models.CharField(verbose_name='Описание роли WEB пользователя', max_length=256, blank=True
#                                    , db_column='descr')
#
#     def __str__(self):
#         return self.name

# def avatar_upload_to(instance, filename):
#     return os.path.join('uploads', instance.user.username + os.path.splitext(filename)[1])
#
# class WebUser(AbstractUser):
#     avatar = models.ImageField(upload_to=avatar_upload_to)
#
#     def get_usersadmlist(user):
#         if user.is_authenticated:
#             return WebUser.objects.all().order_by('id')
#         else:
#             return []
#
class WebUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', blank=True)
    __default_facility_id = 4
    current_facility_id = models.IntegerField('current_facility_id', default=4, blank=False, db_column='current_facility_id')
    own_facility_id = models.CharField('own_facility_id', max_length=50, db_column='own_facility_id', null=True)

    def get_usersadmlist(user):
        if user.is_authenticated:
            return WebUser.objects.all().order_by('id')
        else:
            return []

    def get__usersadm_by_id(request, id):
        # Если пользователь авторизирован
        if request.user.is_authenticated:
            res = WebUser.objects.filter(id=id)
        # Иначе возвращаем пустую корзину
        else:
            res = []
        return res

    def get_current_facility_id(self):
        return self.current_facility_id

    def set_current_facility_id(self, new_fc_id):
        self.current_facility_id = int(new_fc_id)
        self.save()

    def get_default_facility_id(self):
        return self.current_facility_id

    def get_facility_list(request):
        user = request.id
        cursor = connection.cursor()
        facil = "select facility_id from webface.user_fc_list('" + str(user) + "')"
        cursor.execute(facil)
        facility_list = [item[0] for item in cursor.fetchall()]
        return facility_list

    def __str__(self):
        return self.username
    # def __str__(self):
        # return "{self.user_id} ({self.short_name})"
