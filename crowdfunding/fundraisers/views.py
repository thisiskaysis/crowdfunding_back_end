from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Campaign, Donation
from .serializers import CampaignSerializer, DonationSerializer, CampaignDetailSerializer

# ------ Campaign Views ------

class CampaignList(APIView):
    # List all campaigns or create a new one
    def get(self, request, format=None):
        campaigns = Campaign.objects.all()
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CampaignDetail(APIView):
    # Retrieve, update or delete a campaign instance
    def get_object(self, pk):
        try:
            return Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        campaign = self.get_object(pk)
        serializer = CampaignDetailSerializer(campaign)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        campaign = self.get_object(pk)
        serializer = CampaignDetailSerializer(campaign, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        campaign = self.get_object(pk)
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# ------ Donation Views ------
class DonationList(APIView):
    # List all donations or create a new one
    def get(self, request, format=None):
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)