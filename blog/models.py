from django.db import models

class Post(models.Model):
  title=models.CharField(max_length=20,blank=True,null=True)
  Desc=models.CharField(max_length=20)

class Products_Packet_Mapping(models.Model):
    product_id = models.CharField(max_length=20, null=False, blank=True)
    packet_product_id = models.CharField(max_length=20, null=False, blank=True)
    quantity_ratio = models.IntegerField(null=True)
    app_user_id = models.CharField(max_length=20, null=False)
    app_data_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_id
