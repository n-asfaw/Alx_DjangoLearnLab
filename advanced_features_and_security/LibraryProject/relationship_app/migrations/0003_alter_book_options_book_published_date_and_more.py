# Generated by Django 5.1.2 on 2024-11-28 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_alter_book_author_alter_book_title_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_book', 'Can add a book'), ('can_change_book', 'Can change a book'), ('can_delete_book', 'Can delete a book')]},
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default=1985),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
