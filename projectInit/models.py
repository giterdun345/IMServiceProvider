from django.db import models
from django.db.models import constraints
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .utilityFunctionsGapi import populateGSheets

class ProjectSubmission( models.Model):
    folderId = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=200)
    objectives = models.CharField(max_length=20000, null=True, blank=True)
    scope =  models.CharField(max_length=20000, null=True, blank=True)
    requirements =  models.CharField(max_length=20000, null=True, blank=True)
    lead = models.CharField(max_length=200, null=True, blank=True)
    outScope =  models.CharField(max_length=20000, null=True, blank=True)
    deliverables = models.CharField(max_length=1000, null=True, blank=True)
    assumptions =  models.CharField(max_length=20000, null=True, blank=True)
    constraints =  models.CharField(max_length=20000, null=True, blank=True)
    scheduledMilestones =  models.CharField(max_length=20000, null=True, blank=True)
    projectDates =  models.CharField(max_length=5000, null=True, blank=True)
    budget =  models.CharField(max_length=1000, null=True, blank=True)
    mandatedReporting =  models.CharField(max_length=1000, null=True, blank=True)
    Approval =  models.CharField(max_length=20000, null=True, blank=True)
    
    def __str__(self):
        return self.name
