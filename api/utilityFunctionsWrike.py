from rest_framework.response import Response
import requests
from rest_framework import status
from .models import PrioritySubmission
from .serializers import PrioritySubmissionSerializer


def getFolderDataThenSave(getFolderUrl, headers):
    '''given  a folderId, makes a call to Wrike API to obtain all data, populates database by deleting past instances if they exist'''
    try:
        response = requests.get(getFolderUrl, headers=headers)
        print(f"Stage 1:  {response.status_code}")
        getWrikeData = response.json()
        print(f"Stage 2: {getWrikeData}")

        if response.status_code == 200:
            getWrikeData = getWrikeData.get('data')[0]
            print(f"Stage 3: {getWrikeData}")
        else:
            print(f"Stage 3: Failed")
            return Response("No Folder Found in Wrike", status=status.HTTP_200_OK)

        def findCustomDataField(id):
            """Searches custom field by ID to return its value"""
            return next((item["value"] for item in getWrikeData["customFields"] if item["id"] == id), None)

        statement = findCustomDataField("IEABAVGPJUACJTNA")
        workImpact = findCustomDataField("IEABAVGPJUACJTN7")
        solutionRequirements = findCustomDataField('IEABAVGPJUACJTOA')
        possibleSolutions = findCustomDataField('IEABAVGPJUACJTOB')
        linksProvided = findCustomDataField("IEABAVGPJUACJTO4")
        submitter = findCustomDataField('IEABAVGPJUACJTOC')
        solutionDeveloper = findCustomDataField("IEABAVGPJUACJ7JQ")

        if submitter == "":
            submitter = 'Anonymous'

        extractedWrikeData = {
            "folderId": getWrikeData["id"],
            "folderPermalink": getWrikeData["permalink"],
            "title": getWrikeData["title"],
            "startDate": getWrikeData["createdDate"],
            "updatedDate": getWrikeData["updatedDate"],
            "linksProvided": linksProvided,
            "workImpact": workImpact,
            "statement": statement,
            "submitter": submitter,
            "possibleSolutions": possibleSolutions,
            "solutionRequirements": solutionRequirements,
            "solutionDeveloper": solutionDeveloper,
            "inputContributor": "r",
            "agreer": "r",
            "decider": "r",
            "implementor": "r",
            "acceptor": "r",
        }

        serializedFromWrike = PrioritySubmissionSerializer(
            data=extractedWrikeData)

        def deletePriorInstance():
            """Deletes all prior instances in db based on FolderId"""
            instancesOld = PrioritySubmission.objects.filter(
                folderId=extractedWrikeData["folderId"]).order_by("-updatedDate")
            for instance in instancesOld[1:]:
                print(f"Searching ... {instance}")
                instance.delete()
            return "Older Instances deleted, new one added"

        if serializedFromWrike.is_valid():
            print('Made it to is valid')
            serializedFromWrike.save()
            result = deletePriorInstance()
            yield extractedWrikeData
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(serializedFromWrike.errors, status=status.HTTP_200_OK)

    except:
        import sys
        print(str(sys.exc_info()))
