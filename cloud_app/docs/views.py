from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Document
from .models import Operator
from .models import Planet
from .models import Character
from .serializers import DocumentSerializer
from django.template import loader
from docs.war import get_planets
from docs.war import get_people
import docs.war as w
from docs.war import del_all_people
from docs.war import del_all_planets



last_form_action = ""

class DocumentView(APIView):
    def get(self, request):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response({"documents": serializer.data})

    def post(self, request):
        new_doc = request.data.get('article')
        # Create an article from the above data
        serializer = DocumentSerializer(data=new_doc)
        if serializer.is_valid(raise_exception=True):
            doc_saved = serializer.save()
        return Response({"success": "Document '{}' created successfully".format(doc_saved.title)})

class OperatorView(APIView):
    def get(self, request):
        operators = Operator.objects.all()
        return Response({"operarors": operators})


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
