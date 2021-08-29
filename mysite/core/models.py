from django.db import models

GENDERS = (
      ('M', 'Male'),
      ('F', 'Female'),
      ('N', 'Nothing')
  )
class Person(models.Model):
  """ Campo de caracteres """  
  name = models.CharField()
  """ Campo para gerar escolhas """
  gender = models.CharField(max_length=1, choices = GENDERS)
  """ Campo de caracteres """
  location = models.CharField()
  email = models.CharField()
  telephone = models.CharField()
  address = models.CharField()


class Place(models.Model):
  address = models.CharField()
  """ Criar choices """
  noise_level = models.CharField()
  """ Criar choices """
  place_type = models.CharField()
  """ Criar choices """
  region_type = models.CharField()