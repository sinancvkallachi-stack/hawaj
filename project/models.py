from django.db import models
import os
# Create your models here.
def upload_image(instance, filename):
    # This will save images inside MEDIA_ROOT/team_image/
    return os.path.join('team_image', filename)

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    heading = models.CharField(max_length=255)
    description = models.TextField()
    youtubelink = models.CharField(max_length=255, null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    condition = models.IntegerField()
    feature = models.IntegerField()
    date = models.DateTimeField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project'