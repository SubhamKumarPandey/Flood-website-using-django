# Generated by Django 3.1.2 on 2020-10-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_aboutngo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('loc', models.CharField(max_length=122)),
                ('cause', models.CharField(max_length=122)),
                ('death', models.IntegerField()),
                ('damage', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Data2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('loc', models.CharField(max_length=122)),
                ('cause', models.CharField(max_length=122)),
                ('death', models.IntegerField()),
                ('damage', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Data3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('loc', models.CharField(max_length=122)),
                ('cause', models.CharField(max_length=122)),
                ('death', models.IntegerField()),
                ('damage', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Data4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('loc', models.CharField(max_length=122)),
                ('cause', models.CharField(max_length=122)),
                ('death', models.IntegerField()),
                ('damage', models.CharField(max_length=122)),
            ],
        ),
    ]
