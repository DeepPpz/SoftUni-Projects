from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from my_music_app.albums.models import Album


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)
        
        widgets = {
            'album_name': forms.TextInput(
                attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(
                attrs={'placeholder': 'Artist'}),
            'description': forms.TextInput(attrs={
                'placeholder': 'Description'}),
            'image_url': forms.URLInput(
                attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(
                attrs={'placeholder': 'Price'}),
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)


class DeleteAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
