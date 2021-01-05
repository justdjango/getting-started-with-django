from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str)

    def handle(self, *args, **options):
        print(options['first_name'])