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
