from django.urls import path
from . import views


urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("<int:pk>/", views.MovieDetailView.as_view()),
    path("movies-json/", views.MovieListView.as_view()),
    path("reviews-json/", views.MovieReviews.as_view()),
]