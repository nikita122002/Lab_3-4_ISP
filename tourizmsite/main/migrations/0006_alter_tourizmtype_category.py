# Generated by Django 4.0.4 on 2022-06-05 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_category_tourizmtype_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourizmtype',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Категории'),
        ),
    ]