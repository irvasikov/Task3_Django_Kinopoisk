from django.db import models
from django.urls import reverse


class Genres(models.Model):
    """Категории фильмов"""
    name = models.CharField("Жанр", max_length=160)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movies(models.Model):
    """Фильмы и их описание"""
    name = models.CharField("Название фильма", max_length=160)
    description = models.TextField("Описание")
    year = models.DateField("Год выпуска")
    genre = models.ForeignKey(Genres, verbose_name="Жанр", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Reviews(models.Model):
    """Рецензии к фильмам"""
    name = models.CharField("Имя пользователя", max_length=160)
    email = models.EmailField()
    text = models.TextField("Текст рецензии")
    movie = models.ForeignKey(Movies, verbose_name="Фильм", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Рецензия"
        verbose_name_plural = "Рецензии"


class Comments(models.Model):
    """Комментарии к рецензиям"""
    name = models.CharField("Имя пользователя", max_length=160)
    email = models.EmailField()
    text = models.TextField("Текст комментария")
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    review = models.ForeignKey(Reviews, verbose_name="Рецензия", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} - {self.review}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"