# Generated by Django 4.2.3 on 2023-07-14 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MANIMath_Data', '0013_searchmodel_line_color_searchmodel_scale_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sortmodel',
            name='target',
        ),
        migrations.AddField(
            model_name='searchmodel',
            name='target',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
