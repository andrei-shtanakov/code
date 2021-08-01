from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Planet
from .models import Character
from .models import DataUpdate
from .serializers import DataUpdateSerializer
from .serializers import PlanetSerializer
from .serializers import CharacterSerializer
from django.template import loader
from docs.war import get_planets
from docs.war import get_people
from docs.war import update_db
import docs.war as w
from docs.war import del_all_people
from docs.war import del_all_planets

from django.shortcuts import get_object_or_404
from rest_framework import viewsets


last_form_action = ""


class PlanetViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Planet.objects.all()
        serializer = PlanetSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Planet.objects.all()
        planet = get_object_or_404(queryset, pk=pk)
        serializer = PlanetSerializer(planet)
        return Response(serializer.data)


class CharacterViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Character.objects.all()
        serializer = CharacterSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Character.objects.all()
        people = get_object_or_404(queryset, pk=pk)
        serializer = CharacterSerializer(people)
        return Response(serializer.data)

class PlanetPeopleViewSet(viewsets.ViewSet):
    def list(self, request, pk=None):
        queryset = Character.objects.all().filter(homeworld_id=pk)
        serializer = CharacterSerializer(queryset, many=True)
        return Response(serializer.data)


class DataUpdateViewSet(viewsets.ViewSet):
    def list(self, request, pk=None):

        update_db()
        print("test module")
        queryset = DataUpdate.objects.all()
        serializer = DataUpdateSerializer(queryset, many=True)
        return Response(serializer.data)




def management(request):
    global last_form_action
    a = request.GET.get('action', '')
    l = last_form_action
    context = {
        'action': a,
        'last_action': last_form_action,
    }
 
    if request.GET.get('action', '') == "del_planets":
        print("Action: {}".format(a))
        del_all_planets()
        last_form_action = "del_planets"
    elif request.GET.get('action', '') == "del_people":
        print("Action: {}".format(a))
        del_all_people()
        last_form_action = "del_people"

    elif request.GET.get('action', '') == "add_planets":
        print("Action: {}".format(a))
        get_planets()
        last_form_action = "add_planets"

    elif request.GET.get('action', '') == "add_people":
        print("Action: {}".format(a))
        get_people()
        last_form_action = "dadd_peopl"
    else:
        print("None")
        last_form_action = "none"


    return render(request, 'docs/management.html', context)
