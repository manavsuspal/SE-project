from django.core.management.base import BaseCommand
import uuid
from django.utils.text import slugify
from playground.models import Event

class Command(BaseCommand):
    help = 'Creates slugs for MyModel objects'

    def handle(self, *args, **options):
        for obj in Event.objects.all():
            obj.slug = slugify(obj.name) + '-' + str(uuid.uuid4())
            obj.save()

        self.stdout.write(self.style.SUCCESS('Successfully created slugs'))

