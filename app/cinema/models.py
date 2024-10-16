from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator # валидатор mp4
from django.db import models
from django.contrib.humanize.templatetags.humanize import intcomma
from tinymce.models import HTMLField


# Главная страница
class Index(models.Model):
    title = models.CharField(
        'Заголовок страницы',
        max_length=200,
        help_text='Название сериала'
    )
    banner_img = models.ImageField(
        'Баннер главной страницы',
        upload_to='users/%Y/%m/%d/',
        blank=True
    )

    info_img = models.ImageField(
        'Фотография для информации о сериале',
        upload_to='users/%Y/%m/%d/',
        blank=True
    )
    name = models.CharField(
        'Заголовок информации',
        max_length=90,
        help_text='Название фильма'
    )
    description = models.TextField(
        'Краткий пересказ фильма',
        max_length=300
    )

    def __str__(self):
        return 'Главная страница'

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


# Модель сезонов
class Category(models.Model):
    name = models.CharField(
        'Название сериала',
        max_length=90
    )
    description = models.TextField(
        'Описание сезона',
        max_length=200
    )
    slug = models.SlugField(
        help_text='Заполнится автоматически',
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL"
    )
    season = models.CharField(
        'Номер сезона',
        max_length=1
    )
    img_banner = models.ImageField(
        'Фотография для главной страницы',
        upload_to='users/%Y/%m/%d/',
        blank=True
    )

    def __str__(self):
        return f'{self.season} сезон'

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'


class Video(models.Model):
    cat = models.ForeignKey(
        Category,
        related_name='Категория',
        on_delete=models.PROTECT,
        help_text='Сезон'
    )
    poster = models.ImageField(
        'Постер видео',
        upload_to='posters/%Y/%m/%d/',
        blank=True
    )
    title = models.CharField(
        'Номер серии.',
        max_length=8,
        help_text='format - № серия'
    )
    file = models.FileField(
        'Производимый видеофайл',
        upload_to='video/',
        validators=[FileExtensionValidator(
            allowed_extensions=['mp4']
        )]
    )
    create_at = models.DateTimeField(
        'Когда создан',
        auto_now_add=True
    )
    slug = models.SlugField(
        help_text='Заполнится автоматически',
        max_length=255,
        db_index=True,
        verbose_name="URL"
    )
    view = models.IntegerField(
        'Просмотры',
        default=0
    )
    formatted_view = models.CharField(  # форматирование числа
        max_length=20,
        blank=True,
    )

    def format_number(self, *args, **kwargs):
        self.formatted_view = intcomma(self.view)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.cat} - {self.title}'

    def get_absolute_url(self):
        return reverse('video', kwargs={'video_slug': self.slug})



    class Meta:
        verbose_name = 'Cерия'
        verbose_name_plural = 'Серии'


class Comment(models.Model):
    video_c = models.ForeignKey(
        Video,
        related_name='Видео',
        on_delete=models.PROTECT
    )
    name = models.CharField(
        'Имя пользователя',
        max_length=30,
    )
    description = models.TextField(
        'Комментарий',
        max_length=600
    )

    create_at = models.DateTimeField(
        'Когда создан',
        auto_now_add=True
    )

    CHOICE_TYPE_REVIEW = (
        ('Нейтральная', 'Нейтральная'),
        ('Положительная', 'Положительная'),
        ('Отрицательная', 'Отрицательная')
    )

    type_r = models.CharField(
        'Статус рецензии',
        choices=CHOICE_TYPE_REVIEW,
        max_length=30,
        default='Нейтральная'
    )

    def __str__(self):
        return f"{self.video_c} - {self.name} [{self.create_at}]"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'