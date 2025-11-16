from django.contrib import admin
from .models import Campaign, Donation

# Register your models here.
admin.site.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'child', 'goal_amount', 'amount_raised', 'deadline', 'owner', 'created_at')
    search_fields = ('title', 'child__name', 'owner__username')
    list_filter = ('deadline', 'created_at', 'owner')

admin.site.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'donor_name', 'amount', 'payment_confirmed', 'created_at')
    search_fields = ('donor_name', 'donor_email', 'campaign__title')
    list_filter = ('payment_status', 'created_at')
