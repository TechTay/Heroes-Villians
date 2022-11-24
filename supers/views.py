from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from . models import Supers
from . models import SuperType

@api_view(['GET', 'POST'])
def supers_list(request):

    if request.method == 'GET':

        
        super_type = request.query_params.get('type')
        sort_param = request.query_params.get('sort')


        queryset= Supers.objects.all()

        if super_type:
            queryset = queryset.filter(super_type__type=super_type)

        if sort_param:
            queryset = queryset.order_by(sort_param)
            
        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def Supers_detail(request, pk):
        
        super_types = get_object_or_404(Supers, pk=pk)
        if request.method == 'GET':

            

            serializer = SuperSerializer(super_types);
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = SuperSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'DELETE':
            Supers.objects.filter(id=7).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
