from django.shortcuts import render
from .models import Person, Place

# Create your views here.
def homepage(request):
  """ Home page """
  persons = Person.objects.all()
  places = Place.objects.all()

  ctx = {
    "persons": persons,
    "places": places
  }
  return render(request, 'homepage.html', context = ctx)