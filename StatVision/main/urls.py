from django.urls import path
from .views import *
from . import views

urlpatterns = [

    path('', home, name='home'),

    path('about/', about, name='about'),

    path('autocomplete/', autocomplete, name='autocomplete'),

    path('home/', home, name='home'),

    path('mlb/', mlb, name='mlb'),

    path('nba/', nba, name='nba'),

    path('nfl/', nfl, name='nfl'),

    path('<str:league>/<str:team_name>/', views.team_page, name='team_page'),
    
    path('privacy/', privacy, name='privacy'),

    path('results/', results, name='results'),

    path('sign-in/', sign_in, name='sign-in'),

    path('sign-out/', sign_out, name='sign-out'),

    path('sign-up/', sign_up, name='sign-up'),

    path('terms/', terms, name='terms'),
    
    path('search-query/', search_view, name='search_query')
]
