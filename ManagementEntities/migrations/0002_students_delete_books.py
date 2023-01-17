# Generated by Django 4.1.3 on 2022-11-30 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagementEntities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentId', models.CharField(max_length=255)),
                ('StudentName', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=255)),
                ('Year', models.CharField(max_length=255)),
                ('ClassId', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
