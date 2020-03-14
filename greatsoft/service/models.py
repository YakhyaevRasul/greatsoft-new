from django.db import models
import os
import uuid


def service_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    
    return os.path.join('', filename)


class Service(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to=service_image_path)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering  = ('created_at',)
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name
