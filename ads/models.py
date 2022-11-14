# -*- coding: utf8 -*-
from django.db import models


class Ads(models.Model):
    name = models.CharField('Объявление', max_length=255)
    author = models.CharField('Имя продавца', max_length=100)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=0)
    description = models.TextField('Описание', max_length=2000, blank=True)
    address = models.CharField('Адрес', max_length=255)
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

        
