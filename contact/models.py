from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    email = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    date = models.DateTimeField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contact'