# Generated by Django 5.0 on 2024-03-03 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0019_remove_slice_level_remove_slice_lft_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplAntarez',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GallerySet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('imgset', models.ManyToManyField(related_name='imgset', to='panel.gallery')),
            ],
        ),
    ]