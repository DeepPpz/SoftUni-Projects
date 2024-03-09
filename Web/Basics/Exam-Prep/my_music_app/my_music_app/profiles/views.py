from django.shortcuts import render, redirect
from my_music_app.profiles.models import Profile
from my_music_app.albums.models import Album
from django.db.models import Sum


def show_profile_details(request):
    profile = Profile.objects.first()
    num_albums = Album.objects.filter(owner=profile).aggregate(total_price=Sum('price'))['total_price']
    
    context = {
        'profile': profile,
        'num_albums': num_albums,
        'has_profile': Profile.objects.exists()
    }
    
    return render(request, 'profiles/profile-details.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    
    if request.method == 'POST':
        profile.delete()
        return redirect('homepage')
    
    context = {
        'profile': profile,
        'has_profile': Profile.objects.exists()
    }
    
    return render(request, 'profiles/profile-delete.html', context)
