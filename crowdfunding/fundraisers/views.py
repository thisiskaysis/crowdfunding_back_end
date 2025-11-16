from rest_framework import generics
from .models import Campaign, Donation
from .serializers import CampaignSerializer, DonationSerializer

def campaign_list(request):
    campaigns = Campaign.objects.all().values('id', 'title', 'description', 'goal_amount')
    return JsonResponse(list(campaigns), safe=False)

def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    data = {
        'id': campaign.id,
        'title': campaign.title,
        'description': campaign.description,
        'child': campaign.child.name,
        'goal_amount': str(campaign.goal_amount),
        'amount_raised': str(campaign.amount_raised),
        'deadline': campaign.deadline.isoformat(),
    }
    return JsonResponse(data)