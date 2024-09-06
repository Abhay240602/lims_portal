from rest_framework import serializers

from .models import Reader, Book
    
class ReaderSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), many=True)
    class Meta:
        model = Reader
        fields = [
            'reference_id',
            'reader_name',
            'reader_contact',
            'reader_address',
            'books'
        ]

class BookSerializer(serializers.ModelSerializer):
    readers = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all(), many=True)
    class Meta:
        model = Book
        fields = [
            'name',
            'isbn',
            'author',
            'category',
            'readers'
        ]
        
class ExportSerializer(serializers.Serializer):
    detail = serializers.CharField()

class ImportSerializer(serializers.Serializer):
    detail = serializers.CharField()