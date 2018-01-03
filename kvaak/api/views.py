from .serializer import SpeciesSerializer
from .models import Species
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def species_list(request):
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
