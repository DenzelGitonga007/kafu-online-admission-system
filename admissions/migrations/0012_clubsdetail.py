# Generated by Django 4.2 on 2023-05-15 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admissions', '0011_rename_games_represenation_gamesdetail_games_representation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubsDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_club', models.CharField(max_length=50)),
                ('second_club', models.CharField(max_length=50)),
                ('third_club', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
