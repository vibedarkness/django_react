from dataclasses import fields
from xml.parsers.expat import model
from rest_framework import serializers
from .models import Livre,Categorie

class CategorieSerializer(serializers.ModelSerializer):

    class Meta:
       model=Categorie
       fields=('nom','description')

       
class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields=('titre','auteur','date_publication','langue','nombredepage','pays','description','fichier')



