# Generated by Django 3.1.7 on 2022-07-18 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordsearch', '0008_auto_20220718_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordsearch_inner_page',
            name='text_left_right',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='wordsearch_inner_page',
            name='text_up_down',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='wordsearch_inner_page',
            name='line_left_right',
            field=models.FloatField(default=-0.14),
        ),
        migrations.AlterField(
            model_name='wordsearch_inner_page',
            name='line_up_down',
            field=models.FloatField(default=-0.05),
        ),
    ]
