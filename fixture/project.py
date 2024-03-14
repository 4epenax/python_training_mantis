import re

from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def domain(self):
        return "/mantisbt/"

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_overview_page.php") and len(
                wd.find_elements_by_link_text("Site Information")) > 0):
            wd.find_element_by_css_selector(
                f'a[href="{self.domain()}manage_overview_page.php"]').click()

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(
                wd.find_element_by_link_text("Create New Project")) > 0):
            wd.find_element_by_css_selector(
                f'a[href="{self.domain()}manage_proj_page.php"]').click()

    def new_project(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()

    def change_project_name(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)

    def submit_create_project(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="Add Project"]').click()

    def return_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(
                wd.find_element_by_link_text("Operation successful")) > 0):
            wd.find_element_by_css_selector('a[href="manage_proj_page.php"]').click()

    def open_random_project(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector(
            'a[href="manage_proj_edit_page.php?project_id=%s"]' % self.clear(str(id))).click()

    def clear(self, s):
        return re.sub(":.*", "", s)

    def delete_project(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()

    def create(self, project):
        self.open_manage_page()
        self.open_project_page()
        self.new_project()
        self.change_project_name(project)
        self.submit_create_project()
        self.return_project_page()
