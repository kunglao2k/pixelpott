from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Blog(models.Model):

    # Fields
    headline = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    author = models.ForeignKey(settings.AUTH_USER_MODEL, )
    Game = models.ForeignKey('pixeldb.Game', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('pixeldb_blog_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('pixeldb_blog_update', args=(self.slug,))


class Game(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    # Relationship Fields
    publisher = models.ForeignKey('pixeldb.Publisher', )
    Developer = models.ManyToManyField('pixeldb.Developer', )
    Platform = models.ManyToManyField('pixeldb.Platform', )
    Genre = models.ForeignKey('pixeldb.Genre', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('pixeldb_game_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('pixeldb_game_update', args=(self.slug,))


class Publisher(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('pixeldb_publisher_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('pixeldb_publisher_update', args=(self.slug,))


class Developer(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('pixeldb_developer_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('pixeldb_developer_update', args=(self.slug,))


class Genre(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('pixeldb_genre_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('pixeldb_genre_update', args=(self.slug,))


class Platform(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('pixeldb_platform_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('pixeldb_platform_update', args=(self.slug,))


