from django.shortcuts import render, redirect
from my_music_app.profiles.models import Profile
from my_music_app.albums.models import Album
from my_music_app.albums.forms import AddAlbumForm, EditAlbumForm, DeleteAlbumForm


def add_album(request):
    profile = Profile.objects.first()
    form = AddAlbumForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid() and profile:
        form.instance.owner = profile
        form.save()
        return redirect('homepage')
    
    context = {
        'form': form,
        'has_profile': Profile.objects.exists()
    }
    
    return render(request, 'albums/album-add.html', context)


def show_album_details(request, pk):
    album = Album.objects.get(id=pk)
    
    context = {
        'album': album,
        'has_profile': Profile.objects.exists()
    }
    
    return render(request, 'albums/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(id=pk)
    form = EditAlbumForm(request.POST or None, instance=album)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('homepage')
    
    context = {
        'album': album,
        'form': form,
        'has_profile': Profile.objects.exists()
    }
    
    return render(request, 'albums/album-edit.html', context)


def delete_album(request, pk):
    album = Album.objects.get(id=pk)
    form = DeleteAlbumForm(request.POST or None, instance=album)
    
    if request.method == 'POST':
        album.delete()
        return redirect('homepage')
    
    context = {
        'album': album,
        'form': form,
        'has_profile': Profile.objects.exists()
    }
    
    return render(request, 'albums/album-delete.html', context)
