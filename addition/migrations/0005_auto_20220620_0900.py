# Generated by Django 3.1.7 on 2022-06-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addition', '0004_inner_page_number_on_off'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inner_page',
            name='rec_on_off',
            field=models.IntegerField(default=1),
        ),
    ]
