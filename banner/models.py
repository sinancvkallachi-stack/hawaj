from django.db import models

# Create your models here.
class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    image = models.TextField()
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
        managed = False
        db_table = 'banner'
        
        
        
        # banner/models.py