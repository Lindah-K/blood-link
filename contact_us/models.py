from django.db import models
from ckeditor.fields import RichTextField

class ContactDetails(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    display_contact_info = RichTextField(blank=True, null=True)
    logo_image = models.ImageField(upload_to='contact/', blank=True, null=True)

    def __str__(self):
        return self.title
