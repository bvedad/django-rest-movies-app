from rest_framework import routers
from django.conf.urls import url, include
from movies import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'genres', views.GenreViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
