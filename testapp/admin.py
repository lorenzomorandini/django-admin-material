from django.contrib import admin
from . import models


@admin.register(models.TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_1', 'text_2')


@admin.register(models.Test2Model)
class Test2ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'test')
    raw_id_fields = ('test_2',)
