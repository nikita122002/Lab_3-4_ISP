# Generated by Django 4.0.4 on 2022-06-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tourizmtype_delete_mymodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tourizmtype',
            options={'ordering': ['-created_at'], 'verbose_name': 'Тип туризма', 'verbose_name_plural': 'Типы туризма'},
        ),
        migrations.AlterField(
            model_name='tourizmtype',
            name='content',
            field=models.TextField(blank=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='tourizmtype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='tourizmtype',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано?'),
        ),
        migrations.AlterField(
            model_name='tourizmtype',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='tourizmtype',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='tourizmtype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлено'),
        ),
    ]