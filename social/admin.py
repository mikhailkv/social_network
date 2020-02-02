from django.contrib import admin

from social.forms import EntryForm
from social.models import Attribute, Entry, PhotoFile


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    fields = ('name', 'type_attribute', )
    search_fields = ('name', )


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    fields = ('name', 'user', 'attribute', )
    search_fields = ('name',)
    form = EntryForm


@admin.register(PhotoFile)
class PhotoFileAdmin(admin.ModelAdmin):
    fields = ('name', 'user', 'entry', 'file', 'is_deleted', 'is_approved', )
    search_fields = ('name',)
