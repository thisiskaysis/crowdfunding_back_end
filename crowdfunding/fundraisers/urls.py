from django.urls import path
from . import views

urlpatterns = [
    # Campaign endpoints
    path('', views.CampaignList.as_view(), name='campaign_list'), # List all campaigns
    path('<int:campaign_id>/', views.CampaignDetail.as_view(), name='campaign_detail'), # Campaign details

    # Donation endpoints
    path('', views.DonationList.as_view(), name='donation_list'), #List all donations
    path('<int:donation_id>/', views.DonationDetail.as_view(), name='donation_detail'), # Donation details
]