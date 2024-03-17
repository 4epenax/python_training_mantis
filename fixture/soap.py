from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['soap']['wsdl'])
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        client = Client(self.app.config['soap']['wsdl'])
        username = self.app.config['web']['username']
        password = self.app.config['web']['password']
        project_list = []
        try:
            projects_array = client.service.mc_projects_get_user_accessible(username, password)
            for i in range(0, len(projects_array)):
                project_list.append(Project(id=projects_array[i].id, name=projects_array[i].name))
            return project_list
        except WebFault:
            return project_list
