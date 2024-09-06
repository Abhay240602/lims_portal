from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from ..serializers import ReaderSerializer, BookSerializer
from functools import wraps
from .request_bodies import reader_request_body

def combined_schema(*schemas):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)
        
        combined_description = ""
        combined_request_body = None
        combined_responses = {}

        for schema in schemas:
            if hasattr(schema, 'operation_description'):
                combined_description += schema.operation_description + " "
            if hasattr(schema, 'request_body'):
                combined_request_body = schema.request_body
            if hasattr(schema, 'responses'):
                combined_responses.update(schema.responses)
            
        wrapped.schema = swagger_auto_schema(
            operation_description=combined_description.strip(),
            request_body=combined_request_body,
            responses=combined_responses
        )(wrapped)

        return wrapped
    return decorator

reader_create_schema = swagger_auto_schema(
    operation_description="Create a new reader with provided details.",
    request_body=reader_request_body, 
    responses={
        201: openapi.Response(
            description="Reader created successfully",  
            schema=openapi.Schema(  
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
            )
        ),
        400: openapi.Response(description="Bad Request")
    }
)

### GET Schema for all GET requests
get_schema = swagger_auto_schema(
    operation_description="Retrieve resource(s)",
    responses={200: openapi.Response(description="Successful Response")}
)

### POST Schema for all POST requests
post_schema = swagger_auto_schema(
    operation_description="Create a new resource",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        additionalProperties=True,  # Allows flexibility for any schema
        description="Request body for creating a resource"
    ),
    responses={201: openapi.Response(description="Resource created successfully")}
)

### PUT Schema for all PUT requests
put_schema = swagger_auto_schema(
    operation_description="Update a resource completely",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        additionalProperties=True,
        description="Request body for updating a resource"
    ),
    responses={200: openapi.Response(description="Resource updated successfully")}
)

### PATCH Schema for all PATCH requests
patch_schema = swagger_auto_schema(
    operation_description="Partially update a resource",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        additionalProperties=True,
        description="Request body for partially updating a resource"
    ),
    responses={200: openapi.Response(description="Resource updated successfully")}
)

### DELETE Schema for all DELETE requests
delete_schema = swagger_auto_schema(
    operation_description="Delete a resource",
    responses={204: openapi.Response(description="Resource deleted successfully")}
)