# Generated by Django 2.1 on 2020-12-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.CharField(max_length=200)),
                ('creation', models.DateTimeField(verbose_name='creation')),
                ('age', models.IntegerField()),
                ('covid', models.BooleanField()),
                ('UID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='xapi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=40)),
                ('interactionType', models.CharField(max_length=15)),
                ('objectLink', models.CharField(max_length=200)),
                ('localId', models.IntegerField()),
                ('objectName', models.CharField(max_length=100)),
                ('correct', models.CharField(max_length=500)),
                ('answers', models.CharField(max_length=1500)),
                ('description', models.CharField(max_length=500)),
                ('categoryId', models.CharField(max_length=500)),
                ('minScore', models.IntegerField()),
                ('maxScore', models.IntegerField()),
                ('raw', models.FloatField()),
                ('scaled', models.FloatField()),
                ('completion', models.BooleanField()),
                ('success', models.BooleanField()),
                ('response', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='xapiRaw',
            fields=[
                ('UID', models.AutoField(primary_key=True, serialize=False)),
                ('raw', models.CharField(max_length=1500)),
            ],
        ),
    ]