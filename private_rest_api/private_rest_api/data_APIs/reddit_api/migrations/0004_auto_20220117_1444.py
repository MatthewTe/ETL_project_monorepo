# Generated by Django 3.1.4 on 2022-01-17 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reddit_api', '0003_auto_20211227_0241'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedditDeveloperAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_client_id', models.CharField(max_length=50)),
                ('dev_secret', models.CharField(max_length=50)),
                ('dev_user_agent', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=350, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='redditposts',
            name='subreddit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reddit_api.subreddit'),
        ),
    ]
