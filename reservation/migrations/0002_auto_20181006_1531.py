# Generated by Django 2.1.2 on 2018-10-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.IntegerField(choices=[(1, 'FREE'), (2, 'BUSY'), (3, 'CANCELED')], max_length=50),
        ),
    ]
