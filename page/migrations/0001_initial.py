# Generated by Django 4.0.3 on 2022-03-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id', models.CharField(max_length=10)),
                ('FIO', models.CharField(max_length=100)),
                ('kun1', models.DateField()),
                ('kun2', models.DateField()),
                ('kun3', models.DateField()),
                ('kun4', models.DateField()),
                ('kun5', models.DateField()),
                ('jami', models.CharField(max_length=100)),
            ],
        ),
    ]