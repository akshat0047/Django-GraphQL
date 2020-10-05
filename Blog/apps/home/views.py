from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings


def IndexView(request):
    # return redirect(settings.HOME_URL)
    return render(request, "home/index.html")
