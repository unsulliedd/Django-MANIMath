from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from MANIMath_WebUI.models import *

class FunctionModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    custom_animation_name = models.CharField(max_length=256, blank=True, null=True)
    equation1  = models.CharField(max_length=100, blank=True, null=True)
    equation2  = models.CharField(max_length=100, blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if not self.custom_animation_name:
            self.custom_animation_name = f"{self.topic.name.capitalize()}-{self.create_date.strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Function Model'
        verbose_name_plural = 'Function Model'

    def __str__(self):
        return f"{self.user.username.capitalize()} - {self.topic.name.capitalize()} - {self.create_date.strftime('%Y%m%d%H%M%S')}"

class RootFindingModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    custom_animation_name = models.CharField(max_length=256, blank=True, null=True)
    equation1  = models.CharField(max_length=100, blank=True, null=True)
    equation2  = models.CharField(max_length=100, blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if not self.custom_animation_name:
            self.custom_animation_name = f"{self.topic.name.capitalize()}-{self.create_date.strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Root Finding Algorithm Model'
        verbose_name_plural = 'Root Finding Algorithm Model'

    def __str__(self):
        return f"{self.user.username.capitalize()} - {self.topic.name.capitalize()} - {self.create_date.strftime('%Y%m%d%H%M%S')}"

class SortModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    custom_animation_name = models.CharField(max_length=256, blank=True, null=True)
    input_array = models.CharField(max_length=128,blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.custom_animation_name:
            self.custom_animation_name = f"{self.topic.name.capitalize()}-{self.create_date.strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Sort Algorithm Model'
        verbose_name_plural = 'Sort Algorithm Model'
    def __str__(self):
        return f"{self.user.username.capitalize()} - {self.topic.name.capitalize()} - {self.create_date.strftime('%Y%m%d%H%M%S')}"
class SearchModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    custom_animation_name = models.CharField(max_length=256, blank=True, null=True)
    input_array = models.CharField(max_length=128,blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if not self.custom_animation_name:
            self.custom_animation_name = f"{self.topic.name.capitalize()}-{self.create_date.strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Search Algorithm Model'
        verbose_name_plural = 'Search Algorithm Model'

    def __str__(self):
        return f"{self.user.username.capitalize()} - {self.topic.name.capitalize()} - {self.create_date.strftime('%Y%m%d%H%M%S')}"