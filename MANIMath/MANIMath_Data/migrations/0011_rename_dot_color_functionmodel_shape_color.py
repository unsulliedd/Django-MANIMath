# Generated by Django 4.2.2 on 2023-07-10 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MANIMath_Data', '0010_alter_functionmodel_iteration_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='functionmodel',
            old_name='dot_color',
            new_name='shape_color',
        ),
    ]
