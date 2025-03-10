# Generated by Django 5.1.6 on 2025-02-26 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='available',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='image',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='quantity',
        ),
        migrations.AddField(
            model_name='equipment',
            name='quantity_available',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
