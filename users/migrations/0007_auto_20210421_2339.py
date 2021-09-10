# Generated by Django 3.1.4 on 2021-04-22 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210412_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Recruiter'), (2, 'Candidate')], default=2),
        ),
    ]