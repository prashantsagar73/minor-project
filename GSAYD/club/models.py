from django.db import models

# Create your models here.
class Club(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=210)
    author = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.CharField(max_length=130,default="")
    timestamp = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to='media/images/club',default="")


    def __str__(self):
        return self.title + 'by' + self.author