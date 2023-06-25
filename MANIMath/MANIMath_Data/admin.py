from django.contrib import admin
from .models import *

class FunctionModelAdmin(admin.ModelAdmin):
    readonly_fields = ('formatted_create_date',)
    def formatted_create_date(self, obj):
        return obj.create_date.strftime('%Y-%m-%d %H:%M:%S')

    formatted_create_date.short_description = 'Create Date'

class RootFindingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('formatted_create_date',)
    def formatted_create_date(self, obj):
        return obj.create_date.strftime('%Y-%m-%d %H:%M:%S')

    formatted_create_date.short_description = 'Create Date'

class SortModelAdmin(admin.ModelAdmin):
    readonly_fields = ('formatted_create_date',)
    def formatted_create_date(self, obj):
        return obj.create_date.strftime('%Y-%m-%d %H:%M:%S')

    formatted_create_date.short_description = 'Create Date'

class SearchModelAdmin(admin.ModelAdmin):
    readonly_fields = ('formatted_create_date',)
    def formatted_create_date(self, obj):
        return obj.create_date.strftime('%Y-%m-%d %H:%M:%S')

    formatted_create_date.short_description = 'Create Date'

admin.site.register(FunctionModel,FunctionModelAdmin)
admin.site.register(RootFindingModel,RootFindingModelAdmin)
admin.site.register(SearchModel,SearchModelAdmin)
admin.site.register(SortModel,SortModelAdmin)