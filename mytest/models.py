from django.db import models

# Create your models here.
class PollingUnit(models.Model):
    name = models.CharField(max_length=100)
    APC = models.IntegerField()
    PDP = models.IntegerField()
    LP = models.IntegerField()
    others = models.IntegerField()

    def total_votes(self):
        return self.APC + self.PDP + self.LP + self.others
