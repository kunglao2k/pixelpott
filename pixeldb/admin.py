from django.contrib import admin
from django import forms
from .models import Blog, Game, Publisher, Developer, Genre, Platform

class BlogAdminForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ['headline', 'slug', 'Game', 'created', 'last_updated']
    readonly_fields = ['slug']

admin.site.register(Blog, BlogAdmin)


class GameAdminForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = '__all__'


class GameAdmin(admin.ModelAdmin):
    form = GameAdminForm
    list_display = ['name', 'slug']
    readonly_fields = ['slug']

admin.site.register(Game, GameAdmin)


class PublisherAdminForm(forms.ModelForm):

    class Meta:
        model = Publisher
        fields = '__all__'


class PublisherAdmin(admin.ModelAdmin):
    form = PublisherAdminForm
    list_display = ['name', 'slug']
    readonly_fields = ['slug']

admin.site.register(Publisher, PublisherAdmin)


class DeveloperAdminForm(forms.ModelForm):

    class Meta:
        model = Developer
        fields = '__all__'


class DeveloperAdmin(admin.ModelAdmin):
    form = DeveloperAdminForm
    list_display = ['name', 'slug']
    readonly_fields = ['slug']

admin.site.register(Developer, DeveloperAdmin)


class GenreAdminForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = '__all__'


class GenreAdmin(admin.ModelAdmin):
    form = GenreAdminForm
    list_display = ['name', 'slug']
    readonly_fields = ['slug']

admin.site.register(Genre, GenreAdmin)


class PlatformAdminForm(forms.ModelForm):

    class Meta:
        model = Platform
        fields = '__all__'


class PlatformAdmin(admin.ModelAdmin):
    form = PlatformAdminForm
    list_display = ['name', 'slug']
    readonly_fields = ['slug']

admin.site.register(Platform, PlatformAdmin)


