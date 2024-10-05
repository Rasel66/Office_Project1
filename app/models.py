from django.db import models

# Create your models here.
class Styles(models.Model):
    style_no = models.CharField(max_length=200, unique=True)
    style_desc = models.CharField(max_length=400)
    mini_market = models.FileField(upload_to = "documents/", null=True, blank=True)
    techpack = models.FileField(upload_to = "documents/", null=True, blank=True)
    composition = models.FileField(upload_to = "documents/",null=True, blank=True)
    enquiry_date = models.DateTimeField(verbose_name='Enquirey Date', null=True, blank=True)
    fabric_name = models.CharField(max_length=200, null=True, blank=True)
    fabric_consumption = models.FloatField(max_length=200, null=True, blank=True)
    fabric_cost = models.FloatField(default=0, null=True, blank=True)
    accessories_name = models.CharField(max_length=300,null=True, blank=True)
    accessories_consumption = models.FloatField(default=0,null=True, blank=True)
    accessories_cost = models.FloatField(default=0, null=True, blank=True)
    wash_plant_name = models.CharField(max_length=200)
    wash_cost = models.FloatField(default=0,null=True, blank=True)

    def __str__(self):
        return self.fabric_name
    

class Requisition(models.Model):
    styles = models.ForeignKey(Styles,on_delete=models.CASCADE, default="---Select---")
