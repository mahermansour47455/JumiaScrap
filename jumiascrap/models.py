from django.db import models

# Create your models here.
class smartphoness(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    image_path=models.CharField(max_length=100)
    
    class Meta:
        db_table = 'smartphoness'
    

    

