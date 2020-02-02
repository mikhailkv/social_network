from django.db import models


class PhotoFileQuerySet(models.QuerySet):
    def delete(self):
        self.update(is_deleted=True)


class PhotoFileManager(models.Manager):
    def get_queryset(self):
        return PhotoFileQuerySet(self.model, using=self._db).filter(is_deleted=False)


class PhotoFileNotApproveManager(models.Manager):
    def get_queryset(self):
        return PhotoFileQuerySet(self.model, using=self._db).filter(is_deleted=False, is_approved=False)


class PhotoFileManagerAll(models.Manager):
    def get_queryset(self):
        return PhotoFileQuerySet(self.model, using=self._db)


class EntryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()


class EntryPhotoFileApproveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(photos__is_approved=True)


class EntryPhotoFileNotApproveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(photos__is_approved=False)
