from django.db import models

# Create your models here.

class Urlcode(models.Model):
    code=models.CharField(max_length=255)
    url=models.CharField(max_length=255)
    create_date=models.CharField(max_length=255)

class Clientdetail(models.Model):
    code=models.CharField(max_length=255)
    #code = models.ForeignKey(Urlcode, on_delete=models.CASCADE)
    ip=models.CharField(max_length=255)
    browser=models.CharField(max_length=255)
    os=models.CharField(max_length=255)
    date=models.CharField(max_length=255)
    time=models.CharField(max_length=255)
    country=models.CharField(max_length=255)

    def __str__(self):
        return self.code