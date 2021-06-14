from django.http.response import Http404
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from recipe_app.models import Author, Recipe

from recipe_app.forms import AddAuthorForm, AddRecipeForm, LoginForm

# Link used for admin only Authentication
# https://stackoverflow.com/questions/49767843/django-user-permissions

# Create your views here.


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def recipe_detail(request, recipe_id: int):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.user.id == recipe.author.id
    return render(request, 'recipe_detail.html', {'recipe': recipe})

    if this_guy.is_authenticated:
        if this_tweeter in this_guy.followers.all():
            follow_flag = True


def author_detail(request, author_id: int):
    my_author = Author.objects.get(id=author_id)
    author_recipes = Recipe.objects.filter(author=my_author)
    return render(request, 'author_detail.html', {'author': my_author, 'recipes': author_recipes})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_recipe = Recipe.objects.create(
                title=data['title'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddRecipeForm()
    return render(request, 'generic_form.html', {'form': form})


@staff_member_required
def add_author(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = AddAuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                myuser = User.objects.create_user(
                    username=data['username'], password=data['password'])
                Author.objects.create(
                    name=data['name'], bio=data['bio'], user=myuser)
                return HttpResponseRedirect(reverse('homepage'))

        form = AddAuthorForm()
        return render(request, 'generic_form.html', {'form': form})
    else:
        raise Http404


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
