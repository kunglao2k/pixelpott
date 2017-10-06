from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Blog, Game, Publisher, Developer, Genre, Platform
from .forms import BlogForm, GameForm, PublisherForm, DeveloperForm, GenreForm, PlatformForm


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm


class GameListView(ListView):
    model = Game


class GameCreateView(CreateView):
    model = Game
    form_class = GameForm


class GameDetailView(DetailView):
    model = Game


class GameUpdateView(UpdateView):
    model = Game
    form_class = GameForm


class PublisherListView(ListView):
    model = Publisher


class PublisherCreateView(CreateView):
    model = Publisher
    form_class = PublisherForm


class PublisherDetailView(DetailView):
    model = Publisher


class PublisherUpdateView(UpdateView):
    model = Publisher
    form_class = PublisherForm


class DeveloperListView(ListView):
    model = Developer


class DeveloperCreateView(CreateView):
    model = Developer
    form_class = DeveloperForm


class DeveloperDetailView(DetailView):
    model = Developer


class DeveloperUpdateView(UpdateView):
    model = Developer
    form_class = DeveloperForm


class GenreListView(ListView):
    model = Genre


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm


class GenreDetailView(DetailView):
    model = Genre


class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm


class PlatformListView(ListView):
    model = Platform


class PlatformCreateView(CreateView):
    model = Platform
    form_class = PlatformForm


class PlatformDetailView(DetailView):
    model = Platform


class PlatformUpdateView(UpdateView):
    model = Platform
    form_class = PlatformForm

