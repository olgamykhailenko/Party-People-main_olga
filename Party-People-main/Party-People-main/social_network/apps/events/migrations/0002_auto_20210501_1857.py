# Generated by Django 3.2 on 2021-05-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comment'},
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Like', 'verbose_name_plural': 'Likes'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_pubdate',
            field=models.DateTimeField(verbose_name='Publication date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=350, verbose_name='Text of comment'),
        ),
    ]
