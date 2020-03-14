from django.db import models


class ContactUs(models.Model):
    name  = models.CharField(max_length=255)
    email  = models.EmailField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('date',)


    def __str__(self):
        return self.name


class ContactTo(models.Model):
    info  = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.info



