from django.db import models
import os
# Create your models here.
def upload_image(instance, filename):
    # This will save images inside MEDIA_ROOT/team_image/
    return os.path.join('banner_image', filename)

class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    heading = models.CharField(max_length=45)
    category = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    # condition = models.IntegerField()
    # ...
    condition = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
        ],
        default='active'
    )
    def __str__(self):
        return self.heading
    date = models.DateTimeField()
    time = models.DateTimeField()

    class Meta:
        db_table = 'banner'
        
        
        
        # banner/models.py