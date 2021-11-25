from posix import environ
from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread

from sandbox import SERVICE_ACCOUNT_FILE
from .models import PrioritySubmission
from datetime import datetime
# import os
import environ

env = environ.Env()
environ.Env.read_env()


def populateGSheets(folderId):
    '''gets instance by folderId and calls google api to create/update a spreadsheet'''
    saved_data = PrioritySubmission.objects.get(
        folderId=folderId)

    print(saved_data)
    SCOPES = ['https://www.googleapis.com/auth/drive',
              'https://www.googleapis.com/auth/drive.appdata',
              'https://www.googleapis.com/auth/drive.file',
              'https://www.googleapis.com/auth/spreadsheets'
              ]

    # FOR LOCAL
    # SERVICE_ACCOUNT_FILE = json.loads(json.dumps(SERVICE_ACCOUNT_FILE))
    # DIRNAME = os.path.dirname(__file__)
    # SERVICE_ACCOUNT_FILE = os.path.join(DIRNAME, 'serviceAccountKey.json')

    # FOR DEPLOY
    SERVICE_ACCOUNT_FILE = env("GOOGLE_APPLICATION_CREDENTIALS")
    credentials = service_account.Credentials.from_service_account_file(
        # SERVICE_ACCOUNT_FILE,
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES)
    print('credentials...')
    service = build('drive', 'v3', credentials=credentials)
    print('service set...')
    # FOLDER_ID will change after shipped
    TEMPLATE_ID = '12zbKd_luG9Bqk_Almpw2Hq7etbV9vESAEGK3bZ3usrg'
    FOLDER_ID = '1StGjH0wVnoJkJWotTvesk_ki2VjHT2K_'

    incoming_file_name = saved_data.title

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
