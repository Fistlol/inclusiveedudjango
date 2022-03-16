# Generated by Django 4.0.3 on 2022-03-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('theory', models.CharField(max_length=200)),
                ('video', models.CharField(max_length=200)),
                ('matches', models.CharField(max_length=200)),
                ('missing_word', models.CharField(max_length=200)),
                ('right_order', models.CharField(max_length=200)),
                ('right_answer', models.CharField(max_length=200)),
            ],
        ),
    ]
