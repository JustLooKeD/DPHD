from django.db import models


class User(models.Model):
    name = models.CharField('Имя', max_length=50)
    telephone = models.CharField('Номер телефона', max_length=12)
    position = models.CharField('Отдел', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Ticket(models.Model):
    created_ticket = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=30)
    description = models.TextField('Описание')
    create_date = models.DateTimeField('Дата создания заявки')
    status = models.CharField('Статус заявки', max_length=15)
    #executant = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
