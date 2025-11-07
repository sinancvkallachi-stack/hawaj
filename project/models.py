from django.db import models

# Create your models here.
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    image = models.TextField()
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