# import re
# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PrioritySubmission
from .serializers import PrioritySubmissionSerializer
from datetime import datetime, timedelta
from django.utils import timezone
import time
import requests
import environ

env = environ.Env()
environ.Env.read_env()


@api_view(['POST'])
def wrike_incoming(request):
    # enter into array from wrike webhook
    # incoming = request.data[0]
    # print(incoming)
    print(request)
    return Response('Recieved', status=status.HTTP_202_ACCEPTED)
    # wrikeData = incoming
    # # relevant info to/from webhook
    # folderId = incoming["folderId"]
    # eventType = incoming["eventType"]
    # auth_token = env("WRIKE_AUTH")

    # # params and headers used in Wrike GET for folder data
    # getFolderUrl = f"https://www.wrike.com/api/v4/folders/{folderId}"
    # headers = {
    #     "method": "GET",
    #     "Content-Type": "application/json",
    #     "User-Agent": "Mozilla/5.0",
    #     "Authorization": "Bearer " + auth_token
    # }

    # # all eventTypes are sent from Wrike, continues the fuction if the eventType is correct
    # if eventType == 'FolderCreated' or eventType == 'FolderUpdated':
    #     wrikeData = requests.get(getFolderUrl, headers=headers)
    #     wrikeData = wrikeData.json().get('data')[0]
    #     # extract customFields by id
    # statement = 'IEABAVGPJUACJTNA'
    # workImpact = 'IEABAVGPJUACJTN7'
    # solutionRequirements = 'IEABAVGPJUACJTOA'
    # possibleSolutions = 'IEABAVGPJUACJTOB'
    # link = 'IEABAVGPJUACJTO4'
    # submitter = 'IEABAVGPJUACJTOC'
    # ADD USER CUSTOMDATA FIELDS for additional ids

    # if True:

    #     def findCustomDataField(id):
    #         """Searches custom field by ID to return its value"""
    #         return next((item["value"] for item in wrikeData["customFields"] if item["id"] == id), None)

    #     extractedWrikeData = {
    #         "folderId": wrikeData["id"],
    #         "folderPermalink": wrikeData["permalink"],
    #         "title": wrikeData["title"],
    #         "startDate": wrikeData["project"]["startDate"],
    #         "updatedDate": wrikeData["updatedDate"],
    #         "linksProvided": findCustomDataField("IEABAVGPJUACJTO4"),
    #         "workImpact": findCustomDataField("IEABAVGPJUACJTN7"),
    #         "statement": findCustomDataField("IEABAVGPJUACJTNA"),
    #         "submitter": findCustomDataField("IEABAVGPJUACJTOC"),
    #         "possibleSolutions": findCustomDataField("IEABAVGPJUACJTOB"),
    #         "solutionRequirements": findCustomDataField("IEABAVGPJUACJTOA"),
    #         "solutionDeveloper": findCustomDataField("IEABAVGPJUACJ7JQ"),
    #         "inputContributor": findCustomDataField("<t>"),
    #         "agreer": findCustomDataField("<t>"),
    #         "decider": findCustomDataField("<t>"),
    #         "implementor": findCustomDataField("<t>"),
    #         "acceptor": findCustomDataField("<t>"),
    #     }

    #     serializedFromWrike = PrioritySubmissionSerializer(
    #         data=extractedWrikeData)

    #     def deletePriorInstance():
    #         """Deletes all prior instances in db based on FolderId"""
    #         instancesOld = PrioritySubmission.objects.filter(
    #             folderId=extractedWrikeData["folderId"]).order_by("-updatedDate")
    #         for instance in instancesOld[1:]:
    #             instance.delete()
    #         return "Older Instances deleted, new one added"

    #     if serializedFromWrike.is_valid():
    #         serializedFromWrike.save()
    #         result = deletePriorInstance()
    #         return Response(result, status=status.HTTP_201_CREATED)

    #     return Response(serializedFromWrike.errors, status=status.HTTP_400_BAD_REQUEST)

    # instance, created = PrioritySubmission.objects.update_or_create(
    #     folderId=extractedWrikeData["folderId"],
    #     folderPermalink=extractedWrikeData["folderPermalink"],
    #     title=extractedWrikeData["title"],
    #     startDate=extractedWrikeData["startDate"],
    #     linksProvided=extractedWrikeData["linksProvided"],
    #     updatedDate=extractedWrikeData["updatedDate"],
    #     workImpact=extractedWrikeData["workImpact"],
    #     statement=extractedWrikeData["statement"],
    #     submitter=extractedWrikeData["submitter"],
    #     possibleSolutions=extractedWrikeData["possibleSolutions"],
    #     solutionRequirements=extractedWrikeData["solutionRequirements"],
    #     solutionDeveloper=extractedWrikeData["solutionDeveloper"],
    #     inputContributor=extractedWrikeData["inputContributor"],
    #     agreer=extractedWrikeData["agreer"],
    #     decider=extractedWrikeData["decider"],
    #     implementor=extractedWrikeData["implementor"],
    #     acceptor=extractedWrikeData["acceptor"],
    #     defaults=serializedFromWrike.is_valid(),
    # )

    # if created:
    #     return Response("Instance created in db", status=status.HTTP_200_OK)
    # else:
    #     return Response("No new instance created in db", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # return Response("Wrong Event Type", status=status.HTTP_400_BAD_REQUEST)


@ api_view(["GET"])
def simple_get(request):
    print(request)
    return Response('Your request has been met', status=status.HTTP_200_OK)
