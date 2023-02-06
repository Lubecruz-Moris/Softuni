from django.shortcuts import render, redirect

from gamesplay_app.web.forms import ProfileCreationForm, GameCreationForm, GameEditForm, GameDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from gamesplay_app.web.models import Profile, Game


# Create your views here.
#
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
        'profile_nav': profile_nav
    }
    return render(request, 'core/home-page.html', context)


def dashboard(request):
    context = {
        'games': Game.objects.all(),
        'profile_nav': True
    }

    return render(request, 'core/dashboard.html', context)


def games_rating():
    games = Game.objects.all()
    if games:
        return sum([game.rating for game in games]) / len(games)
    return None


def profile_details(request):
    profile = get_profile()
    games_rating()
    games_count = Game.objects.count()
    context = {
        'profile': profile,
        'games_count': games_count,
        'games_rating': games_rating,
        'profile_nav': True,
    }
    return render(request, 'profile/details-profile.html', context)


def profile_create(request):
    profile = get_profile()
    profile_nav = get_profile_nav(profile)
    if request.method == 'GET':
        form = ProfileCreationForm()
    else:
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile_nav': profile_nav
    }

    return render(request, 'profile/create-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
        'profile_nav': True

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
        'profile_nav': True

    }
    return render(request, 'profile/delete-profile.html', context)


def game_details(request, pk):
    game = Game.objects.filter(pk=pk).get()
    context = {
        'game': game,
        'profile_nav': True,
    }
    return render(request, 'games/details-game.html', context)


def game_create(request):
    if request.method == 'GET':
        form = GameCreationForm()
    else:
        form = GameCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile_nav': True
    }
    return render(request, 'games/create-game.html', context)


def game_edit(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
        'profile_nav': True

    }
    return render(request, 'games/edit-game.html', context)


def game_delete(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'game': game,
        'profile_nav': True

    }
    return render(request, 'games/delete-game.html', context)
