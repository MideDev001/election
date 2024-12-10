from django.db import models

# Create your models here.
class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    state_id = models.IntegerField()

class Ward(models.Model):
    ward_id = models.IntegerField(primary_key=True)
    ward_name = models.CharField(max_length=255)
    lga_id = models.IntegerField()

class LGA(models.Model):
    lga_id = models.IntegerField(primary_key=True)
    lga_name = models.CharField(max_length=255)
    state_id = models.IntegerField()

class AnnouncedPUResults(models.Model):
    polling_unit_uniqueid = models.IntegerField()
    party_abbreviation = models.CharField(max_length=5)
    party_score = models.IntegerField()

class AnnouncedLGAResults(models.Model):
    lga_id = models.IntegerField()
    party_abbreviation = models.CharField(max_length=5)
    party_score = models.IntegerField()