from django.urls import path
from .views import CharactersDetail, CharactersList
urlpatterns = [
    path('characters/', CharactersList.as_view()),
    path('characters/<int:pk>/', CharactersDetail.as_view()),
]