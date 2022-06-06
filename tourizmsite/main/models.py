from django.db import models
from django.urls import reverse


class TourPlace(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    tourtype = models.TextField(blank=True, verbose_name='Тип туризма')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категории')
    def get_absolute_url(self):
        return reverse('view_tourplace',kwargs={"category_id":self.pk})
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['-created_at']
class Category(models.Model):
    title =models.CharField(max_length=150,db_index=True,verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class TourizmType(models.Model):
    title = models.CharField(max_length=150,verbose_name='Наименование')
    content = models.TextField(blank=True,verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата публикации')
    updated_at =models.DateTimeField(auto_now=True,verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='фото',blank=True)
    is_published = models.BooleanField(default=True,verbose_name='Опубликовано?')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Тип туризма'
        verbose_name_plural ='Типы туризма'
        ordering =['-created_at']





