from django.db import models


def next_order():
    try:
        return MenuItem.objects.order_by('order').last().order + 1
    except:
        return 1


class Menu(models.Model):
    logo = models.FileField(upload_to='', verbose_name="Лого")
    items = models.ManyToManyField('MenuItem', verbose_name="Пункты меню", blank=True)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return 'Меню'


class MenuItem(models.Model):
    name = models.CharField(max_length=64, default='', verbose_name="Название")
    url = models.CharField(max_length=255, default='', verbose_name="Ссылка")
    order = models.IntegerField(default=next_order, verbose_name="Порядок вывода")

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
        ordering = ('order',)

    def __str__(self):
        return f'{self.name}'
