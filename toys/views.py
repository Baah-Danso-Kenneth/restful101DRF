from django.shortcuts import render
from toys.models import Toy
from rest_framework import status
from toys.serializers import ToySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True)
        return Response(toys_serializer.data)

    elif request.method == 'POST':
        toys_serializer = ToySerializer(data=toy_data)
        if toys_serializer.is_valid():
            toys_serializer.save()
            return Response(toys_serializer.data,
                                status=status.HTTP_201_CREATED)
        return Response(toys_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def toy_detail(request, pk):
    try:
        toy = Toy.objects.get(pk=pk)
    except Toy.DoesNotExist:
        return Response(status=status.HTTP_404_NoT_FOUND)

    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return Response(toy_serializer.data)

    elif request.method == 'PUT':
        toy_serializer = ToySerializer(toy, data=request.data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return Response(toy_serializer.data)
        return Response(toy_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)