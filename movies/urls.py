from rest_framework import routers
from django.conf.urls import url, include
from movies import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'movies', views.MovieViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
