# Generated by Django 4.2.5 on 2023-09-17 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='code')),
                ('flag', models.ImageField(blank=True, null=True, upload_to='countries/flags/', verbose_name='flag')),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='locations.country')),
            ],
            options={
                'verbose_name_plural': 'Counties',
                'ordering': ('name',),
            },
        ),
    ]
