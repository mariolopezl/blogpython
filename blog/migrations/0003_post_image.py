# Generated by Django 4.0.5 on 2022-06-05 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='featured_image/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
