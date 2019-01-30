from django.db import models
from issues.models import IssueModel

# Create your models here.


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.full_name, self.date)
        
    
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(IssueModel, null=False, on_delete=models.CASCADE)

    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)
        