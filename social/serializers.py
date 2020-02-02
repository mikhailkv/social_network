from rest_framework import serializers

from social.models import Attribute, Entry, PhotoFile


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'name', 'type_attribute',)


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'name', 'attribute', )


class PhotoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoFile
        fields = ('id', 'name', )
