from django.contrib import admin
from .models import (
    Category,
    Genre,
    Movie,
    MovieShots,
    Actor,
    Reting,
    RetingStar,
    Reviews
)


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Reting)
admin.site.register(RetingStar)
admin.site.register(Reviews)