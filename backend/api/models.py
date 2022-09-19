from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom=models.CharField(max_length=100)
    description=models.TextField()


class Livre(models.Model):
    titre=models.CharField(max_length=100)
    auteur=models.CharField(max_length=100)
    date_publication=models.DateField()
    langue=models.CharField(max_length=100)
    nombredepage=models.IntegerField()
    pays=models.CharField(max_length=100)
    description=models.TextField()
    fichier=models.FileField()


