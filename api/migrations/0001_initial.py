# Generated by Django 3.2.3 on 2021-05-29 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=5, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('master_category', models.CharField(max_length=20)),
                ('sub_category', models.CharField(max_length=20)),
                ('article_type', models.CharField(max_length=20)),
                ('base_color', models.CharField(max_length=20)),
                ('season', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=10)),
                ('usage', models.CharField(max_length=20)),
                ('display_name', models.CharField(max_length=100)),
            ],
        ),
    ]