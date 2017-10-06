import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Blog, Game, Publisher, Developer, Genre, Platform
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_blog(**kwargs):
    defaults = {}
    defaults["headline"] = "headline"
    defaults.update(**kwargs)
    if "author" not in defaults:
        defaults["author"] = create_django_contrib_auth_models_user()
    if "Game" not in defaults:
        defaults["Game"] = create_game()
    return Blog.objects.create(**defaults)


def create_game(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "publisher" not in defaults:
        defaults["publisher"] = create_publisher()
    if "Developer" not in defaults:
        defaults["Developer"] = create_developer()
    if "Platform" not in defaults:
        defaults["Platform"] = create_platform()
    if "Genre" not in defaults:
        defaults["Genre"] = create_genre()
    return Game.objects.create(**defaults)


def create_publisher(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Publisher.objects.create(**defaults)


def create_developer(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Developer.objects.create(**defaults)


def create_genre(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Genre.objects.create(**defaults)


def create_platform(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Platform.objects.create(**defaults)


class BlogViewTest(unittest.TestCase):
    '''
    Tests for Blog
    '''
    def setUp(self):
        self.client = Client()

    def test_list_blog(self):
        url = reverse('pixeldb_blog_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_blog(self):
        url = reverse('pixeldb_blog_create')
        data = {
            "headline": "headline",
            "author": create_django_contrib_auth_models_user().pk,
            "Game": create_game().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_blog(self):
        blog = create_blog()
        url = reverse('pixeldb_blog_detail', args=[blog.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_blog(self):
        blog = create_blog()
        data = {
            "headline": "headline",
            "author": create_django_contrib_auth_models_user().pk,
            "Game": create_game().pk,
        }
        url = reverse('pixeldb_blog_update', args=[blog.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class GameViewTest(unittest.TestCase):
    '''
    Tests for Game
    '''
    def setUp(self):
        self.client = Client()

    def test_list_game(self):
        url = reverse('pixeldb_game_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_game(self):
        url = reverse('pixeldb_game_create')
        data = {
            "name": "name",
            "publisher": create_publisher().pk,
            "Developer": create_developer().pk,
            "Platform": create_platform().pk,
            "Genre": create_genre().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_game(self):
        game = create_game()
        url = reverse('pixeldb_game_detail', args=[game.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_game(self):
        game = create_game()
        data = {
            "name": "name",
            "publisher": create_publisher().pk,
            "Developer": create_developer().pk,
            "Platform": create_platform().pk,
            "Genre": create_genre().pk,
        }
        url = reverse('pixeldb_game_update', args=[game.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PublisherViewTest(unittest.TestCase):
    '''
    Tests for Publisher
    '''
    def setUp(self):
        self.client = Client()

    def test_list_publisher(self):
        url = reverse('pixeldb_publisher_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_publisher(self):
        url = reverse('pixeldb_publisher_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_publisher(self):
        publisher = create_publisher()
        url = reverse('pixeldb_publisher_detail', args=[publisher.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_publisher(self):
        publisher = create_publisher()
        data = {
            "name": "name",
        }
        url = reverse('pixeldb_publisher_update', args=[publisher.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DeveloperViewTest(unittest.TestCase):
    '''
    Tests for Developer
    '''
    def setUp(self):
        self.client = Client()

    def test_list_developer(self):
        url = reverse('pixeldb_developer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_developer(self):
        url = reverse('pixeldb_developer_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_developer(self):
        developer = create_developer()
        url = reverse('pixeldb_developer_detail', args=[developer.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_developer(self):
        developer = create_developer()
        data = {
            "name": "name",
        }
        url = reverse('pixeldb_developer_update', args=[developer.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class GenreViewTest(unittest.TestCase):
    '''
    Tests for Genre
    '''
    def setUp(self):
        self.client = Client()

    def test_list_genre(self):
        url = reverse('pixeldb_genre_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_genre(self):
        url = reverse('pixeldb_genre_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_genre(self):
        genre = create_genre()
        url = reverse('pixeldb_genre_detail', args=[genre.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_genre(self):
        genre = create_genre()
        data = {
            "name": "name",
        }
        url = reverse('pixeldb_genre_update', args=[genre.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PlatformViewTest(unittest.TestCase):
    '''
    Tests for Platform
    '''
    def setUp(self):
        self.client = Client()

    def test_list_platform(self):
        url = reverse('pixeldb_platform_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_platform(self):
        url = reverse('pixeldb_platform_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_platform(self):
        platform = create_platform()
        url = reverse('pixeldb_platform_detail', args=[platform.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_platform(self):
        platform = create_platform()
        data = {
            "name": "name",
        }
        url = reverse('pixeldb_platform_update', args=[platform.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


