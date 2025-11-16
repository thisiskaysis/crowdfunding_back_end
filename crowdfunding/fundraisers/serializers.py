from rest_framework import serializers
from .models import Campaign, Donation

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'

class CampaignDetailSerializer(serializers.ModelSerializer):
    donations = DonationSerializer(many=True, read_only=True) #nested donations
    class Meta:
        model = Campaign
        fields = '__all__'