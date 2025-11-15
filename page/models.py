from django.db import models
import os
# Create your models here.
def upload_image(instance, filename):
    # This will save images inside MEDIA_ROOT/team_image/
    return os.path.join('page_image', filename)

class Page(models.Model):
    page_id = models.AutoField(primary_key=True)
    meta_title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    meta_description = models.TextField()
    title = models.CharField(max_length=255)
    page_name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    heading = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    date = models.DateTimeField()
    time = models.DateTimeField()

    class Meta:
        db_table = 'page'
        
    def __str__(self):
        return self.heading