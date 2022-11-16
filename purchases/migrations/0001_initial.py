# Generated by Django 3.1.2 on 2022-01-28 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0007_clientprofile'),
        ('menus', '0002_menuonsale_price'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='users.clientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('take_away', models.BooleanField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.menu')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='purchases.purchase')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.site')),
            ],
        ),
    ]