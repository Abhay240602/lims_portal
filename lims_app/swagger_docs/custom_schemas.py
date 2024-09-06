from drf_spectacular.utils import OpenApiParameter, OpenApiTypes, extend_schema

# Common Parameters
AUTHORIZATION_HEADER = OpenApiParameter(
    name='Authorization',
    description='JWT authorization token',
    required=True,
    type=OpenApiTypes.STR,
    location=OpenApiParameter.HEADER
)

ORG_HEADER = OpenApiParameter(
    name='Org',
    description='Organization identifier',
    required=True,
    type=OpenApiTypes.STR,
    location=OpenApiParameter.HEADER
)

GET_SCHEMA = extend_schema(
    summary='Retrieve a resource or list of resources',
    parameters=[AUTHORIZATION_HEADER, ORG_HEADER],
    responses={
        200: OpenApiTypes.OBJECT  # Adjust response type as needed
    }
)

POST_SCHEMA = extend_schema(
    summary='Create a resource',
    parameters=[AUTHORIZATION_HEADER, ORG_HEADER],
    request=OpenApiTypes.OBJECT,  # Adjust request format as needed
    responses={
        201: OpenApiTypes.OBJECT,  # Adjust response type as needed
        400: OpenApiTypes.STR
    }
)

DELETE_SCHEMA = extend_schema(
    summary='Delete a resource by its ID',
    parameters=[AUTHORIZATION_HEADER, ORG_HEADER],
    responses={
        204: None,  # No content on successful delete
        404: OpenApiTypes.STR
    }
)

PUT_SCHEMA = extend_schema(
    summary='Update all fields of a resource',
    parameters=[AUTHORIZATION_HEADER, ORG_HEADER],
    request=OpenApiTypes.OBJECT,  # Adjust request format as needed
    responses={
        200: OpenApiTypes.OBJECT,  # Adjust response type as needed
        400: OpenApiTypes.STR
    }
)

PATCH_SCHEMA = extend_schema(
    summary='Partially update some fields of a resource',
    parameters=[AUTHORIZATION_HEADER, ORG_HEADER],
    request=OpenApiTypes.OBJECT,  # Adjust request format as needed
    responses={
        200: OpenApiTypes.OBJECT,  # Adjust response type as needed
        400: OpenApiTypes.STR
    }
)

# Reader Schemas
READER_LIST_CREATE_SCHEMA = extend_schema(
    parameters=[
        OpenApiParameter(
            name='reader_name',
            description='Name of the reader',
            required=True,
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY
        ),
    ]
)

READER_DELETE_SCHEMA = extend_schema(
    summary='Delete a reader by their ID'
)

READER_DETAIL_SCHEMA = extend_schema(
    summary='Retrieve a single reader by their ID'
)

READER_UPDATE_PUT_SCHEMA = extend_schema(
    summary='Update all fields of a specific reader',
    request=OpenApiTypes.OBJECT  # Adjust as needed for your specific request format
)

READER_UPDATE_PATCH_SCHEMA = extend_schema(
    summary='Partially update some fields of a specific reader',
    request=OpenApiTypes.OBJECT  # Adjust as needed for your specific request format
)

# Book Schemas
BOOK_LIST_CREATE_SCHEMA = extend_schema(
    summary='Retrieve or create a book'
)

BOOK_DELETE_SCHEMA = extend_schema(
    summary='Delete a book by its ID'
)

BOOK_DETAIL_SCHEMA = extend_schema(
    summary='Retrieve a single book by its ID'
)

BOOK_UPDATE_PUT_SCHEMA = extend_schema(
    summary='Update all fields of a specific book',
    request=OpenApiTypes.OBJECT  # Adjust as needed for your specific request format
)

BOOK_UPDATE_PATCH_SCHEMA = extend_schema(
    summary='Partially update some fields of a specific book',
    request=OpenApiTypes.OBJECT  # Adjust as needed for your specific request format
)
