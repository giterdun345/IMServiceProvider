from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import environ
from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread
import os
import urllib
import sys

env = environ.Env()
environ.Env.read_env()


@ api_view(['POST'])
def project_incoming(request):
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

    # projectInitiationFolderId = 'IEABAVGPI4YG5C5X'  TesttaskId:'IEABAVGPI4YG5HRK'
    getFolderUrl = f"https://www.wrike.com/api/v4/folders/{folderId}"
    headers = {
        "method": "GET",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Authorization": "Bearer " + auth_token
    }

    # project status changed; cosidering the status goes from waiting for approval to something else, will generate the document
    if eventType in ['ProjectStatusChanged']:
        # get the folder information , customData fields project name (title), created date (createdDate), start end dates (project.startDate, project.endDate)
        try:
            response = requests.get(getFolderUrl, headers=headers)
            print(f"Stage 1:  {response.status_code}")
            getWrikeData = response.json()
            if response.status_code == 200:
                getWrikeData = getWrikeData.get('data')[0]
                print(getWrikeData)
                sys.stdout.flush()

            else:
                return Response("No Folder Found in Wrike", status=status.HTTP_200_OK)
        except:
            import sys
            print(str(sys.exc_info()))
            sys.stdout.flush()

    else:
        return Response('Event Type is not what we are looking for...', status=status.HTTP_200_OK)

    # UPLOAD WITH  GAPI
    folderId = getWrikeData["id"]
    folderPermalink = getWrikeData["permalink"]
    title = getWrikeData["title"]
    createdDate = getWrikeData["createdDate"]
    startDate = getWrikeData["project"]["startDate"]
    endDate = getWrikeData["project"]["endDate"]
    currentStatus = getWrikeData["project"]["customStatusId"]

    if currentStatus == 'IEABAVGPJMA73JDT':
        return Response("Project has not been approved; no document creation.", status=status.HTTP_200_OK)

    SCOPES = ['https://www.googleapis.com/auth/drive',
              'https://www.googleapis.com/auth/drive.appdata',
              'https://www.googleapis.com/auth/drive.file',
              'https://www.googleapis.com/auth/spreadsheets'
              ]

    # FOR LOCAL
    # DIRNAME = os.path.dirname(__file__)
    # SERVICE_ACCOUNT_FILE = os.path.join(DIRNAME, 'serviceAccountKey.json')

    # FOR DEPLOY
    SERVICE_ACCOUNT_FILE = env("GOOGLE_APPLICATION_CREDENTIALS")

    # CREDENTIALS
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    TEMPLATE_ID = '1CoNcyCSRI7Y_ieQCZyGXquD1HyJQQ3ACDRnHc087_l0'
    FOLDER_ID = '1fAcPXuAM5JU4SWqGGxR5yKBl0FJZIa5n'
    incoming_file_name = f'{title} Project Lifecycle Checklist'

    request_body = {
        "name": incoming_file_name,
        "parents": [FOLDER_ID],
    }

    print("Searching files on gdrive...")
    # searches google drive api for existence of file based on given name
    response = service.files().list(q=f"name='{incoming_file_name}'",
                                    spaces='drive',
                                    fields='files(id, name)',
                                    ).execute()

    results = response.get('files', [])
    # created tells IMSP to send an attachment or not to wrike on initial creation
    created = ''
    if len(results) == 0:
        created = True
        newPMOFile = service.files().copy(fileId=TEMPLATE_ID, body=request_body,
                                          supportsAllDrives=True).execute()
        print(newPMOFile)
        print('File has been created')
        sys.stdout.flush()
    else:
        created = False
        print(f'results: {results}')
        sys.stdout.flush()

    # custom status id to text
    if currentStatus == "IEABAVGPJMBPKMVU":
        currentStatus = "Not Started"

    if currentStatus == "IEABAVGPJMBME6VY":
        currentStatus = "Waiting for Approval"

    if currentStatus == "IEABAVGPJMA73JCI":
        currentStatus = "Green"

    if currentStatus == "IEABAVGPJMA73JCS":
        currentStatus = "Yellow"

    if currentStatus == "IEABAVGPJMA73JC4":
        currentStatus = "Red"

    if currentStatus == "IEABAVGPJMBFYZFQ":
        currentStatus = "Critical red"

    if currentStatus == "IEABAVGPJMA73JCJ":
        currentStatus = "Completed"

    if currentStatus == "IEABAVGPJMA73JDI":
        currentStatus = "On Hold"

    if currentStatus == "IEABAVGPJMA73JDT":
        currentStatus = "Not Approved"

    gc = gspread.authorize(credentials=credentials)
    sh = gc.open(incoming_file_name)
    sh.sheet1.update_acell('C4', title)
    sh.sheet1.update_acell("C9", folderPermalink)
    sh.sheet1.update_acell('F12', currentStatus)
    sh.sheet1.update_acell('C11', createdDate)
    sh.sheet1.update_acell('C12', startDate)
    sh.sheet1.update_acell('C13', endDate)

    if created:
        # post attachment
        print('Sending attachment...')
        sys.stdout.flush()

        postAttachment = f"https://www.wrike.com/api/v4/folders/{folderId}/attachments"
        headers = {
            "method": "POST",
            "Content-Type": "application/octet-stream",
            "User-Agent": "Mozilla/5.0",
            "Authorization": "Bearer " + auth_token,
            "X-Requested-With": "XMLHttpRequest",
            "X-File-Name": incoming_file_name,
        }

        response = requests.post(
            postAttachment, headers=headers, data=newPMOFile)
        print(f"Attachment Response:  {response.json()}")
        sys.stdout.flush()

    return Response("Created new document from template; Data populated template", status=status.HTTP_200_OK)


@ api_view(["GET"])
def project_get(request):
    print(request)
    sys.stdout.flush()
    return Response('Nothing here yet, but your request has been met.', status=status.HTTP_200_OK)


# [{
#     "webhookId": "IEAADQQLKQAKAOPB",
#     "eventAuthorId": "KQAKAOPB",
#     "eventType": "ProjectStatusChanged",
#     "folderId": "IEABAVGPI4YKF42S",
#     "lastUpdatedDate": "2016-10-10T11:33:28Z"
# }]
