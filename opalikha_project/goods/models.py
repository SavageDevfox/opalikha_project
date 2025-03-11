from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлена')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL; разрешены символы '
                   'латиницы, цифры, дефис и подчёркивание.')
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='category_pictures',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Good(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    price = models.DecimalField(
        verbose_name='Цена', max_digits=10, decimal_places=2, blank=True
    )
    description = models.TextField(
        default='Нет описания', verbose_name='Описание товара'
    )
    image = models.ImageField(
        'Изображение', upload_to='goods_pictures', blank=True, null=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создан'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Обновлен'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'
        default_related_name = 'goods'

    def __str__(self):
        return self.title
