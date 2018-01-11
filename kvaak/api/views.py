from .serializer import SpeciesSerializer
from .serializer import SightingSerializer
from .models import Species
from .models import Sighting
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import BrowsableAPIRenderer
from .utils.renderer import CamelCaseJSONRenderer


@api_view(['GET', 'POST'])
def species_list(request, format=None):
    """
    List all species
    """
    if request.method == 'GET':
        species = Species.objects.all()
        serializer = SpeciesSerializer(species, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SpeciesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def species_detail(request, pk, format=None):
    """
    Retrieve, update or delete a species.
    """
    try:
        species = Species.objects.get(pk=pk)
    except Species.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Species(species, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        species.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@renderer_classes((CamelCaseJSONRenderer, BrowsableAPIRenderer,))
def sightings_list(request, format=None):
    """
    List all sightings
    """
    if request.method == 'GET':
        sightings = Sighting.objects.all()
        serializer = SightingSerializer(sightings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            request.data['id']
        except KeyError:
            request.data.update({'id': get_first_empty_id()})
        serializer = SightingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_first_empty_id():
    new_id = 1
    # new_id = Sighting.objects.count() + 1
    while 1:
        try:
            Sighting.objects.get(id__exact=new_id)
            new_id += 1
        except Sighting.DoesNotExist:
            return new_id


@api_view(['GET', 'PUT', 'DELETE'])
@renderer_classes((CamelCaseJSONRenderer, BrowsableAPIRenderer,))
def sighting_detail(request, pk, format=None):
    """
    Retrieve, update or delete a sightings.
    """
    try:
        sighting = Sighting.objects.get(pk=pk)
    except Sighting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SightingSerializer(sighting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Species(sighting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sighting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
