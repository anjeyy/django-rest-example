from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from rest_framework.views import APIView

from .models import Document
from .serializers import DocumentSerializer


# Create your views here.


class DocumentViews(APIView):

    def get(self, request: Request, id: int = None) -> Response:
        if id:
            found_document = Document.objects.get(id=id)
            serializer: DocumentSerializer = DocumentSerializer(found_document)
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        found_documents = Document.objects.all()
        serializer: DocumentSerializer = DocumentSerializer(found_documents, many=True)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def post(self, request: Request) -> Response:
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED)
            response['Location'] = 'http://localhost:8000/xxx'
        else:
            response = Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        return response

    def patch(self, request: Request, id=None) -> Response:
        found_document = Document.objects.get(id=id)
        serializer: DocumentSerializer = DocumentSerializer(found_document, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request: Request, id=None) -> Response:
        found_document: QuerySet = get_object_or_404(Document, id=id)
        found_document.delete()
        return Response({"status": "success", "data": "Document deleted"})
