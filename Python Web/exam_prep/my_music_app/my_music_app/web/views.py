from django.core import exceptions
from django.shortcuts import render, redirect

from my_music_app.web.forms import ProfileCreationForm, AlbumCreationForm, AlbumEditForm, AlbumDeleteForm, \
    ProfileDeleteForm
from my_music_app.web.models import Profile, Album


# Create your views here.


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return profile_add(request)

    context = {
        'albums': Album.objects.all(),
    }
    return render(request, 'core/home-with-profile.html', context)


def album_details(request, pk):
    album = Album.objects.filter(pk=pk).get()
    context = {
        'album': album
    }
    return render(request, 'albums/album-details.html', context)


def album_add(request):
    if request.method == 'GET':
        form = AlbumCreationForm()
    else:
        form = AlbumCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'albums/add-album.html', context)


def album_edit(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,

    }

    return render(request, 'albums/edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'album': album,

    }
    return render(request, 'albums/delete-album.html', context)


def profile_details(request):
    profile = get_profile()

    context = {
        'profile': profile,

    }
    return render(request, 'profile/profile-details.html', context)


def profile_add(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreationForm()
    else:
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,

    }
    return render(request, 'core/home-no-profile.html', context)


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
    return render(request, 'profile/profile-delete.html', context)
