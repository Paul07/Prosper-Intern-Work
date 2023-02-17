from django import forms
from django.forms import ModelForm
from .models import FaveSongsModel


# form for creating song entry

class SongEntry(ModelForm):
    class Meta:
        model = FaveSongsModel
        fields = "__all__"
