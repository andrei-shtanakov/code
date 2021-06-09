from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Document
from .models import Operator
from .serializers import DocumentSerializer

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
