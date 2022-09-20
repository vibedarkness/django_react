from dataclasses import fields
from xml.parsers.expat import model
from rest_framework import serializers
from .models import Livre,Categorie

class CategorieSerializer(serializers.ModelSerializer):

    class Meta:
       model=Categorie
       fields=('nom','description')


class LivreSerializer(serializers.ModelSerializer):
    # fichier=serializers.CharField(read_only=True)
    class Meta:
        model = Livre
        fields=('titre','auteur','date_publication','langue','nombredepage','pays','description','fichier')

    def create(self,validated_data):
        langue=validated_data.pop('langue')
        print(langue) 
        print(validated_data)
        return Livre.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.titre=validated_data.get('titre')
        return super().update(instance, validated_data)

