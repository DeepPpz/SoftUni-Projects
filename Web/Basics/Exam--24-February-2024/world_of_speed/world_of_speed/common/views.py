from django.shortcuts import render
from world_of_speed.profiles.models import Profile


def show_index_page(request):
    has_profile = Profile.objects.exists()

    context = {
        'has_profile': has_profile,
        # 'has_profile': False,
        }

    return render(request, 'index.html', context)
