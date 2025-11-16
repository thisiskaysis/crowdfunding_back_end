from django.urls import path
from . import views

urlpatterns = [
    path('', views.campaign_list, name='campaign_list'), # List all campaigns
    path('<int:campaign_id>/', views.campaign_detail, name='campaign_detail'), # Campaign details
]