# Generated by Django 2.2.5 on 2019-09-09 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20190905_1804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]
