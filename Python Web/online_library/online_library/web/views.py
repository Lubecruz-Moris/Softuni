from django.shortcuts import render, redirect

from online_library.web.forms import ProfileCreationForm, BookCreationForm, BookEditForm, ProfileEditForm, \
    ProfileDeleteForm
from online_library.web.models import Profile, Book

# Create your views here.
'''
•	http://localhost:8000/ - home page
•	http://localhost:8000/add/ - add book page
•	http://localhost:8000/edit/:id - edit book page
•	http://localhost:8000/details/:id - book details page
•	http://localhost:8000/profile/ - profile page
•	http://localhost:8000/profile/edit/ - edit profile page
•	http://localhost:8000/profile/delete/ - delete profile page

'''


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
        'books': Book.objects.all(),
        'profile': profile

    }
    return render(request, 'core/home-with-profile.html', context)


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
        'hide_nav_links': True,
    }
    return render(request, 'core/home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()

    context = {
        'profile': profile,

    }

    return render(request, 'profile/profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
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
    return render(request, 'profile/edit-profile.html', context)


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
        'profile': profile,

    }
    return render(request, 'profile/delete-profile.html', context)


def book_add(request):
    profile = get_profile()
    if request.method == 'GET':
        form = BookCreationForm()
    else:
        form = BookCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'books/add-book.html', context)


def book_details(request, pk):
    profile = get_profile()
    book = Book.objects.filter(pk=pk).get()
    context = {
        'book': book,
        'profile': profile,
    }
    return render(request, 'books/book-details.html', context)


def book_edit(request, pk):
    profile = get_profile()
    book = Book.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'book': book,
        'profile': profile,

    }
    return render(request, 'books/edit-book.html', context)


def book_delete(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.delete()

    return redirect('index')
