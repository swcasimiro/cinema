from django.db import models
from django.core.validators import FileExtensionValidator

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
    title = models.CharField(
        max_length=100
    )
    image = models.ImageField(
        upload_to='image/'
    )
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(
            allowed_extensions=['mp4']
        )]
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Cерия'
        verbose_name_plural = 'Серии'

