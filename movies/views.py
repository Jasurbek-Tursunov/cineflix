from django.shortcuts import render
from django.views.generic import View

from .models import Movie


class MoviesView(View):
    """Список фильмов"""
    def get(self,request):
        movie = Movie.objects.all()
        return render(request, "base.html")

    """, {"movie_list":movie}"""