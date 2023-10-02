# Generated by Django 4.2.5 on 2023-09-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50)),
                ('dob', models.DateField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField(max_length=11)),
                ('occupation', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('nok', models.CharField(max_length=100)),
            ],
        ),
    ]