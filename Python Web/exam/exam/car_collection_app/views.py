from django.shortcuts import render, redirect

from exam.car_collection_app.forms import ProfileCreationForm, CarCreationForm, CarEditForm, CarDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from exam.car_collection_app.models import Profile, Car

# Create your views here.


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def get_profile_nav(profile):
    profile_nav = True
    if profile is None:
        profile_nav = False
    return profile_nav


def index(request):
    profile = get_profile()
    profile_nav = get_profile_nav(profile)

    context = {
        'profile': profile,
        'profile_nav': profile_nav,
    }
    return render(request, 'core/index.html', context)


def catalogue(request):
    cars_count = Car.objects.count()
    context = {
        'cars': Car.objects.all(),
        'cars_count': cars_count,
    }

    return render(request, 'core/catalogue.html', context)


def total_price():
    cars = Car.objects.all()
    if cars:

        return sum([car.price for car in cars])
    return None

def profile_details(request):
    profile = get_profile()
    total_price()
    context = {
        'profile': profile,
        'total_price': total_price,
    }
    return render(request, 'profiles/profile-details.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreationForm()
    else:
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-create.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
        'profile': profile,

    }
    return render(request, 'profiles/profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,

    }
    return render(request, 'profiles/profile-delete.html', context)


def car_create(request):
    if request.method == 'GET':
        form = CarCreationForm()
    else:
        form = CarCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'cars/car-create.html', context)


def car_details(request, pk):
    car = Car.objects.filter(pk=pk).get()

    context = {
        'car': car,
    }

    return render(request, 'cars/car-details.html', context)


def car_edit(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'cars/car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'cars/car-delete.html', context)
