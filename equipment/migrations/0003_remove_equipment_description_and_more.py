# Generated by Django 5.1.6 on 2025-02-26 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_remove_equipment_available_remove_equipment_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='description',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='quantity_available',
        ),
        migrations.AddField(
            model_name='equipment',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipment',
            name='status',
            field=models.CharField(default='Available', max_length=50),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
