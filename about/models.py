from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    logo_image = models.ImageField(upload_to='about_images', null=True, blank=True) 

    def __str__(self):
        return self.title
