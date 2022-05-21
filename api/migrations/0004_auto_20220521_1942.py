# Generated by Django 3.1.4 on 2022-05-21 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220126_0644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='address',
            new_name='locations',
        ),
        migrations.RemoveField(
            model_name='company',
            name='description',
        ),
        migrations.RemoveField(
            model_name='company',
            name='facebook_link',
        ),
        migrations.RemoveField(
            model_name='company',
            name='founded',
        ),
        migrations.RemoveField(
            model_name='company',
            name='title',
        ),
        migrations.AddField(
            model_name='company',
            name='varified',
            field=models.BooleanField(default=False),
        ),
    ]