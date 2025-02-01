from django.db import models

# Create your models here.
class Cve(models.Model):
    cve_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=300)
    cvss_v3_base_score = models.FloatField()

    def __str__(self):
        return self.cve_id