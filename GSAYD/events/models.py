from django.db import models

# Create your models here.
class Events(models.Model):
    post_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=210)
    author = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.CharField(max_length=130,default="")
    timestamp = models.DateTimeField(blank=True)
    thumbnail = models.ImageField(upload_to='images/events',default="")

    def __str__(self):
        return self.event_name  + 'by' + self. author