from django.shortcuts import render, redirect
from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .execute_sql import execute_sql_query
from .SQL_query_generation import generate_sql_query, generate_users_results, clean_sql_query, clean_python_table
from .forms import *
from .models import *
from datetime import date
import requests


class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


def about(request):
    return render(request, 'about.html')

def autocomplete(request):
    return render(request, 'autocomplete.html')

def home(request):
    today = date.today()
    date_params = {'year': today.year, 'month': today.month, 'day': today.day, 'limit': 10}
    all_events = []
    for abbr, path in [('MLB','mlb/scoreboard'),('NBA','nba/scoreboard'),('NFL','nfl/scoreboard')]:
        try:
            all_events += fetch_league_events(path, date_params, abbr)
        except:
            pass
    all_events.sort(key=lambda e: e.get('date',''))
    return render(request, 'home.html', {
        'events': all_events,
        'today': today,
        'league_name': None,
    })

def mlb(request):
    today = date.today()
    date_params = {'year': today.year, 'month': today.month, 'day': today.day, 'limit': 10}
    events = fetch_league_events('mlb/scoreboard', date_params, 'MLB')
    standings = fetch_standings('mlb/standings', today.year, group='league')
    return render(request, 'mlb.html', {
        'events': events,
        'standings': standings,
        'today': today,
        'league_name': 'MLB',
    })

def nba(request):
    today = date.today()
    date_params = {'year': today.year, 'month': today.month, 'day': today.day, 'limit': 10}
    events = fetch_league_events('nba/scoreboard', date_params, 'NBA')
    standings = fetch_standings('nba/standings', today.year, group='league')
    return render(request, 'nba.html', {
        'events': events,
        'standings': standings,
        'today': today,
        'league_name': 'NBA',
    })

def nfl(request):
    today = date.today()
    date_params = {'year': today.year, 'month': today.month, 'day': today.day, 'limit': 10}
    events = fetch_league_events('nfl/scoreboard', date_params, 'NFL')
    standings = fetch_standings('nfl/standings', today.year, group='league')
    return render(request, 'nfl.html', {
        'events': events,
        'standings': standings,
        'today': today,
        'league_name': 'NFL',
    })

def privacy(request):
    return render(request, 'privacy.html')

def results(request):
    return render(request, 'results.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
    return render(request, 'sign-in.html')

@login_required(login_url='sign-in')
def sign_out(request):
    logout(request)
    return redirect('home')


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('sign-in')
    else:
        form = CustomUserCreationForm()
    return render(request, 'sign-up.html', {'form': form})

def terms(request):
    return render(request, 'terms.html')

def results(request):
    try:
        search_query = None 
        results = None 

        if request.method == 'POST': 
            search_query = request.POST.get('search_query') 
            print(f"User search: {search_query}") 

            if search_query: 
                sql_query = generate_sql_query(search_query) 
                print(f"sql_query: {sql_query}") 
                sql_query = clean_sql_query(sql_query)
                print(f"sql_query_cleaned:{sql_query}")
                sql_results = execute_sql_query(sql_query) 
                results, table_result = generate_users_results(search_query ,sql_results)
                if results.startswith("Sorry"):
                    table_result = None
                else:
                    table_result = clean_python_table(table_result)
                print(f"Search Results: {results}") 

        return render(request, 'results.html', {
        'results': results,
        'table_result': table_result
        })
    except Exception as e:
        print(f"Error during search: {e}")        
        error_message = "Something went wrong, please try again."
        return render(request, 'results.html', {'results': error_message})



def fetch_league_events(path, date_params, league_abbr):
    """Fetch scoreboard events for a league."""
    url = f'https://sports-information.p.rapidapi.com/{path}'
    headers = {
        'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
        'X-RapidAPI-Host': 'sports-information.p.rapidapi.com'
    }
    resp = requests.get(url, headers=headers, params=date_params, timeout=5)
    resp.raise_for_status()
    events = resp.json().get('events', [])
    for e in events:
        e['league'] = league_abbr
    return events

def fetch_standings(path, year, group='league'):
    """Fetch and group standings entries by conference and division."""
    params = {'year': year}
    if group:
        params['group'] = group
    url = f'https://sports-information.p.rapidapi.com/{path}'
    headers = {
        'X-RapidAPI-Key': settings.RAPIDAPI_KEY,
        'X-RapidAPI-Host': 'sports-information.p.rapidapi.com'
    }
    resp = requests.get(url, headers=headers, params=params, timeout=5)
    resp.raise_for_status()
    standings = resp.json()['standings']

    return standings