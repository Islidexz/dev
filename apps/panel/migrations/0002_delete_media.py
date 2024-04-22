# Generated by Django 5.0.4 on 2024-04-18 18:04

from django.db import migrations
from django.db import connection

def forwards_func(apps, schema_editor):
    # Получаем имя таблицы из модели
    model = apps.get_model("panel", "Media")
    table_name = model._meta.db_table
    # Проверяем, существует ли таблица
    if table_name in connection.introspection.table_names():
        schema_editor.delete_model(model)

class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
