from django.contrib import admin

from . import models


@admin.register(models.Character)
class CharacterAdminModel(admin.ModelAdmin):
    list_display = ('id', 'name')
    readonly_fields = ('source_file',)


@admin.register(models.Planets)
class PlanetAdminModel(admin.ModelAdmin):
    list_display = ('id', 'name')
    readonly_fields = ('source_file',)
