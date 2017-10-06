from . import models
from . import serializers
from rest_framework import viewsets, permissions


class BlogViewSet(viewsets.ModelViewSet):
    """ViewSet for the Blog class"""

    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [permissions.IsAuthenticated]


class GameViewSet(viewsets.ModelViewSet):
    """ViewSet for the Game class"""

    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    permission_classes = [permissions.IsAuthenticated]


class PublisherViewSet(viewsets.ModelViewSet):
    """ViewSet for the Publisher class"""

    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeveloperViewSet(viewsets.ModelViewSet):
    """ViewSet for the Developer class"""

    queryset = models.Developer.objects.all()
    serializer_class = serializers.DeveloperSerializer
    permission_classes = [permissions.IsAuthenticated]


class GenreViewSet(viewsets.ModelViewSet):
    """ViewSet for the Genre class"""

    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlatformViewSet(viewsets.ModelViewSet):
    """ViewSet for the Platform class"""

    queryset = models.Platform.objects.all()
    serializer_class = serializers.PlatformSerializer
    permission_classes = [permissions.IsAuthenticated]


