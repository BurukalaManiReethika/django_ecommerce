from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .forms import ProfileForm

from .models import Profile


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            Profile.objects.create(
                user=user
            )

            login(request, user)

            return redirect('home')

    else:
        form = RegisterForm()

    return render(
        request,
        'users/register.html',
        {'form': form}
    )


@login_required
def profile(request):

    profile_obj, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            instance=profile_obj
        )

        if form.is_valid():

            form.save()

            return redirect('profile')

    else:

        form = ProfileForm(
            instance=profile_obj
        )

    return render(
        request,
        'users/profile.html',
        {'form': form}
    )
