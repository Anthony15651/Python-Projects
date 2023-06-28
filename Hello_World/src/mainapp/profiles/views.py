from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

def admin_console(request):
    profiles = Profile.objects.all()
    return render(request, "profiles/users_page.html", {'profiles': profiles})
