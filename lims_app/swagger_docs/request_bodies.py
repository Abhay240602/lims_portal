from drf_yasg import openapi

reader_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'reference_id': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='Reference ID of the reader'
        ),
        'reader_name': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Name of the reader'
        ),
        'reader_contact': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Contact information of the reader'
        ),
        'reader_address': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Address of the reader'
        ),
        'books': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Items(type=openapi.TYPE_INTEGER), 
            description='List of book IDs associated with the reader'
        ),
    },
    required=['reference_id', 'reader_name', 'reader_contact', 'reader_address']  
)