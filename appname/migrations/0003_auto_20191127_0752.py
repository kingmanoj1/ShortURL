# Generated by Django 2.2.7 on 2019-11-27 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0002_clientdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlcode',
            name='create_date',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientdetail',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appname.Urlcode'),
        ),
    ]
