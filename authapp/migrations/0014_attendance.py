# Generated by Django 5.0.1 on 2024-02-08 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Selectdate', models.DateTimeField(auto_now_add=True)),
                ('phonenumber', models.CharField(default='your_default_value_here', max_length=15)),
                ('Login', models.CharField(max_length=200)),
                ('Logout', models.CharField(max_length=200, null=True)),
                ('SelectWorkout', models.CharField(max_length=200)),
                ('TrainedBy', models.CharField(max_length=200)),
            ],
        ),
    ]
