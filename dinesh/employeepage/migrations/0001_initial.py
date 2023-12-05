# Generated by Django 4.2.6 on 2023-12-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('empname', models.CharField(max_length=15)),
                ('empphno', models.IntegerField()),
                ('empsalary', models.IntegerField()),
                ('empaddress', models.CharField(max_length=20)),
            ],
        ),
    ]