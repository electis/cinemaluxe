from django.db import models
from PIL import Image as Img
from PIL import ExifTags
from io import BytesIO
from django.core.files import File
from sorl.thumbnail import ImageField


def next_order():
    try:
        return MenuItem.objects.order_by('order').last().order + 1
    except:
        return 1

def banner_order():
    try:
        return BannerItem.objects.order_by('order').last().order + 1
    except:
        return 1

def group_order():
    try:
        return GroupItem.objects.order_by('order').last().order + 1
    except:
        return 1

def product_order():
    try:
        return ProductItem.objects.order_by('order').last().order + 1
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
    order = models.IntegerField(default=banner_order, verbose_name="Порядок вывода")
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


class Group(models.Model):
    big = models.CharField(max_length=255, default='', verbose_name="Крупный")
    mini = models.CharField(max_length=255, default='', verbose_name="Мелкий")

    class Meta:
        verbose_name = "Заголовок групп"
        verbose_name_plural = "4 Заголовок групп"

    def __str__(self):
        return 'Заголовок групп'


class GroupItem(models.Model):
    img = models.ImageField(upload_to='', null=True, verbose_name="Картинка")
    name = models.CharField(max_length=255, default='', verbose_name="Название H4")
    text = models.CharField(max_length=255, default='', verbose_name="Текст")
    light = models.BooleanField(default=False, verbose_name="Картинка светлая")
    order = models.IntegerField(default=group_order, verbose_name="Порядок вывода")

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "5 Группы"
        ordering = ('order', 'name')

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    img = ImageField(upload_to='', null=True, verbose_name="Основная картинка")
    name = models.CharField(max_length=255, default='', verbose_name="Название")
    text = models.CharField(max_length=255, default='', verbose_name="Краткое описание")
    description = models.TextField(default='', verbose_name="Подробное описание")
    order = models.IntegerField(default=product_order, verbose_name="Порядок вывода")
    group = models.ForeignKey(GroupItem, on_delete=models.SET_NULL, null=True,
                              verbose_name="Основная группа товара", related_name="product")
    group_many = models.ManyToManyField(GroupItem, blank=True,
                                        verbose_name="Дополнительные группы товара", related_name="product_many")
    field_many = models.ManyToManyField('FieldItem', verbose_name="Параметры товара", blank=True)
    img_many = models.ManyToManyField('ImageItem', verbose_name="Изображения товара", blank=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "6 Товары"
        ordering = ('order', 'name')

    def __str__(self):
        return f'{self.name}'


class FieldItem(models.Model):
    desc = models.CharField(max_length=255, default='', verbose_name="Внутреннее описание")
    name = models.CharField(max_length=255, default='', verbose_name="Название")
    text = models.CharField(max_length=255, default='', verbose_name="Значение")
    icon = models.CharField(max_length=255, default='', verbose_name="Иконка")
    order = models.IntegerField(default=1, verbose_name="Порядок вывода")

    class Meta:
        verbose_name = "Параметр товара"
        verbose_name_plural = "7 Параметры товаров"
        ordering = ('order', 'name')

    def __str__(self):
        return self.desc


class ImageItem(models.Model):
    desc = models.CharField(max_length=255, default='', verbose_name="Внутреннее описание")
    name = models.CharField(max_length=255, default='', verbose_name="Название", blank=True)
    img = ImageField(upload_to='', null=True, verbose_name="Картинка")
    order = models.IntegerField(default=1, verbose_name="Порядок вывода")

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "8 Изображения товаров"
        ordering = ('order', 'name')

    def image_tag(self):
        from django.utils.safestring import mark_safe
        return mark_safe(f'<img src="/static/images/{self.img}" height="200px" />')
    image_tag.short_description = 'Image'

    def image50_tag(self):
        from django.utils.safestring import mark_safe
        return mark_safe(f'<img src="/static/images/{self.img}" height="50px" />')
    image_tag.short_description = 'Image50'

    def __str__(self):
        return self.desc


class Gallery(models.Model):
    big = models.CharField(max_length=255, default='', verbose_name="Заголовок")
    text = models.CharField(max_length=255, default='', verbose_name="Текст после")
    btn = models.CharField(max_length=255, default='', verbose_name="Кнопка название")
    btn_url = models.CharField(max_length=255, default='', verbose_name="Кнопка ссылка")

    class Meta:
        verbose_name = "Заголовок галереи"
        verbose_name_plural = "9 Заголовок галереи"

    def __str__(self):
        return 'Заголовок галереи'


class GalleryItem(models.Model):
    img = models.ImageField(upload_to='', null=True, verbose_name="Картинка")
    name = models.CharField(max_length=255, default='', verbose_name="Текст при наведении")
    order = models.IntegerField(default=1, verbose_name="Порядок вывода")

    class Meta:
        verbose_name = "Фото галереи"
        verbose_name_plural = "10 Фото галереи"
        ordering = ('order', 'name')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.img:
            pilImage = Img.open(BytesIO(self.img.read()))
            orientation = 0
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = dict(pilImage._getexif().items())
            if exif[orientation] == 3:
                pilImage = pilImage.rotate(180, expand=True)
            elif exif[orientation] == 6:
                pilImage = pilImage.rotate(270, expand=True)
            elif exif[orientation] == 8:
                pilImage = pilImage.rotate(90, expand=True)
            output = BytesIO()
            pilImage.save(output, format='JPEG', quality=75)
            output.seek(0)
            self.img = File(output, self.img.name)
        return super(GalleryItem, self).save(*args, **kwargs)
