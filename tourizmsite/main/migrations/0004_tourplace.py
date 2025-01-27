# Generated by Django 4.0.4 on 2022-06-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_tourizmtype_options_alter_tourizmtype_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('tourtype', models.TextField(blank=True, verbose_name='Тип туризма')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано?')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'ordering': ['-created_at'],
            },
        ),
    ]
