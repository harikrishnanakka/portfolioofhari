from django.db import models

# Create your models here.

class Contact(models.Model):
    company_name = models.CharField(max_length=255)
    recruiter_name = models.CharField(max_length=255)
    description = models.TextField()
    recruiter_email = models.EmailField()

    def __str__(self):
        return self.company_name