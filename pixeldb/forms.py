from django import forms
from .models import Blog, Game, Publisher, Developer, Genre, Platform


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['headline', 'author', 'Game']


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'publisher', 'Developer', 'Platform', 'Genre']


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['name']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name']


