from django.db import models
from django.contrib.auth.models import User


class Departament(models.Model):
    departament = models.CharField('Отдел', max_length=30)

    def __unicode__(self):
        return self.departament

    def __str__(self):
        return f"{self.departament}"

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    departament = models.ForeignKey(Departament, null=False, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Ticket(models.Model):
    created_ticket = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=30)
    description = models.TextField('Описание')
    create_date = models.DateTimeField('Дата создания заявки')
    status = models.CharField('Статус заявки', max_length=15)

    # executant = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
