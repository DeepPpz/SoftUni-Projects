from django.shortcuts import render, redirect
from my_music_app.albums.models import Album
from my_music_app.profiles.models import Profile
from my_music_app.profiles.forms import CreateProfileForm


def show_homepage(request):
    profile = Profile.objects.first()

    if profile is None:
        form = CreateProfileForm(request.POST or None)

        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('homepage')

        context = {
            'form': form,
            'has_profile': Profile.objects.exists(),
        }

        return render(request, 'common/home-no-profile.html', context)
    
    else:
        context = {
            'albums': Album.objects.all(),
            'has_profile': Profile.objects.exists(),
        }

        return render(request, 'common/home-with-profile.html', context)
