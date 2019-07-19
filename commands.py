from __future__ import print_function
import datetime
import pickle
import sys
import os
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/documents"]

DOCUMENT_NAME = str(sys.argv[1])


def main():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("docs", "v1", credentials=creds)

    title = DOCUMENT_NAME
    body = {"title": title}
    doc = service.documents().create(body=body).execute()

    DOCUMENT_ID = doc.get("documentId")
    DOCUMENT_URL = "https://docs.google.com/document/d/" + DOCUMENT_ID

    print("Created document with id: {0}".format(DOCUMENT_ID))

    print("The title of the document is: {}".format(doc.get("title")))

    os.system("python -m webbrowser -t " + DOCUMENT_URL)
    os.system("python -m webbrowser -t https://notion.so/utsav")


if __name__ == "__main__":
    main()
