# Generated by Django 4.0.2 on 2022-02-17 14:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alterado',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='criado',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 2, 17, 14, 50, 51, 19740, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2022, 2, 17, 14, 50, 2, 212825, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('rascunho', 'Rascunho'), ('publicar', 'Publicar')], default='rascunho', max_length=10),
        ),
    ]
