from django.shortcuts import render

from .models import sample
def index(request):

    return render(request,"index.html")


def contact(request):

    return render(request,"contact.html")