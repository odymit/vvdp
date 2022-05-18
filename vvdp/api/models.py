from django.db import models

# Create your models here.
'''
CREATE TABLE 'vul_list' (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cve_id` varchar(255) NOT NULL
)
'''
class VulList(models.Model):
    cve_id = models.CharField(max_length=255)
    cnnvd_id = models.CharField(max_length=255)
    description = models.TextField()
    vul_unit = models.TextField()
    affected_unit = models.TextField()
    attack_vector = models.CharField(max_length=8)
    attack_complexity = models.CharField(max_length=8)
    priviledge_required = models.CharField(max_length=8)
    user_interaction = models.CharField(max_length=8)
    confidential  = models.CharField(max_length=8)
    integration  = models.CharField(max_length=8)
    available  = models.CharField(max_length=8)
    privacy  = models.CharField(max_length=8)
    ecnomic  = models.CharField(max_length=8)
    functional  = models.CharField(max_length=8)
    human_safety = models.CharField(max_length=8)
    scope = models.CharField(max_length=8)
    cvss_score = models.FloatField()
    cvss_version = models.FloatField()
    vehicle_sec_score = models.FloatField(null=True)
    link = models.TextField()
    date = models.DateTimeField('date published')
