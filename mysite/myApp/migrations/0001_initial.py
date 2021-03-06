# Generated by Django 2.2.11 on 2020-04-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_heading', models.CharField(max_length=200)),
                ('article_text', models.CharField(max_length=1024)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
