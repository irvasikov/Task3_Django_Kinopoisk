from django.contrib import admin
from .models import Genres, Movies, Reviews, Comments


admin.site.register(Genres)
admin.site.register(Movies)
admin.site.register(Reviews)
admin.site.register(Comments)