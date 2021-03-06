# Generated by Django 3.0.2 on 2020-02-02 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django_extensions.db.fields
import social.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Attribute name')),
                ('type_attribute', models.PositiveSmallIntegerField(choices=[(1, 'Country'), (2, 'City'), (3, 'Thing')], verbose_name='Type name')),
                ('level', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Hierarchy level')),
            ],
            options={
                'verbose_name': 'Attribute',
                'verbose_name_plural': 'Attributes',
                'db_table': 'attribute_object',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=200, verbose_name='Entry name')),
                ('attribute', models.ManyToManyField(to='social.Attribute', verbose_name='Attribute')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entries',
                'db_table': 'entry_object',
            },
            managers=[
                ('objects_approve', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PhotoFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=200, verbose_name='Photo name')),
                ('file', models.FileField(upload_to=social.models.user_directory_path)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False, verbose_name='To approve')),
                ('entry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photos', to='social.Entry', verbose_name='Entry')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
                'db_table': 'photo_file',
            },
        ),
    ]
