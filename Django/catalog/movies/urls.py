from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'movies'),
    path('<int:movie_id>', views.detail, name = 'movies'),
    path('search', views.search, name = 'search')

]

