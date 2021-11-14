# import re
# from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
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
    incoming = request.data[0]  # ["data"][0] for Folder GET
    print(incoming)
    # relevant info from webhook
    if request.method == 'POST':
        # wrike webhook is inconsistent in id
        if "folderId" in incoming:
            folderId = incoming.get("folderId", None)
            print(f"folderId {folderId}")

        if "taskId" in incoming:
            folderId = incoming.get("taskId", None)
            print(f"taskId now {folderId}")

        eventType = incoming["eventType"]
        auth_token = env("WRIKE_AUTH")

    # params and headers used in Wrike GET for folder data
    getFolderUrl = f"https://www.wrike.com/api/v4/folders/{folderId}"
    headers = {
        "method": "GET",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Authorization": "Bearer " + auth_token
    }

    # # all eventTypes are sent from Wrike, continues the fuction if the eventType is correct
    if eventType == 'FolderCreated' or eventType == 'FolderUpdated':
        getWrikeData = requests.get(getFolderUrl, headers=headers)
        print(f"Stage 1:  {getWrikeData}")
        getWrikeData = getWrikeData.json().get('data')[0]
        print(f"Stage 2: {getWrikeData}")

        def findCustomDataField(id):
            """Searches custom field by ID to return its value"""
            # extract customFields by id
            # statement = 'IEABAVGPJUACJTNA'
            # workImpact = 'IEABAVGPJUACJTN7'
            # solutionRequirements = 'IEABAVGPJUACJTOA'
            # possibleSolutions = 'IEABAVGPJUACJTOB'
            # link = 'IEABAVGPJUACJTO4'
            # submitter = 'IEABAVGPJUACJTOC'
            # ADD USER CUSTOMDATA FIELDS for additional ids
            return next((item["value"] for item in getWrikeData["customFields"] if item["id"] == id), None)

        extractedWrikeData = {
            "folderId": getWrikeData["id"],
            "folderPermalink": getWrikeData["permalink"],
            "title": getWrikeData["title"],
            "startDate": getWrikeData["createdDate"],
            "updatedDate": getWrikeData["updatedDate"],
            "linksProvided": findCustomDataField("IEABAVGPJUACJTO4"),
            "workImpact": findCustomDataField("IEABAVGPJUACJTN7"),
            "statement": findCustomDataField("IEABAVGPJUACJTNA"),
            "submitter": findCustomDataField("IEABAVGPJUACJTOC"),
            "possibleSolutions": findCustomDataField("IEABAVGPJUACJTOB"),
            "solutionRequirements": findCustomDataField("IEABAVGPJUACJTOA"),
            "solutionDeveloper": findCustomDataField("IEABAVGPJUACJ7JQ"),
            "inputContributor": findCustomDataField("<t>"),
            "agreer": findCustomDataField("<t>"),
            "decider": findCustomDataField("<t>"),
            "implementor": findCustomDataField("<t>"),
            "acceptor": findCustomDataField("<t>"),
        }

        serializedFromWrike = PrioritySubmissionSerializer(
            data=extractedWrikeData)

        def deletePriorInstance():
            """Deletes all prior instances in db based on FolderId"""
            instancesOld = PrioritySubmission.objects.filter(
                folderId=extractedWrikeData["folderId"]).order_by("-updatedDate")
            for instance in instancesOld[1:]:
                instance.delete()
            return "Older Instances deleted, new one added"

        if serializedFromWrike.is_valid():
            serializedFromWrike.save()
            result = deletePriorInstance()
            return Response(result, status=status.HTTP_201_CREATED)

    return Response(serializedFromWrike.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


@ api_view(["GET"])
def simple_get(request):
    print(request)
    return Response('Your request has been met', status=status.HTTP_200_OK)
