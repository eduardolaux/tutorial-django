from django.shortcuts import render
from .models import Person, Place
from .serializers import PersonSerializer

# Create your views here.
def homepage(request):
  """ Home page """
  persons = Person.objects.prefetch_related('places').all()
  persons = PersonSerializer(persons, many = True).data
  places = Place.objects.all()

  ctx = {
    "persons": persons,
    "places": places
  }

  return render(request, 'homepage.html', context = ctx)