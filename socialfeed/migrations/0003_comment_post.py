# Generated by Django 4.1.5 on 2023-06-18 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialfeed', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='socialfeed.post'),
            preserve_default=False,
        ),
    ]
