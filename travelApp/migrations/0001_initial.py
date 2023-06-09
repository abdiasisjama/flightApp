# Generated by Django 4.1.6 on 2023-02-03 06:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_name', models.CharField(max_length=255)),
                ('arrival_name', models.CharField(max_length=255)),
                ('IATA_code', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('passport_number', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=50)),
                ('checking_time', models.DateTimeField(max_length=255)),
                ('departure_time', models.DateTimeField(max_length=255)),
                ('arrival_time', models.DateTimeField(max_length=255)),
                ('duration_in_min', models.PositiveSmallIntegerField()),
                ('flight_class', models.CharField(choices=[('B', 'B'), ('E', 'E')], default='E', max_length=1)),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='travelApp.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.CharField(max_length=50)),
                ('confirmation_number', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1)])),
                ('issue_date', models.DateTimeField(max_length=255)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='travelApp.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='travelApp.passenger')),
            ],
        ),
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=50)),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='travelApp.airport')),
            ],
        ),
    ]
