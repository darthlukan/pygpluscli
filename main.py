import sys
import time
import json
import gflags
import httplib2
from pprint import pprint
from datetime import datetime, timedelta
from oauth2client.tools import run
from oauth2client.file import Storage
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow

from ConfigParser import SafeConfigParser


class Auth(object):
    """
    Google Authorization object.  Uses Web App OAuth2 flow
    to seit and get authentication so that we only have to interact
    on initial setup.  Saves tokens in secrets.dat.
    """

    def __init__(self):
        self.http = ''
        self.service = ''
        self.FLAGS = gflags.FLAGS
        self.secrets = ''

        config = SafeConfigParser()
        config.read('keys.dat')
        self.DEVKEY = config.get('CONFIG', 'devkey')

        with open('client_secrets.json') as secrets:
            self.secrets = json.load(secrets)

        self.FLOW = OAuth2WebServerFlow(
            client_id=self.secrets['installed']['client_id'],
            client_secret=self.secrets['installed']['client_secret'],
            scope="https://www.googleapis.com/auth/plus.login",
            user_agent='Playground/v1'
        )

        self.storage = Storage('secrets.dat')
        self.credentials = self.storage.get()

    def validate_creds(self):
        """
        Pulls credentials from storage, executes auth flow otherwise.

        Returns credentials object.
        """
        if self.credentials is None or self.credentials.invalid is True:
            self.credentials = run(self.FLOW, self.storage)
        return self.credentials

    def get_authed_http(self):
        """
        Sets up and returns an HTTP object authorized
        with our credentials.
        """
        self.http = httplib2.Http()
        self.http = self.credentials.authorize(self.http)
        return self.http

    def build_service(self):
        """
        Builds a service object based on authed http object,
        developer API key, and API version arguments.

        Returns service (object)
        """
        # Build a service object for interacting with the API. Visit
        # the Google APIs Console to get a developerKey for your own application.
        self.service = build(serviceName='plus', version='v1', http=self.http,
                             developerKey=self.DEVKEY)
        return self.service


class App(object):

    def __init__(self, service):
        self.service = service
        self.language = 'en'
        self.myId = 'me'  # The authed user (from initial authflow in Auth class.
        self.myCircledIds = []

    def get_circled_people(self):
        nextPageToken = None
        while True:
            request = self.service.people().list(userId=self.myId, collection='visible', pageToken=nextPageToken)
            peopleResource = request.execute()
            if 'items' in peopleResource:
                for person in peopleResource['items']:
                    self.myCircledIds.append(person['id'])
            try:
                nextPageToken = peopleResource['nextPageToken']
            except KeyError:
                break
        return self.myCircledIds

    def get_all_activities(self):
        activitiesResource = self.service.activities()
        for person in self.myCircledIds:
            request = activitiesResource.list(userId=int(person), collection='public', maxResults=2)
            if request is not None:
                activitiesDoc = request.execute()
                if 'items' in activitiesDoc:
                    for activity in activitiesDoc['items']:
                        print activity['published'], activity['object']['content']
                    print "======================================================="


def main():
    auth = Auth()
    auth.validate_creds()
    auth.get_authed_http()
    service = auth.build_service()

    print "We have a service object!"
    pprint(service)

    app = App(service)
    app.get_circled_people()
    app.get_all_activities()

    return sys.exit()


if __name__ == '__main__':
    main()
