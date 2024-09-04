from django.urls import path
from .views import voter_cards

urlpatterns = [
    path('voterCards/', voter_cards, name='voter_cards'),
]
