from django.core.management.base import BaseCommand
from drf_yasg.generators import OpenAPISchemaGenerator
import json

class Command(BaseCommand):
    help = 'Generate OpenAPI schema as JSON or YAML.'

    def handle(self, *args, **kwargs):
        schema_generator = OpenAPISchemaGenerator()
        schema = schema_generator.get_schema(request=None, public=True)

        with open('openapi_schema.json', 'w') as file:
            json.dump(schema, file, indent=2)

        import yaml
        with open('openapi_schema.yaml', 'w') as file:
            yaml.dump(schema, file, default_flow_style=False)

        self.stdout.write(self.style.SUCCESS('Successfully generated OpenAPI schema!'))
