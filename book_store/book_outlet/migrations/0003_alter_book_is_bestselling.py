# Generated by Django 4.2.8 on 2024-01-02 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0002_book_is_bestselling_alter_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='is_bestselling',
            field=models.BooleanField(default=False),
        ),
    ]
