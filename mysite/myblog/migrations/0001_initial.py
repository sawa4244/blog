# Generated by Django 2.2.4 on 2019-08-12 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myblog_title', models.CharField(max_length=200)),
                ('myblog_text', models.TextField()),
                ('myblog_date', models.DateTimeField()),
                ('myblog_likes', models.IntegerField()),
            ],
            options={
                'db_table': 'myblog',
            },
        ),
    ]