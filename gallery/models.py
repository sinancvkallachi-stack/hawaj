from django.db import models
import os
# Create your models here.
def upload_image(instance, filename):
    # This will save images inside MEDIA_ROOT/team_image/
    return os.path.join('gallery_image', filename)

class Gallery(models.Model):
    gallery_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    title = models.CharField(max_length=255)
    priority = models.IntegerField()
    condition = models.CharField(max_length=20)
    date = models.DateTimeField()
    time = models.DateTimeField()

    class Meta:
        db_table = 'gallery'
        
        
def __str__(self):
    return self.title