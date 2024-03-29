# Generated by Django 4.2.6 on 2023-10-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.CharField(max_length=20)),
                ('away', models.CharField(max_length=20)),
                ('home_scored', models.IntegerField(default=0)),
                ('away_scored', models.IntegerField(default=0)),
                ('match_status', models.CharField(max_length=30)),
            ],
        ),
    ]
