# Generated by Django 4.2.2 on 2023-07-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MANIMath_Data', '0008_alter_functionmodel_iteration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='functionmodel',
            name='axes_color',
            field=models.CharField(blank=True, default='#ffffff', max_length=32, null=True),
        ),
    ]
