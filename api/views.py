from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import environ
import time
from .utilityFunctionsWrike import getFolderDataThenSave
from .utilityFunctionsGapi import populateGSheets


env = environ.Env()
environ.Env.read_env()


@ api_view(['POST'])
def wrike_incoming(request):
    time.sleep(21)
    # 20 seconds to allow the dyno to get up and running
    # enter into array from wrike webhook
    auth_token = env("WRIKE_AUTH")

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

        print(eventType)
        # print(auth_token)

    # params and headers used in Wrike GET for folder data
    getFolderUrl = f"https://www.wrike.com/api/v4/folders/{folderId}"
    headers = {
        "method": "GET",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Authorization": "Bearer " + auth_token
    }

    # # all eventTypes are sent from Wrike, continues the fuction if the eventType is correct; InCONSISTENT WRIKE API
    if eventType in ['FolderCreated', 'FolderUpdated', 'ProjectStatusChanged', 'ProjectDatesChanged', 'CustomFieldUpdated', 'FolderCustomFieldChanged']:
        print('Entering getFolderDataThenSave')
        getFolderDataThenSave(getFolderUrl, headers)
        print('Stored in db moving onto gapi...')
        populateGSheets(folderId)
        print('Check the google drive now')

        return Response("Older Instances deleted, new one added", status=status.HTTP_200_OK)
    else:
        print('Not the event type we dig.')
        return Response('Event Type is not what we are looking for...', status=status.HTTP_200_OK)


@ api_view(["GET"])
def simple_get(request):
    print(request)
    return Response('Your request has been met', status=status.HTTP_200_OK)
