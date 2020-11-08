from django.db import models

# Create your models here.

class Pdf(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=110)
    head = models.CharField(max_length=110)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    pdfile = models.ImageField(upload_to='media/pdfs',default="")

    def __str__(self):
        return 'Message from ' + self
    #  this is for describing name and email in admin section(