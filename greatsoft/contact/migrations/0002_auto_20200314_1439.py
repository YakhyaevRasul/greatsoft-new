# Generated by Django 3.0.4 on 2020-03-14 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactto',
            options={'ordering': ('date',)},
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'ordering': ('date',)},
        ),
    ]
