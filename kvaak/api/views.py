from .serializer import SpeciesSerializer
from .models import Species
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def species_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
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
    Retrieve, update or delete a code snippet.
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
