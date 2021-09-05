from django.db import models

class Person(models.Model):
GENDERS = (
      ('M', 'Male'),
      ('F', 'Female'),
      ('N', 'Nothing')
  )
  """ Campo de caracteres """  
  name = models.CharField(max_length = 100, null = False, blank = False)
  """ Campo para gerar escolhas """
  gender = models.CharField(max_length=1, choices = GENDERS, blank = False, null = False)
  """ Campo de caracteres """
  location = models.CharField()
  email = models.CharField()
  telephone = models.CharField()
  address = models.CharField()

#%%
class Place(models.Model):
    CLASSE = (
            ('B', 'Baixo'),
            ('M', 'Medio'),
            ('A', 'Alto')
            )
    TIPO_LUGAR = (
            ('C', 'Comercial'),
            ('U', 'Urbano'),
            ('R', 'Rural')
            )
  person = models.ForeignKey("Person", on_delete = models.CASCADE, related_name = 'NPS lugar')
  address = models.CharField(max_length = 200, null = False, blank = False)
  """ Criar choices """
  noise_level = models.CharField(max_length = 1, choices = CLASSE, blank = False, null = False)
  """ Criar choices """
  place_type = models.CharField(max_length = 1, choices = TIPO_LUGAR, blank = False, null = False)
  """ Criar choices """
  region_type = models.CharField()
  
  #%%
  