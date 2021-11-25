from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread

# from sandbox import SERVICE_ACCOUNT_FILE
from .models import PrioritySubmission
from datetime import datetime

import json
import os


def populateGSheets(folderId):

    saved_data = PrioritySubmission.objects.get(
        folderId=folderId)

    print(saved_data)
    SCOPES = ['https://www.googleapis.com/auth/drive',
              'https://www.googleapis.com/auth/drive.appdata',
              'https://www.googleapis.com/auth/drive.file',
              'https://www.googleapis.com/auth/spreadsheets'
              ]

    SERVICE_ACCOUNT_FILE = {
        "type": "service_account",
        "project_id": "prioritiesdocumentsheet",
        "private_key_id": "97dc7a52758f5682213b37db2af86a019df93d66",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDRud6Hl3VGOBgn\n4TYRQD4kXaOj75oj5exArs89Ts79eSlrlQ69sCXU/JTnuN+LkqmsLQpL34us22FH\ns9w46jQN1J2Kxq+3Z0WfzXoNTYc1WpBFh+3Xag7C82CKQwJ5gUcK/8WHT5CGLjt7\nUNlFOluo3VoiJzpzcqBboPR2hML5NPAEnfa6UOZazPHLohAvMoPVe8X7iVdbm9f9\nb9BN5ozzUNNCFaxTOBBrroaKvdTCLoV2+ebGCrwMfgrfwH8Zw3HhcfiDBBA7n5Eg\nxM3CU+Pn8puDSsY2UUyRVG55YukB3af57N0OfKG0Z9NGA+DS1yk5kDKPO5UroUdr\n4CNDSnD9AgMBAAECggEAFWkxsWC3taDUa9MvfziydL6lONSlRTTxQZ6XGbM0qTv4\nC+ZTyER2GEsRCKHJxf4FxHDKCaTw0DI1ZD9Aea8EpsTQsJzyziPaP85CaklCnHfP\nyB7FxqV/4aHnITZmHPF4ce8FbiL5UOQ3aQd//ElQ7OnBjJW5/z9HOmjcNvKm1Q9w\nahDYCgVqDLCOuPphu+umvpAAvaXewpg49I/srh0EuFiQ+0rLhEFW36XHOY6TCvec\noxgbNeq6+68H0ij7nH9xaiKpJ2eSMSZEnOJkLXJ3KXRb0IWgE10GMhnWW5H/8buS\nShu9yV25a4gZSdq6sleCibIDxVaU7B5nQ+KVbEPmIQKBgQD2rxHkQx+Rr2LYRc6g\nlReR/jXDlq/b58iqtkBIFiCHOQurIrA1wAvf76oHk2bhHJtNBVXZYlOHl+3FGeqD\n7OM+i+x0a5L2QuT4riIzjN8IEjtbanKkiYvfaVV0WZUem9nRf8X76Nt8vP8NzRtA\nrbybLAsjwoTPNWxd1sXmmaxk4wKBgQDZpX4dej/EAj8di5l6ydrEJcjXhy+H/BPU\n8FJ7VbTFwH71XeZgRB2UvqvFSsjZKUy7JXHqxidoCuH3+nQ3krCHc1z8NQDoDM/N\nSDpIyvx85X+LAaC0dktwC++NdOKsxKs4uKvVA4SsNrakVscwU8ARuxty6yG4FYFo\n1Od6BzuYnwKBgQDV5yDgicPKFAbl+kIdxKpXkdMU8okzalz6imZbG7TBDJotnzqk\noQ6q86rAPvSqpp+TvdifUz+TCA7JJpvQIY07IyG6Ib2hhIf/ix9lC/YpjYWi0z7t\npcd/xlqvNS61B/dsThtjQJtyIoAXe47yGrS86QgPzhBTjMOW6zFXsFFoeQKBgA4d\nN1J+DQiPBLzLwsY9tNwnfyDK+YAeDsMuWor5AeIZG6KZ1kjD4g81VjpTITdEAF/a\ni8qn0wJiQkksisDX2G7QQmVwooBp5EfxuSXjVABdeanwDxXk3fuEKqLHw7NkhZ4G\nC86ijcYFPk7l+cDejYQY2CzZprQjYOMFe4VkVq8NAoGAEuYiAtsN1rn1+5oD+d+F\n1WF4wSHwz3Tzc3x+mAKV1cWyFGntl19bqfcVRW/LcSkpbwe/jrvpsTk70Pti7jnr\nMPmxe4D0WWS21i0GehUabQyNleeuINKN/AnRJ4U5jSE0fGz5RuZqW6Q9OuKE0up9\np6HX/JU33LOkxnkw7Ry2SyQ=\n-----END PRIVATE KEY-----\n",
        "client_email": "imspsa@prioritiesdocumentsheet.iam.gserviceaccount.com",
        "client_id": "114774358409418193029",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/imspsa%40prioritiesdocumentsheet.iam.gserviceaccount.com"
    }

    # SERVICE_ACCOUNT_FILE = json.loads(json.dumps(SERVICE_ACCOUNT_FILE))
    DIRNAME = os.path.dirname(__file__)

    credentials = service_account.Credentials.from_service_account_file(
        # SERVICE_ACCOUNT_FILE,
        os.path.join(DIRNAME, 'serviceAccountKey.json'),
        scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    # these will remain constant; FOLDER_ID will change after shipped
    TEMPLATE_ID = '12zbKd_luG9Bqk_Almpw2Hq7etbV9vESAEGK3bZ3usrg'
    FOLDER_ID = '1StGjH0wVnoJkJWotTvesk_ki2VjHT2K_'

    incoming_file_name = saved_data.title

    request_body = {
        "name": incoming_file_name,
        "parents": [FOLDER_ID],
    }

    # searches google drive api for existence of file based on given name
    response = service.files().list(q=f"name='{incoming_file_name}'",
                                    spaces='drive',
                                    fields='files(id, name)',
                                    ).execute()
    results = response.get('files', [])
    if len(results) == 0:
        new_file = service.files().copy(fileId=TEMPLATE_ID, body=request_body,
                                        supportsAllDrives=True).execute()
        print('File has been created')
    else:
        print(f'results: {results}')

    # UTILITY SCRIPT FOR DELETING REPEATS
    for file in response.get('files', []):
        # Delete files if duplicates
        # service.files().delete(fileId=file.get('id')).execute()
        print('Found file: %s (%s)' % (file.get('name'), file.get('id')))

    # fills in google spreadsheet with acell given the column/row
    gc = gspread.authorize(credentials=credentials)
    sh = gc.open(incoming_file_name)

    folderId = saved_data.folderId
    folderPermalink = saved_data.folderPermalink
    startDate = saved_data.startDate
    updatedDate = saved_data.updatedDate
    linksProvided = saved_data.linksProvided
    workImpact = saved_data.workImpact
    statement = saved_data.statement
    submitter = saved_data.submitter
    possibleSolutions = saved_data.possibleSolutions
    solutionRequirements = saved_data.solutionRequirements
    solutionDeveloper = saved_data.solutionDeveloper
    inputContributor = saved_data.inputContributor
    agreer = saved_data.agreer
    decider = saved_data.decider
    implementor = saved_data.implementor
    acceptor = saved_data.acceptor

    # update the created date if it does not exist else input todays date
    if sh.sheet1.acell('C5').value == None:
        sh.sheet1.update_acell(
            'C5', datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

    sh.sheet1.update_acell('B3', incoming_file_name)
    sh.sheet1.update_acell(
        'C6', startDate.strftime("%Y-%m-%d %H:%M:%S.%f"))
    sh.sheet1.update_acell('B11', statement)
    # sh.sheet1.update_acell('B18', background)
    sh.sheet1.update_acell('B25', workImpact)
    sh.sheet1.update_acell('B33', possibleSolutions)
    sh.sheet1.update_acell('B40', solutionRequirements)
# from wrike in body
    sh.sheet1.update_acell('D57', submitter)
    sh.sheet1.update_acell('D58', solutionDeveloper)
    sh.sheet1.update_acell('D59', inputContributor)
    sh.sheet1.update_acell('D60', agreer)
    sh.sheet1.update_acell('D61', decider)
    sh.sheet1.update_acell('D62', implementor)
    sh.sheet1.update_acell('D63', acceptor)

    sh.sheet1.update_acell('B80', linksProvided)
# footer
    sh.sheet1.update_acell('F116', folderPermalink)
    sh.sheet1.update_acell(
        'F117', updatedDate.strftime("%Y-%m-%d %H:%M:%S.%f"))
    sh.sheet1.update_acell('B118', folderId)

    # sh.sheet1.update_acell('C6', some kind of model id )
