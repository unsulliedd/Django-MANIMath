from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, default=None)
    defination_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    def __str__(self):
        return self.name