from django.db import models

class Url(models.Model):
    long_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length= 100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.long_url
