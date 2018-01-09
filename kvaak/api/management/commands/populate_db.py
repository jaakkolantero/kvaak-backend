from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from ...models import Sighting
from ...models import Species


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    species = {'mallard', 'redhead', 'gadwall', 'canvasback', 'lesser', 'scaup'}
    dates = {'1990-12-23T23:33:00Z', '2015-01-05T17:20:59Z', '2016-09-11T18:15:15Z', '2017-04-30T07:00:30Z', '2018-01-16T11:00:42Z', '2000-03-17T16:59:59Z'}
    count = {1, 5, 22 , 223, 1000, 44}

    def _create_sightings(self):
        for bird, date, count in zip(self.species, self.dates, self.count):
            try:
                species = Species.objects.get(name=bird)
            except Species.DoesNotExist:
                species = Species(name=bird)
                species.save()
            sighting = Sighting(date_time=date,
                                description='wow such bird',
                                species=Species.objects.get(name=bird),
                                count=count
                                )
            sighting.save()

    def _create_species(self):
        species = Species(name='tweeter')
        species.save()

    def handle(self, *args, **options):
        self._create_sightings()
