# Generated by Django 4.2.3 on 2023-07-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('is_student', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
