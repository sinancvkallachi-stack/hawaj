from django.db import models

# Create your models here.
class Testimonial(models.Model):
    testimonial_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    testimonial = models.CharField(max_length=255)
    priority = models.IntegerField()
    condition = models.IntegerField()
    date = models.DateTimeField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'testimonial'