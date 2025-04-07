from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
#from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .execute_sql import execute_sql_query
from .SQL_query_generation import generate_sql_query, generate_users_results, clean_sql_query, clean_python_table
from .forms import *
from .models import *
import openai

# class SignUpView(CreateView):
#     template_name = 'sign_up.html'
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('sign-in')

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']



def about(request):
    return render(request, 'about.html')

def autocomplete(request):
    return render(request, 'autocomplete.html')

def home(request):
    return render(request, 'home.html')
    

def mlb(request):
    return render(request, 'mlb.html')

def nba(request):
    return render(request, 'nba.html')

def nfl(request):
    return render(request, 'nfl.html')

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

def search_view(request):
    try:
        search_query = None 
        results = None 
        error_message = "Hello"
        if request.method == 'POST': 
                search_query = request.POST.get('search_query') 
                print(f"User search: {search_query}") 

                if search_query: 
                    sql_query = generate_sql_query(search_query) 
                    print(f"sql_query: {sql_query}") 
                    sql_query = clean_sql_query(sql_query)
                    print(f"sql_query_cleaned:{sql_query}")
                    sql_results = execute_sql_query(sql_query) 
                    print(f"sql Result: {sql_results}")
                    results, table_result = generate_users_results(search_query ,sql_results)
                    if results.startswith("Sorry"):
                        table_result = None
                    else:
                        table_result = clean_python_table(table_result)
                    print(f"Search Results: {results}") 
                    return render(request, 'home.html', {
                    'results': results,
                    'table_result': table_result
                    })
    except Exception as e:
        print(f"Error during search: {e}")
        error_message = "Sorry"
        return render(error_message, 'home.html')

            
        