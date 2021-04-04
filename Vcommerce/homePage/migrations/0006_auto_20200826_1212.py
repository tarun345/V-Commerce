# Generated by Django 3.1 on 2020-08-26 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0005_auto_20200826_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='company',
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homePage.companies'),
        ),
    ]
