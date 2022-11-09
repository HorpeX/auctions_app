from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name='main/index.html')


def next_view(request):
    return render(request, template_name='main/next_view.html')