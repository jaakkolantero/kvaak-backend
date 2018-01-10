from django.core.management.base import BaseCommand
from ...models import Sighting
from ...models import Species
import random


class Command(BaseCommand):
    help = 'Populate database with dummy data. \
            Amount of Sightings given as argument. \
            Creates 6 Sightings if argument not given. \
             \n ex. python manage.py populate_db 15'

    species = [
        'mallard',
        'redhead',
        'gadwall',
        'canvasback',
        'lesser',
        'scaup'
        ]

    def _add_species(self, species):
        for bird in species:
            try:
                species = Species.objects.get(name=bird)
            except Species.DoesNotExist:
                species = Species(name=bird)
                species.save()

    def _create_sightings(self, count):
        # TODO: Create random data
        self._add_species(self.species)
        for i in range(count):
            sighting = Sighting(date_time='1990-12-23T23:33:00Z',
                                description='wow such bird',
                                species=Species.objects.get(name=self.species[random.randint(0, 5)]),
                                count=3
                                )
            self.stdout.write(self.style.SUCCESS('Successfully added sighting %s!' % sighting.species))
            sighting.save()

    def add_arguments(self, parser):
        # https://docs.python.org/3/library/argparse.html
        parser.add_argument('sightings', nargs='*', type=int, default=5)

    def handle(self, *args, **options):
        try:
            for sightings_count in options['sightings']:
                self._create_sightings(sightings_count)
        except TypeError:
            self._create_sightings(6)
