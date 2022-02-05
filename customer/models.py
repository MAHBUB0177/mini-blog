from django.db import models

# Create your models here.
class Customer(models.Model):
  name=models.CharField(max_length=200)
  logo=models.ImageField()
  description=models.TextField()
  updated=models.DateField(auto_now=True)
  created=models.DateField(auto_now_add=True)

  def __str__(self):
      return str(self.name)