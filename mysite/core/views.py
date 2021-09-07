from django.shortcuts import render
from .models import Person, Place

# Create your views here.
def homepage(request):
  """ Home page """
  persons = Person.objects.prefetch_related('places').all()
  places = Place.objects.all()
  persons_list = []

  for person in persons:
    person.places_list = person.places.all()
    persons_list.append(person)
    

  ctx = {
    "persons": persons_list,
    "places": places
  }

  return render(request, 'homepage.html', context = ctx)