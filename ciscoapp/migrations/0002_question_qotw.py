# Generated by Django 2.1.3 on 2019-01-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciscoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='qotw',
            field=models.CharField(db_column='qotw', default='n', max_length=1),
        ),
    ]
