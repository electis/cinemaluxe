from django.db import models


def next_order():
    try:
        return MenuItem.objects.order_by('order').last().order + 1
    except:
        return 1


class Site(models.Model):
    title = models.CharField(max_length=255, default='', verbose_name="Заголовок вкладки")
    keywords = models.CharField(max_length=255, default='', verbose_name="Ключевые слова")
    description = models.CharField(max_length=255, default='', verbose_name="Описание")
    logo = models.ImageField(upload_to='', null=True, verbose_name="Лого")

    class Meta:
        verbose_name = "Сайт"
        verbose_name_plural = "0 Сайт"

    def __str__(self):
        return f'{self.title}'


class MenuItem(models.Model):
    name = models.CharField(max_length=64, default='', verbose_name="Название")
    url = models.CharField(max_length=255, default='', verbose_name="Ссылка")
    order = models.IntegerField(default=next_order, verbose_name="Порядок вывода")

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "1 Пункты меню"
        ordering = ('order', 'name')

    def __str__(self):
        return f'{self.name}'


class BannerItem(models.Model):
    img = models.ImageField(upload_to='', null=True, verbose_name="Картинка")
    name = models.CharField(max_length=255, default='', verbose_name="Заголовок H1")
    mark = models.BooleanField(default=False, verbose_name="Заголовок выделен")
    text = models.CharField(max_length=255, default='', verbose_name="Текст H4")
    btn = models.CharField(max_length=255, default='', verbose_name="Кнопка название")
    btn_url = models.CharField(max_length=255, default='', verbose_name="Кнопка ссылка")
    btn_left = models.BooleanField(default=False, verbose_name="Кнопка иконка слева")
    order = models.IntegerField(default=1, verbose_name="Порядок вывода")
    top = models.BooleanField(default=False, verbose_name="Текст сверху")
    center = models.BooleanField(default=True, null=True, verbose_name="Текст по центру (None - слева)")

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "2 Баннеры"
        ordering = ('order', 'name')

    def __str__(self):
        return f'{self.name}'


class Description(models.Model):
    before = models.CharField(max_length=255, default='', verbose_name="Перед крупным")
    big = models.CharField(max_length=255, default='', verbose_name="Крупный")
    mini = models.CharField(max_length=255, default='', verbose_name="Мелкий")

    class Meta:
        verbose_name = "Описание"
        verbose_name_plural = "3 Описание"

    def __str__(self):
        return 'Описание'
