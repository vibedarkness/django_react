from django.shortcuts import render

from rest_framework import mixins,generics

from .serializers import LivreSerializer

from .models import Livre

# Create your views here.

class LivreMixins(generics.GenericAPIView,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    lookup_field = 'pk'
    def perform_create(self, serializer):
        titre=serializer.validated_data.get('titre')
        description=serializer.validated_data.get('description') or None
        if description is None:
            description= titre
        serializer.save(description=description)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)