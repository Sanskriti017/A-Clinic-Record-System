from django.db import models


# Create your models here.
class record(models.Model):
    name=models.CharField(max_length=55)
    email=models.EmailField()
    number=models.CharField(max_length=12)
    disease=models.CharField(max_length=55)
    condition=models.TextField()
    curr_prescribed=models.CharField(max_length=122)
    prev_prescribed=models.CharField(max_length=122)
    venue_image=models.ImageField(null=True,blank=True,upload_to="images/") 

    def __str__(self):
        return self.name
    