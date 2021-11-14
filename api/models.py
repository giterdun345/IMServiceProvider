from django.db import models


class PrioritySubmission (models.Model):
    folderId = models.CharField(max_length=20, null=False)
    folderPermalink = models.URLField(max_length=100, null=True)
    title = models.CharField(max_length=200)
    startDate = models.DateField(auto_now=False, null=True)
    updatedDate = models.DateTimeField(auto_now=True)
    linksProvided = models.CharField(max_length=1000, null=True)
    workImpact = models.CharField(max_length=20000, null=True)
    statement = models.CharField(max_length=20000, null=True)
    submitter = models.CharField(max_length=100, null=True)
    possibleSolutions = models.CharField(max_length=20000, null=True)
    solutionRequirements = models.CharField(max_length=2000, null=True)
    solutionDeveloper = models.CharField(max_length=100, null=True)
    inputContributor = models.CharField(max_length=100, null=True)
    agreer = models.CharField(max_length=100, null=True)
    decider = models.CharField(max_length=100, null=True)
    implementor = models.CharField(max_length=100, null=True)
    acceptor = models.CharField(max_length=100, null=True)

    def __str__(self):
        return [self.title, self.updatedDate]
