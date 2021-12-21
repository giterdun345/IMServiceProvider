from requests import status_codes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import environ
from .utilityFunctionsWrike import getFolderDataThenSave

env = environ.Env()
environ.Env.read_env()


@ api_view(['POST'])
def wrike_incoming(request):
    # 20 seconds to allow the dyno to get up and running?
    auth_token = env("WRIKE_AUTH")

    incoming = request.data[0]  # ["data"][0] for Folder GET

    if request.method == 'POST':
        # wrike webhook is inconsistent in id
        if "taskId" in incoming:
            folderId = incoming.get("taskId", None)
            print(f"taskId now {folderId}")

        if "folderId" in incoming:
            folderId = incoming.get("folderId", None)
            print(f"folderId {folderId}")

        eventType = incoming["eventType"]
        print(f"Event type: {eventType}")

    # params and headers used in Wrike GET for folder data
    getFolderUrl = f"https://www.wrike.com/api/v4/folders/{folderId}"
    headers = {
        "method": "GET",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Authorization": "Bearer " + auth_token
    }

    # all eventTypes are sent from Wrike, continues the fuction if the eventType is correct; InCONSISTENT WRIKE API
    if eventType in ['FolderCreated', 'FolderUpdated', 'ProjectStatusChanged', 'ProjectDatesChanged', 'CustomFieldUpdated', 'FolderCustomFieldChanged']:
        getFolderDataThenSave(getFolderUrl, headers)
        return Response("Older Instances deleted, new one added", status=status.HTTP_200_OK)
    else:
        print('Not the event type we dig.')
        return Response('Event Type is not what we are looking for...', status=status.HTTP_200_OK)


@ api_view(["GET"])
def simple_get(request):
    print(request)
    return Response('Your request has been met, nothing to see here.', status=status.HTTP_200_OK)


@ api_view(['POST'])
def wrike_outgoing(requesting):
    wrikeUrl = requesting.data.get('wrikeUrl')
    wrike_auth = env('WRIKE_AUTH')
    title = requesting.data.get('title')
    customFields = requesting.data.get('customFields')
    customFields = str(customFields).replace('"', '\"')

    print(f"before: {customFields}")
    params = {
        "customFields": customFields,
        "title": title,
        "access_token": wrike_auth
    }

    response = requests.request(url=wrikeUrl, params=params, method="PUT")
    return Response('Data transfer complete', status=status.HTTP_200_OK)
