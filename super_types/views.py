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
        print(super_type_name)

        queryset = SuperType.objects.all()

        if super_type_name:
            queryset = queryset.filter(super_type__name=super_type_name)

        
        serializer = SuperTypeSerializer(queryset, many=True)
        return Response(serializer.data)
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