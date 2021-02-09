from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=10)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name_plural = 'URL List'