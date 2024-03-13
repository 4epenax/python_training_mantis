from model.project import Project
import random


def test_add_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create(Project(name="Temp"))
    old_projects = db.get_project_list()
    project = random.choice(old_projects)
    app.project.open_manage_page()
    app.project.open_project_page()
    app.project.open_random_project(project)
    app.project.delete_project()
    app.project.delete_project()
    new_projects = db.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
