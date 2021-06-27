from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movies, Reviews
from .serializers import MovieListSerializer, MovieReviewSeralizer


class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movies.objects.all()
        return render(request, "movies/movie_list.html", {"movie_list": movies})


class MovieDetailView(View):
    """Полное описание фильма"""
    def get(self, request, pk):
        movie = Movies.objects.get(id=pk)
        reviews = Reviews.objects.filter(movie_id=pk)
        return render(request, "movies/movie_detail.html", {"movie":movie, "reviews": reviews})


class MovieListView(APIView):
    """Вывод списка фильмов через сериализаторы"""
    def get(self, request):
        movies = Movies.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class MovieReviews(APIView):
    """Вывод списка фильмов жанра комедии через сериализаторы"""
    def get(self, request):
        reviews = Reviews.objects.all()
        serializer = MovieReviewSeralizer(reviews, many=True)
        return Response(serializer.data)


