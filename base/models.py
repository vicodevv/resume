from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    message = models.TextField(max_length=2500, null=True)

    def __str__(self):
        return self.first_name