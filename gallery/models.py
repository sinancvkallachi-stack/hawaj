from django.db import models

# Create your models here.
class Gallery(models.Model):
    gallery_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    image = models.TextField()
    title = models.CharField(max_length=255)
    priority = models.IntegerField()
    condition = models.CharField(max_length=20)
    date = models.DateTimeField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gallery'
        
        
def __str__(self):
    return self.title