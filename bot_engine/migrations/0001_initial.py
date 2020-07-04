# Generated by Django 2.2.14 on 2020-07-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('using_place', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=400)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]