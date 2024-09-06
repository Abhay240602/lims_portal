from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Reader, Book
from .serializers import ReaderSerializer, BookSerializer, ExportSerializer, ImportSerializer
from .forms import UploadFileForm
import io
import zipfile
import json
import pickle

from .swagger_docs.swagger_schemas import (
    get_schema, post_schema, put_schema, patch_schema, delete_schema, reader_create_schema, combined_schema
)

from .swagger_docs.custom_schemas import (
    READER_LIST_CREATE_SCHEMA, 
    READER_DELETE_SCHEMA,
    READER_DETAIL_SCHEMA,
    READER_UPDATE_PUT_SCHEMA,
    READER_UPDATE_PATCH_SCHEMA,
    BOOK_LIST_CREATE_SCHEMA,
    BOOK_DELETE_SCHEMA,
    BOOK_DETAIL_SCHEMA,
    BOOK_UPDATE_PUT_SCHEMA,
    BOOK_UPDATE_PATCH_SCHEMA,
    GET_SCHEMA,
    POST_SCHEMA,
    DELETE_SCHEMA,
    PUT_SCHEMA,
    PATCH_SCHEMA
)

class ReaderListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve list of readers or create a new reader.
    
    - GET: Retrieve a list of all readers.
    - POST: Create a new reader. Requires authentication.
    """
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    
    @get_schema
    def get(self, request, *args, **kwargs):
        """
        Retrieve a list of all readers.
        """
        return super().get(request, *args, **kwargs)

    @reader_create_schema
    def post(self, request, *args, **kwargs):
        """
        Create a new reader instance.
        
        This endpoint requires authentication. The data for the new reader should be provided in the request body.
        
        Returns:
            Response: JSON response containing the created reader's details.
        """
        return super().post(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        """
        Custom method called after validating the data to create a new reader.
        
        Args:
            serializer (ReaderSerializer): Serializer instance containing validated data for a new reader.
        """
        print(serializer.validated_data.get('reader_name'))
        serializer.save()

class ReaderDestroyAPIView(generics.DestroyAPIView):
    """
    API view to delete a reader by their ID.
    
    - DELETE: Deletes a specific reader instance.
    """
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    lookup_field = 'pk'
   
    @delete_schema 
    def delete(self, request, *args, **kwargs):
        """
        Deletes a reader instance.
        """
        return super().delete(request, *args, **kwargs)
    
    def perform_destroy(self, instance):
        """
        Custom method to handle additional logic before destroying the reader instance.
        
        Args:
            instance (Reader): The reader instance to delete.
        """
        super().perform_destroy(instance)

class ReaderDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve a single reader by their ID.
    
    - GET: Retrieves the details of a specific reader.
    """
    @get_schema
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

class ReaderUpdateAPIView(generics.UpdateAPIView):
    """
    API view to update a reader's information.
    
    - PUT: Updates all fields of a specific reader.
    - PATCH: Partially updates some fields of a specific reader.
    """
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    lookup_field = 'pk'
    
    @put_schema
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @patch_schema
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        """
        Custom method called after validating the data to update a reader.
        
        Args:
            serializer (ReaderSerializer): Serializer instance containing validated data for updating the reader.
        """
        serializer.save()

class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve list of books or create a new book.
    
    - GET: Retrieve a list of all books.
    - POST: Create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    @get_schema 
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @reader_create_schema  
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        """
        Custom method called after validating the data to create a new book.
        
        Args:
            serializer (BookSerializer): Serializer instance containing validated data for a new book.
        """
        print(serializer.validated_data.get('name'))
        serializer.save()

class BookDestroyAPIView(generics.DestroyAPIView):
    """
    API view to delete a book by its ID.
    
    - DELETE: Deletes a specific book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    
    @delete_schema 
    def delete(self, request, *args, **kwargs):
        """
        Deletes a reader instance.
        """
        return super().delete(request, *args, **kwargs)
    
    def perform_destroy(self, instance):
        """
        Custom method to handle additional logic before destroying the book instance.
        
        Args:
            instance (Book): The book instance to delete.
        """
        super().perform_destroy(instance)

class BookDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve a single book by its ID.
    
    - GET: Retrieves the details of a specific book.
    """
    @get_schema
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateAPIView(generics.UpdateAPIView):
    """
    API view to update a book's information.
    
    - PUT: Updates all fields of a specific book.
    - PATCH: Partially updates some fields of a specific book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    
    @put_schema
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @patch_schema
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        """
        Custom method called after validating the data to update a book.
        
        Args:
            serializer (BookSerializer): Serializer instance containing validated data for updating the book.
        """
        serializer.save()
