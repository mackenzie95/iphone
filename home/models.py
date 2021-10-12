from django.db import models

# Create your models here.


class app(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname


class code(models.Model):
    verify = models.CharField(max_length=8)

    def __str__(self):
        return self.verify
