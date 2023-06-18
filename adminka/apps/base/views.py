from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def not_found_view(request, exception):
    return render(request, "error.html")

@login_required(login_url="login")
def index(request):
    return render(request, "index.html")
