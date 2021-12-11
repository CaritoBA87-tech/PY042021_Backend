import graphene
from graphene_django import DjangoObjectType
from .models import *

class AccesorioType(DjangoObjectType):
    class Meta:
        model = Accesorio

class Query(graphene.ObjectType): 
    all_accessories = graphene.List(AccesorioType)

    def resolve_all_accessories(self, info, **kwargs):
        return Accesorio.objects.all()

schema = graphene.Schema(query=Query)

