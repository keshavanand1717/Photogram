# Generated by Django 4.1.5 on 2023-07-02 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialfeed', '0008_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_photos'),
        ),
    ]