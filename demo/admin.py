from django.contrib import admin
from . import models


class Model3Inline(admin.TabularInline):
    model = models.Model3
    extra = 1


@admin.register(models.Model1)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'text_1', 'text_2')
    search_fields = ('text_1', 'text_2')
    inlines = [Model3Inline]
    fieldsets = (
        (None, {
            'classes': ('material-tab', 'material-tab-try1',),
            'fields': (
                ('text_1', 'text_2'),
            )
        }),
        ('Try 2', {
            'classes': ('material-tab', 'material-tab-try2',),
            'fields': (
                ('choice_1'),
                'boolean_1'
            )
        }),
    )
    material_tabs = (('try1', 'Try 1'), ('try2', 'Try 2'))


@admin.register(models.Model2)
class Model2Admin(admin.ModelAdmin):
    list_display = ('id', 'test')
    raw_id_fields = ('test_2',)
    autocomplete_fields = ('test_3',)
    fieldsets = (
        (None, {
            'fields': (
                'test',
                ('test_2', 'test_3'),
            )
        }),
    )