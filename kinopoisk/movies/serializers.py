from rest_framework import serializers

from .models import Movies, Reviews


class MovieListSerializer(serializers.ModelSerializer):
    """Список фильмов"""
    class Meta:
        model = Movies
        fields = ("name", "description")


class MovieReviewSeralizer(serializers.ModelSerializer):
    """Вывод списка отзывов к фильмам без поля movie"""
    class Meta:
        model = Reviews
        exclude = ("movie",)