# Generated by Django 4.0.1 on 2022-02-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=12)),
                ('disease', models.CharField(max_length=55)),
                ('condition', models.TextField()),
                ('curr_prescribed', models.CharField(max_length=122)),
                ('prev_prescribed', models.CharField(max_length=122)),
            ],
        ),
    ]
