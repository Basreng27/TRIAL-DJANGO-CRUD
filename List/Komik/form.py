from django import forms
from .models import *

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
        labels = {
            'name': 'Nama Genre'  # Label untuk field 'name'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            if self.instance.name:
                self.fields['name'].initial = self.instance.name

class ComicForm(forms.ModelForm):
    genre_id = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        empty_label="--Pilih--",
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'background:black'})
    )

    class Meta:
        model = Comic
        fields = ['name', 'genre_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            if self.instance.name:
                self.fields['name'].initial = self.instance.name

            # if self.instance.genre_id:
            #     self.fields['genre_id'].initial = self.instance.genre_id