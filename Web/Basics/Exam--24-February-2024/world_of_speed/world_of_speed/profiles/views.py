from django.shortcuts import render, redirect
from world_of_speed.profiles.models import Profile
from world_of_speed.cars.models import Car
from world_of_speed.profiles.forms import CreateProfileForm, EditProfileForm
from django.db.models import Sum


def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('cars_catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile-create.html', context)


def show_profile_details(request):
    profile = Profile.objects.first()
    total_price = Car.objects.filter(owner=profile).aggregate(total_price=Sum('price'))['total_price']

    context = {
        'profile': profile,
        'total_price': total_price,
        'has_profile': Profile.objects.exists(),
    }
    
    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(request.POST or None, instance=profile)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile_details')

    context = {
        'profile': profile,
        'form': form,
        'has_profile': Profile.objects.exists(),
    }
    
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    
    if request.method == 'POST':
        profile = Profile.objects.first()
        profile.delete()
        return redirect('index')

    context = {
        'has_profile': Profile.objects.exists(),
    }

    return render(request, 'profile-delete.html', context)
