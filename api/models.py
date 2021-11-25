from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utilityFunctionsGapi import populateGSheets


class PrioritySubmission (models.Model):
    folderId = models.CharField(max_length=20, null=False)
    folderPermalink = models.URLField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=200)
    startDate = models.DateTimeField(auto_now=False, null=True, blank=True)
    updatedDate = models.DateTimeField(auto_now=True)
    linksProvided = models.CharField(max_length=1000, null=True, blank=True)
    workImpact = models.CharField(max_length=20000, null=True, blank=True)
    statement = models.CharField(max_length=20000, null=True, blank=True)
    submitter = models.CharField(max_length=100, null=True, blank=True)
    possibleSolutions = models.CharField(
        max_length=20000, null=True, blank=True)
    solutionRequirements = models.CharField(
        max_length=2000, null=True, blank=True)
    solutionDeveloper = models.CharField(max_length=100, null=True, blank=True)
    inputContributor = models.CharField(max_length=100, null=True, blank=True)
    agreer = models.CharField(max_length=100, null=True, blank=True)
    decider = models.CharField(max_length=100, null=True, blank=True)
    implementor = models.CharField(max_length=100, null=True, blank=True)
    acceptor = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=PrioritySubmission)
def populate_google(sender, instance, created, **kwargs):
    if created:
        print('Entered post save function...')
        populateGSheets(instance.folderId)
