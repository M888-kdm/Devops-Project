from django.db import models

class Utilisateur(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
