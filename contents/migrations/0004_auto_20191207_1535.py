# Generated by Django 2.2.6 on 2019-12-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_remove_images_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, to='contents.Images'),
        ),
    ]