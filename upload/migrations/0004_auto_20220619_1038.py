# Generated by Django 3.1.7 on 2022-06-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_alter_up_file_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='up_file',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
