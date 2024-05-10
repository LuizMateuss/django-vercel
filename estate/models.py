from django.db import models
from django.utils import timezone
class ServiceContractingPlan(models.Model):
    name = models.CharField(max_length=10, unique=True)

class Estate(models.Model):
    class Meta:
        db_table = 'estate'
    servic_contracting_plan = models.ForeignKey(ServiceContractingPlan, on_delete=models.RESTRICT)
    name = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=timezone.now)

class PaymentHistory(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    payment_api_id = models.CharField(max_length=15)
    creation_date = models.DateTimeField(default=timezone.now)