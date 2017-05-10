from django.db import models
from django.utils import timezone

class Candidate(models.Model):
    first_name = models.CharField(max_length = 30, blank=False)
    last_name  = models.CharField(max_length = 30, blank=False)
    school     = models.CharField(max_length = 50, blank=False)
    year       = models.DateField()
    text       = models.TextField(blank=False)
    impact     = models.TextField(blank=False)
    github     = models.URLField()
    email      = models.EmailField(max_length=100)
    SPONSORSHIP = (
        ('50','50%'),
        ('75','75%'),
        ('100','100%'),
    )

    def publish(self):
        self.save()
    def __str__(self):
        return self.email


# Create your models here.
