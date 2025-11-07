from django.db import models
import os

# Helper function for upload path
def upload_image(instance, filename):
    # This will save images inside MEDIA_ROOT/team_image/
    return os.path.join('team_image', filename)


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    priority = models.IntegerField()
    date = models.DateTimeField()
    time = models.DateTimeField()
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        db_table = 'team'
