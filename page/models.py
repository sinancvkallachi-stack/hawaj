from django.db import models

# Create your models here.
class Page(models.Model):
    page_id = models.AutoField(primary_key=True)
    meta_title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    meta_description = models.TextField()
    title = models.CharField(max_length=255)
    page_name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    image = models.TextField()
    heading = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    date = models.DateTimeField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'page'
        
    def __str__(self):
        return self.heading