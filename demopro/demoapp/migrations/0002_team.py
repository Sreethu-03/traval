# Generated by Django 3.2.16 on 2022-12-24 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=250)),
                ('img2', models.ImageField(upload_to='pics')),
                ('desc2', models.TextField()),
            ],
        ),
    ]
