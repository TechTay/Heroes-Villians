from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperTypeSerializer
from . models import SuperType

@api_view(['GET', 'POST'])
def super_types_list(request):

    if request.method == 'GET':

        
        super_type_name = request.query_params.get('super_type')
        queryset = SuperType.objects.all()
        custom_response_dictionary = {'Heroes' = [id=1], 'Villian' = [id=2]}

        for supertype in super_type_name:
            Heroes = SuperType.objects.filter(type=type)
            super_type_serializer = SuperTypeSerializer(Heroes, many=True)

            custom_response_dictionary[SuperType.type] = {
                'Heroes': SuperType.Heroes,
                'Villians': super_type_serializer.data
            }

        return Response(custom_response_dictionary)

        
    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def Super_Type_detail(request, pk):
        super_types = get_object_or_404(super_types, pk=pk)
        if request.method == 'GET':
            serializer = SuperTypeSerializer(SuperType);
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = SuperTypeSerializer(SuperType, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'DELETE':
            SuperType.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)