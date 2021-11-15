# import re
# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import environ
from .uitilityFunctions import getFolderDataThenSave

env = environ.Env()
environ.Env.read_env()


@ api_view(['POST'])
def wrike_incoming(request):
    # enter into array from wrike webhook
    incoming = request.data[0]  # ["data"][0] for Folder GET
    print(incoming)
    # relevant info from webhook
    if request.method == 'POST':
        # wrike webhook is inconsistent in id
        if "taskId" in incoming:
            folderId = incoming.get("taskId", None)
            print(f"taskId now {folderId}")

        if "folderId" in incoming:
            folderId = incoming.get("folderId", None)
            print(f"folderId {folderId}")

        eventType = incoming["eventType"]
        auth_token = env("WRIKE_AUTH")
        print(eventType)
        print(auth_token)

    # params and headers used in Wrike GET for folder data
    getFolderUrl = f"https://www.wrike.com/api/v4/folders/{folderId}"
    headers = {
        "method": "GET",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Authorization": "Bearer " + auth_token
    }

    print(eventType)
    # # all eventTypes are sent from Wrike, continues the fuction if the eventType is correct ICONSISTENT WRIKE API
    if eventType in ['FolderCreated', 'FolderUpdated', 'ProjectStatusChanged', 'CustomFieldUpdated', 'FolderCustomFieldChanged']:
        getFolderDataThenSave(getFolderUrl, headers)

        def populateGSheets():
            return ""

        return Response("Older Instances deleted, new one added", status=status.HTTP_200_OK)
    else:
        return Response('Event Type is not what we are looking for...', status=status.HTTP_200_OK)


@ api_view(["GET"])
def simple_get(request):
    print(request)
    return Response('Your request has been met', status=status.HTTP_200_OK)
