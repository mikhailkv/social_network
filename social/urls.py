from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from social.views import AttributeViewSet, PhotoFileSet, EntryNotApproveViewSet, EntryApproveViewSet

schema_view = get_swagger_view(title='Social API')
router = DefaultRouter()
router.register(r'attribute', AttributeViewSet, basename='Attributes')
router.register(r'entry_approve', EntryApproveViewSet, basename='Entries')
router.register(r'entry_not_approve', EntryNotApproveViewSet, basename='Entries')
router.register(r'photo_file_not_approve', PhotoFileSet, basename='Photo Files')

urlpatterns = router.urls + [
    path('api/', schema_view),
]
