# Generated by Django 3.1.4 on 2022-03-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles_api', '0002_auto_20220325_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]