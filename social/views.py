from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from social.models import Attribute, Entry, PhotoFile
from social.serializers import AttributeSerializer, EntrySerializer, PhotoFileSerializer


class AttributeViewSet(ModelViewSet):
    serializer_class = AttributeSerializer
    queryset = Attribute.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
    search_fields = ('name', )
    ordering_fields = ('name', )


class EntryApproveViewSet(ModelViewSet):
    serializer_class = EntrySerializer
    queryset = Entry.objects_approve.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
    search_fields = ('name', )
    ordering_fields = ('name', )


class EntryNotApproveViewSet(ModelViewSet):
    serializer_class = EntrySerializer
    queryset = Entry.objects_not_approve.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
    search_fields = ('name', )
    ordering_fields = ('name', )


class PhotoFileSet(ModelViewSet):
    serializer_class = PhotoFileSerializer
    queryset = PhotoFile.objects_not_approve.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
    search_fields = ('name', )
    ordering_fields = ('name', )
