# Generated by Django 3.2.23 on 2024-02-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'teacher',
                'managed': False,
            },
        ),
    ]
