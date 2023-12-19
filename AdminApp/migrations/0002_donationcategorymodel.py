# Generated by Django 4.2.7 on 2023-12-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationCategoryModel',
            fields=[
                ('donation_category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('donation_category_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'donation_category_table',
            },
        ),
    ]