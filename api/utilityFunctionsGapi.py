from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread
from datetime import datetime
import os
import environ

env = environ.Env()
environ.Env.read_env()


def populateGSheets(instance):
    '''gets instance by folderId and calls google api to create/update a spreadsheet'''
    print(f'The saved data is called {instance}')

    SCOPES = ['https://www.googleapis.com/auth/drive',
              'https://www.googleapis.com/auth/drive.appdata',
              'https://www.googleapis.com/auth/drive.file',
              'https://www.googleapis.com/auth/spreadsheets'
              ]

    # FOR LOCAL
    DIRNAME = os.path.dirname(__file__)
    SERVICE_ACCOUNT_FILE = os.path.join(DIRNAME, 'serviceAccountKey.json')

    # FOR DEPLOY
    # SERVICE_ACCOUNT_FILE = env("GOOGLE_APPLICATION_CREDENTIALS")

    # CREDENTIALS
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    TEMPLATE_ID = '12zbKd_luG9Bqk_Almpw2Hq7etbV9vESAEGK3bZ3usrg'
    FOLDER_ID = '1StGjH0wVnoJkJWotTvesk_ki2VjHT2K_'
    incoming_file_name = instance.title

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
        service.files().copy(fileId=TEMPLATE_ID, body=request_body,
                             supportsAllDrives=True).execute()
        print('File has been created')
    else:
        print(f'results: {results}')

    # UTILITY SCRIPT FOR DELETING REPEATS NOT REQUIRED IN PROD
    # for file in response.get('files', []):
    # Delete files if duplicates
    # service.files().delete(fileId=file.get('id')).execute()
    # print('Found file: %s (%s)' % (file.get('name'), file.get('id')))

    # fills in google spreadsheet with acell given the column/row
    gc = gspread.authorize(credentials=credentials)
    sh = gc.open(incoming_file_name)

    folderId = instance.folderId
    folderPermalink = instance.folderPermalink
    dateCreated = instance.dateCreated
    startDate = instance.startDate
    updatedDate = instance.updatedDate
    linksProvided = instance.linksProvided
    workImpact = instance.workImpact
    statement = instance.statement
    submitter = instance.submitter
    possibleSolutions = instance.possibleSolutions
    solutionRequirements = instance.solutionRequirements
    solutionDeveloper = instance.solutionDeveloper
    inputContributor = instance.inputContributor
    agreer = instance.agreer
    decider = instance.decider
    implementor = instance.implementor
    acceptor = instance.acceptor
    currentStatus = instance.currentStatus

    # intentional to slow the process for gspread quota
    if currentStatus == "IEABAVGPJMBVTIMO":
        currentStatus = "Incoming"

    if currentStatus == "IEABAVGPJMBVTINC":
        currentStatus = "Requirements"

    if currentStatus == "IEABAVGPJMBVTIMY":
        currentStatus = "Solution Development"

    if currentStatus == "IEABAVGPJMBZLCL6":
        currentStatus = "Implementation"

    if currentStatus == "IEABAVGPJMBVTIMP":
        currentStatus = "Resolved"

    if currentStatus == "IEABAVGPJMBVTINO":
        currentStatus = "Pending Scheduling"

    if currentStatus == "IEABAVGPJMB2VOIE":
        currentStatus = "Scheduled"

    if currentStatus == "IEABAVGPJMBVTINZ":
        currentStatus = "Cancelled"

    sh.sheet1.update_acell('B3', incoming_file_name)
    sh.sheet1.update_acell('C5', dateCreated.strftime("%Y-%m-%d %H:%M:%S.%f"))
    sh.sheet1.update_acell('C6', startDate)
    sh.sheet1.update_acell('C7', currentStatus)
    sh.sheet1.update_acell('B11', statement)
    # sh.sheet1.update_acell('B18', background) ??? dependent on form
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
