from rest_framework import serializers
from movies.models import Movie, Genre, Review
from django.contrib.auth.models import User

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_date', 'genre')

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'summary', 'date_created', 'owner', 'movie')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(many=True, queryset=Review.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'reviews')