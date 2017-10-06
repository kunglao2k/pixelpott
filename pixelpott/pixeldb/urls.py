from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'blog', api.BlogViewSet)
router.register(r'game', api.GameViewSet)
router.register(r'publisher', api.PublisherViewSet)
router.register(r'developer', api.DeveloperViewSet)
router.register(r'genre', api.GenreViewSet)
router.register(r'platform', api.PlatformViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Blog
    url(r'^pixeldb/blog/$', views.BlogListView.as_view(), name='pixeldb_blog_list'),
    url(r'^pixeldb/blog/create/$', views.BlogCreateView.as_view(), name='pixeldb_blog_create'),
    url(r'^pixeldb/blog/detail/(?P<slug>\S+)/$', views.BlogDetailView.as_view(), name='pixeldb_blog_detail'),
    url(r'^pixeldb/blog/update/(?P<slug>\S+)/$', views.BlogUpdateView.as_view(), name='pixeldb_blog_update'),
)

urlpatterns += (
    # urls for Game
    url(r'^pixeldb/game/$', views.GameListView.as_view(), name='pixeldb_game_list'),
    url(r'^pixeldb/game/create/$', views.GameCreateView.as_view(), name='pixeldb_game_create'),
    url(r'^pixeldb/game/detail/(?P<slug>\S+)/$', views.GameDetailView.as_view(), name='pixeldb_game_detail'),
    url(r'^pixeldb/game/update/(?P<slug>\S+)/$', views.GameUpdateView.as_view(), name='pixeldb_game_update'),
)

urlpatterns += (
    # urls for Publisher
    url(r'^pixeldb/publisher/$', views.PublisherListView.as_view(), name='pixeldb_publisher_list'),
    url(r'^pixeldb/publisher/create/$', views.PublisherCreateView.as_view(), name='pixeldb_publisher_create'),
    url(r'^pixeldb/publisher/detail/(?P<slug>\S+)/$', views.PublisherDetailView.as_view(), name='pixeldb_publisher_detail'),
    url(r'^pixeldb/publisher/update/(?P<slug>\S+)/$', views.PublisherUpdateView.as_view(), name='pixeldb_publisher_update'),
)

urlpatterns += (
    # urls for Developer
    url(r'^pixeldb/developer/$', views.DeveloperListView.as_view(), name='pixeldb_developer_list'),
    url(r'^pixeldb/developer/create/$', views.DeveloperCreateView.as_view(), name='pixeldb_developer_create'),
    url(r'^pixeldb/developer/detail/(?P<slug>\S+)/$', views.DeveloperDetailView.as_view(), name='pixeldb_developer_detail'),
    url(r'^pixeldb/developer/update/(?P<slug>\S+)/$', views.DeveloperUpdateView.as_view(), name='pixeldb_developer_update'),
)

urlpatterns += (
    # urls for Genre
    url(r'^pixeldb/genre/$', views.GenreListView.as_view(), name='pixeldb_genre_list'),
    url(r'^pixeldb/genre/create/$', views.GenreCreateView.as_view(), name='pixeldb_genre_create'),
    url(r'^pixeldb/genre/detail/(?P<slug>\S+)/$', views.GenreDetailView.as_view(), name='pixeldb_genre_detail'),
    url(r'^pixeldb/genre/update/(?P<slug>\S+)/$', views.GenreUpdateView.as_view(), name='pixeldb_genre_update'),
)

urlpatterns += (
    # urls for Platform
    url(r'^pixeldb/platform/$', views.PlatformListView.as_view(), name='pixeldb_platform_list'),
    url(r'^pixeldb/platform/create/$', views.PlatformCreateView.as_view(), name='pixeldb_platform_create'),
    url(r'^pixeldb/platform/detail/(?P<slug>\S+)/$', views.PlatformDetailView.as_view(), name='pixeldb_platform_detail'),
    url(r'^pixeldb/platform/update/(?P<slug>\S+)/$', views.PlatformUpdateView.as_view(), name='pixeldb_platform_update'),
)

