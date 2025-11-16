from django.db import models
from django.conf import settings
from users.models import Child

class Campaign(models.Model):
    # A fundraising campaign for a specific child
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='campaigns')
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_raised = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='campaigns')

    def __str__(self):
        return f"{self.title} for {self.child.name}"

class Donation(models.Model):
    # A donation made to a specific campaign
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='donations')
    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('failed', 'Failed')],
        default='pending')

    def __str__(self):
        return f"Donation of {self.amount} to {self.campaign.title} by {self.donor.username}"