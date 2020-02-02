from django_extensions.db.models import TimeStampedModel
from model_utils import Choices

from django.contrib.auth.models import User
from django.db import models

from social.managers import PhotoFileManager, PhotoFileManagerAll, EntryPhotoFileApproveManager, \
    EntryPhotoFileNotApproveManager, EntryManager, PhotoFileNotApproveManager

ATTRIBUTE_TYPE = (
    Choices(
        (1, 'COUNTRY', 'Country'),
        (2, 'CITY', 'City'),
        (3, 'THING', 'Thing'),
    )
)


def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'


class Attribute(TimeStampedModel):

    class Meta:
        db_table = 'attribute_object'
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'

    name = models.CharField(max_length=200, verbose_name='Attribute name', unique=True)
    type_attribute = models.PositiveSmallIntegerField(verbose_name='Type name',
                                                      choices=ATTRIBUTE_TYPE,
                                                      null=False,
                                                      blank=False)
    level = models.PositiveSmallIntegerField(verbose_name='Hierarchy level', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if self.type_attribute == ATTRIBUTE_TYPE.COUNTRY:
            self.level = 0
        elif self.type_attribute == ATTRIBUTE_TYPE.CITY:
            self.level = 1
        elif self.type_attribute == ATTRIBUTE_TYPE.THING:
            self.level = 2
        super().save(**kwargs)


class Entry(TimeStampedModel):
    class Meta:
        db_table = 'entry_object'
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    name = models.CharField(max_length=200, verbose_name='Entry name')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attribute = models.ManyToManyField(Attribute, verbose_name='Attribute')

    objects = EntryManager()
    objects_approve = EntryPhotoFileApproveManager()
    objects_not_approve = EntryPhotoFileNotApproveManager()

    def __str__(self):
        return self.name


class PhotoFile(TimeStampedModel):
    class Meta:
        db_table = 'photo_file'
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    name = models.CharField(max_length=200, verbose_name='Photo name')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='User', null=True)
    entry = models.ForeignKey(Entry, on_delete=models.SET_NULL, verbose_name='Entry', related_name='photos', null=True)
    file = models.FileField(upload_to=user_directory_path)
    is_deleted = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False, verbose_name='To approve')

    objects = PhotoFileManager()
    objects_not_approve = PhotoFileNotApproveManager()
    all_objects = PhotoFileManagerAll()

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
