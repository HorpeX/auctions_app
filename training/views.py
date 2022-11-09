from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, template_name='training/index.html')


def next_view(request):
    return render(request, template_name='training/next_view.html')