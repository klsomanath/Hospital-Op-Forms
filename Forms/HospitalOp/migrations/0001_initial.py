# Generated by Django 4.0.2 on 2022-02-22 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('text', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
    ]
