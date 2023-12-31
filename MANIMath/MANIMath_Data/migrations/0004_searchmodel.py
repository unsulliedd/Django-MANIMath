# Generated by Django 4.2.2 on 2023-06-25 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MANIMath_WebUI', '0002_alter_category_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MANIMath_Data', '0003_sortmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('custom_animation_name', models.CharField(blank=True, max_length=256, null=True)),
                ('input_array', models.CharField(blank=True, max_length=128, null=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MANIMath_WebUI.category')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MANIMath_WebUI.topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Search Algorithm Model',
                'verbose_name_plural': 'Search Algorithm Model',
            },
        ),
    ]
