# Generated by Django 4.1.4 on 2023-04-17 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0011_rename_condition_usermodel_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='on_delete',
            field=models.BooleanField(default=False),
        ),
    ]