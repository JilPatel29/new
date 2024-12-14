# Generated by Django 5.0.6 on 2024-10-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]