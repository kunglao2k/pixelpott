from . import models

from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = (
            'slug', 
            'headline', 
            'created', 
            'last_updated', 
        )


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Game
        fields = (
            'slug', 
            'name', 
        )


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Publisher
        fields = (
            'slug', 
            'name', 
        )


class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Developer
        fields = (
            'slug', 
            'name', 
        )


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Genre
        fields = (
            'slug', 
            'name', 
        )


class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Platform
        fields = (
            'slug', 
            'name', 
        )


