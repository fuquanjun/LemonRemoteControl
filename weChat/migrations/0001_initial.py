# Generated by Django 2.0.7 on 2018-07-27 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corp_id', models.CharField(max_length=200)),
                ('secret', models.CharField(max_length=200)),
                ('agent_id', models.CharField(max_length=10)),
                ('tag_id', models.CharField(max_length=10)),
            ],
        ),
    ]
