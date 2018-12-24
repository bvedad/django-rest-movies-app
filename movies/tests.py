from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Genre, Movie
from movies.serializers import GenreSerializer, MovieSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_genre(name=""):
        if name != "":
            return Genre.objects.create(name=name)

    @staticmethod
    def create_movie(title="", release_date="", genre=""):
        if title != "" and release_date != "" and genre != "":
            res = Movie.objects.create(title=title, release_date=release_date)
            res.genre.add(genre)



class GenresTest(BaseViewTest):

    def setUp(self):
        # add test data
        self.create_genre(name="Action")
        self.create_genre(name="Drama")
        self.create_genre(name="Comedy")
        self.create_genre(name="War")

    def test_get_all_genres(self):
        """
        This test ensures that all genres added in the setUp method
        exist when we make a GET request to the /genres endpoint
        """
        response = self.client.get('/genres')
        expected = Genre.objects.all()
        serialized = GenreSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_genre(self):
        """
        This test ensures that genre added in the setUp method
        exist when we make a GET request to the /genres/1 endpoint
        """
        response = self.client.get('/genres/1')
        expected = Genre.objects.get(id=1)
        serialized = GenreSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_genre(self):
        """
        This test ensures that genre can be successfuly created
        when we make a POST request to the /genres endpoint
        """
        response = self.client.post('/genres', {'name': 'Thriller'}, format='json')
        self.assertEqual(response.data['name'], 'Thriller')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_genre(self):
        """
        This test ensures that genre can be successfuly updated
        when we make a PUT request to the genres/1 endpoint
        """
        response = self.client.put('/genres/1', {'name': 'Fiction'}, format='json')
        self.assertEqual(response.data['name'], 'Fiction')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class MoviesTest(BaseViewTest):

    def setUp(self):
        # add test data
        genreAction = self.create_genre(name="Action")
        self.create_genre(name="Drama")
        self.create_movie("Movie1", "2018-10-10", genreAction)
        self.create_movie("Movie2", "2018-11-10", genreAction)

    def test_get_all_movies(self):
        """
        This test ensures that all genres added in the setUp method
        exist when we make a GET request to the /genres endpoint
        """
        response = self.client.get('/movies')
        expected = Movie.objects.all()
        serialized = MovieSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_movie(self):
        """
        This test ensures that genre added in the setUp method
        exist when we make a GET request to the /movies/1 endpoint
        """
        response = self.client.get('/movies/1')
        expected = Movie.objects.get(id=1)
        serialized = MovieSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_movie(self):
        """
        This test ensures that genre can be successfuly created
        when we make a POST request to the /movies endpoint
        """
        response = self.client.post('/movies', {'title': 'Movie3', 'release_date': '2018-12-10', 'genre': [1]}, format='json')
        self.assertEqual(response.data['title'], 'Movie3')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_movie(self):
        """
        This test ensures that genre can be successfuly updated
        when we make a PUT request to the genres/1 endpoint
        """
        json_data = {'id': 1, 'title': 'Movie1-new', 'release_date': '2018-12-10', 'genre': [1, 2]}
        response = self.client.put('/movies/1', json_data, format='json')
        self.assertEqual(response.data, json_data);
        self.assertEqual(response.status_code, status.HTTP_200_OK)