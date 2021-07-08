from django.db import models

# Create your models here.
class Operator(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Document(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    operator = models.ForeignKey('Operator', related_name='documents', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Planet(models.Model):
    name            = models.CharField(max_length=50)
    gravity         = models.CharField(max_length=99)
    climate         = models.CharField(max_length=99)
    rotation_period = models.CharField(max_length=99)
    orbital_period  = models.CharField(max_length=99)
    diameter        = models.CharField(max_length=10)
    terrain         = models.CharField(max_length=99)
    population      = models.CharField(max_length=50)
    planet_url       = models.CharField(default="", max_length=99)


    def __str__(self):
        return self.name


class Character(models.Model):
    name       = models.CharField(max_length=50)
    gender     = models.CharField(max_length=99)
    height     = models.CharField(max_length=10)
    mass       = models.CharField(max_length=10)
    hair_color = models.CharField(max_length=50)
    skin_color = models.CharField(max_length=50)
    eye_color  = models.CharField(max_length=50)
    birth_year = models.CharField(max_length=10)
    charact_url = models.CharField(default="", max_length=99)
    homeworld  = models.ForeignKey(Planet, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

