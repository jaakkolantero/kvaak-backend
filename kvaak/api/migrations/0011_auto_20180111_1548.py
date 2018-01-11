# Generated by Django 2.0.1 on 2018-01-11 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20180111_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='species',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Species', to_field='name'),
        ),
        migrations.AlterField(
            model_name='species',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
