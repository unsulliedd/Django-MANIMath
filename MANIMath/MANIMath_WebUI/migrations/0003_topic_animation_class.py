# Generated by Django 4.2.2 on 2023-07-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MANIMath_WebUI', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='animation_class',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
