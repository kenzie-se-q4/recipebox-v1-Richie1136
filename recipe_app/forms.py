from django import forms



class AddRecipeForm(forms.Form):
  title = forms.CharField(max_length=30)
  description = forms.CharField(widget=forms.Textarea)
  time_required = forms.CharField(max_length=40)
  instructions = forms.CharField(widget=forms.Textarea)
  author = forms.ModelChoiceField(queryset=Author.objects.all())



class AddAuthorForm(forms.Form):
  name = models.CharField(max_length=50)
  bio = models.forms.CharField(widget=forms.Textarea)