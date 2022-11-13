from unicodedata import mirrored
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Contribution
from .serializers import ContributionSerializer
from rest_framework import status
from rest_framework.response import Response
from datetime import date, datetime, timedelta

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_all_contribution(request):
    if request.method == 'GET':
        contributions = Contribution.objects.all()
        serializer = ContributionSerializer(contributions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ContributionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def mark_shipment_products(request, products):
    contributions = Contribution.objects.filter(contribution_type=products)
    serializer = ContributionSerializer(contributions, many=True)
    current_time = datetime.now()
    for contribution in contributions:
        str_d1= current_time.replace(microsecond=0, second=0, minute=0, hour=0)
        str_d2= contribution.date_received.replace(microsecond=0, second=0, minute=0, hour=0)
        d1= datetime.strptime(str(str_d1), '%Y-%m-%d %H:%M:%S')
        d2= datetime.strptime(str(str_d2), '%Y-%m-%d %H:%M:%S')
        delta= d1-d2
        if delta.days >= 90:
            contribution.marked_for_shipment = True
            contribution.save()
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([AllowAny])
def mark_shipment_money(request, money):
    contributions = Contribution.objects.filter(contribution_type=money)
    serializer = ContributionSerializer(contributions, many=True)
    current_time = datetime.now()
    for contribution in contributions:
        str_d1= current_time.replace(microsecond=0, second=0, minute=0, hour=0)
        str_d2= contribution.date_received.replace(microsecond=0, second=0, minute=0, hour=0)
        d1= datetime.strptime(str(str_d1), '%Y-%m-%d %H:%M:%S')
        d2= datetime.strptime(str(str_d2), '%Y-%m-%d %H:%M:%S')
        delta= d1-d2
        if delta.days >= 90:
            contribution.marked_for_shipment = True 
            contribution.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def mark_shipment_services(request, services):
    contributions = Contribution.objects.filter(contribution_type=services)
    serializer = ContributionSerializer(contributions, many=True)
    current_time = datetime.now()
    for contribution in contributions:
        str_d1= current_time.replace(microsecond=0, second=0, minute=0, hour=0)
        str_d2= contribution.date_received.replace(microsecond=0, second=0, minute=0, hour=0)
        d1= datetime.strptime(str(str_d1), '%Y-%m-%d %H:%M:%S')
        d2= datetime.strptime(str(str_d2), '%Y-%m-%d %H:%M:%S')
        delta= d1-d2
        if delta.days >= 90:
            contribution.marked_for_shipment = True 
            contribution.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def mark_shipment_food(request, food):
    contributions = Contribution.objects.filter(contribution_type=food)
    serializer = ContributionSerializer(contributions, many=True)
    current_time = datetime.now()
    for contribution in contributions:
        str_d1= current_time.replace(microsecond=0, second=0, minute=0, hour=0)
        str_d2= contribution.date_received.replace(microsecond=0, second=0, minute=0, hour=0)
        d1= datetime.strptime(str(str_d1), '%Y-%m-%d %H:%M:%S')
        d2= datetime.strptime(str(str_d2), '%Y-%m-%d %H:%M:%S')
        delta= d1-d2
        if delta.days >= 30:
            contribution.marked_for_shipment = True 
            contribution.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

