# Generated by Django 4.2.2 on 2023-08-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0012_profile_comment_user_subject_comment_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='loginUser',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Girişli mi?'),
        ),
    ]
