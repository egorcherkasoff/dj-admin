from django.shortcuts import render


# Create your views here.
def not_found_view(request, exception):
    return render(request, "error.html")


def index(request):
    return render(request, "index.html")
