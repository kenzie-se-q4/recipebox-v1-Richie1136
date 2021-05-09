from django.shortcuts import render, HttpResponseRedirect, reverse

from recipe_app.models import Author, Recipe

from recipe_app.forms import AddAuthorForm, AddRecipeForm

# Create your views here.
def index(request):
  recipes = Recipe.objects.all()
  return render(request, 'index.html', {'recipes' : recipes})


def recipe_detail(request, recipe_id: int):
  recipe = Recipe.objects.get(id=recipe_id)
  return render(request, 'recipe_detail.html', {'recipe': recipe})


def author_detail(request, author_id: int):
  my_author = Author.objects.get(id=author_id)
  author_recipes = Recipe.objects.filter(author=my_author)
  return render(request, 'author_detail.html', {'author': my_author, 'recipes': author_recipes})

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
  return render(request, 'recipe_add.html', {'form' : form})

def add_author(request):
  if request.method == 'POST':
    form = AddAuthorForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      new_author = Author.objects.create(
        name=data['name'],
        bio=data['bio'],
      )
    return HttpResponseRedirect(reverse('homepage'))

  form = AddAuthorForm()
  return render(request, 'author_add.html', {'form' : form})
