from django.shortcuts import render, redirect
from world_of_speed.cars.models import Car
from world_of_speed.profiles.models import Profile
from world_of_speed.cars.forms import CreateCarForm, EditCarForm, DeleteCarForm


def show_cars_catalogue(request):

    context = {
        'cars': Car.objects.all(),
        'total_cars': Car.objects.count(),
        'has_profile': Profile.objects.exists(),
    }
    
    return render(request, 'catalogue.html', context)


def create_car(request):
    profile = Profile.objects.first()
    form = CreateCarForm(request.POST or None)

    if request.method == 'POST' and form.is_valid() and profile:
        form.instance.owner = profile
        form.save()
        return redirect('cars_catalogue')

    context = {
        'form': form,
        'has_profile': Profile.objects.exists(),
    }

    return render(request, 'car-create.html', context)


def show_car_details(request, pk):
    car = Car.objects.get(id=pk)

    context = {
        'car': car,
        'has_profile': Profile.objects.exists(),
    }

    return render(request, 'car-details.html', context)


def edit_car_details(request, pk):
    car = Car.objects.get(id=pk)
    form = EditCarForm(request.POST or None, instance=car)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('cars_catalogue')

    context = {
        'car': car,
        'form': form,
        'has_profile': Profile.objects.exists(),
    }
    
    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.get(id=pk)
    form = DeleteCarForm(request.POST or None, instance=car)
    
    if request.method == 'POST':
        car.delete()
        return redirect('cars_catalogue')

    context = {
        'car': car,
        'form': form,
        'has_profile': Profile.objects.exists(),
    }
    
    return render(request, 'car-delete.html', context)
