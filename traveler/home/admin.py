from django.contrib import admin
from .models import AttractionType, Region, Attraction

@admin.register(AttractionType)
class AttractionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    fields = ('name', 'region_id', 'attraction_type_id', 'info', 'image_path')
    list_filter = ('region_id', 'attraction_type_id')
    search_fields = ('name', 'info') 
