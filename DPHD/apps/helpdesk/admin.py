from django.contrib import admin
from .models import Ticket, UserProfile, Departament
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)


# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Ticket)
admin.site.register(Departament)
