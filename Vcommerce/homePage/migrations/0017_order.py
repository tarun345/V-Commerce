# Generated by Django 3.1 on 2020-08-27 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0016_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(null=True)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('pd', 'Pendin'), ('dn', 'Done')], max_length=2, null=True)),
                ('payment_mode', models.CharField(choices=[('co', 'COD'), ('ca', 'Card'), ('nb', 'Net Banking')], max_length=2, null=True)),
                ('delivery_status', models.CharField(choices=[('pd', 'Pendin'), ('od', 'Out For Delivery'), ('de', 'Delivered')], max_length=2, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homePage.userprofile')),
            ],
        ),
    ]
