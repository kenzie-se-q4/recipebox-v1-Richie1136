from django import forms

from recipe_app.models import Author




class AddRecipeForm(forms.Form):
  title = forms.CharField(max_length=30)
  description = forms.CharField(widget=forms.Textarea)
  time_required = forms.CharField(max_length=40)
  instructions = forms.CharField(widget=forms.Textarea)
  author = forms.ModelChoiceField(queryset=Author.objects.all())


class AddAuthorForm(forms.Form):
  name = forms.CharField(max_length=50)
  bio = forms.CharField(widget=forms.Textarea)
  username = forms.CharField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput)




class LoginForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput)
