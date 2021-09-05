from django.shortcuts import render
from .models import Person

# Create your views here.
def homepage(request):
  """ Home page """
  persons = Person.objects.all()
  ctx = {
    "persons": persons
  }
  return render(request, 'homepage.html', context = ctx)