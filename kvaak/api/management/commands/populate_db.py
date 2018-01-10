from django.core.management.base import BaseCommand
from ...models import Sighting
from ...models import Species


class Command(BaseCommand):
    help = 'Populate database with dummy data. \
            Amount of Sightings given as argument. \
            Creates 6 Sightings if argument not given. \
             \n ex. python manage.py populate_db 15'

    species = {
        'mallard',
        'redhead',
        'gadwall',
        'canvasback',
        'lesser',
        'scaup'
        }
    dates = {
        '1990-12-23T23:33:00Z',
        '2015-01-05T17:20:59Z',
        '2016-09-11T18:15:15Z',
        '2017-04-30T07:00:30Z',
        '2018-01-16T11:00:42Z',
        '2000-03-17T16:59:59Z'
        }
    count = {1, 5, 22, 223, 1000, 44}

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
                                species=Species.objects.get(name="mallard"),
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
