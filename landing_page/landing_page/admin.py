from django.contrib import admin
from . import models


@admin.register(models.Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    list_editable = ('content',)
