from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " " * 2
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    old_projects = app.soap.get_project_list()
    name = random_string("np", 8)
    app.project.create(Project(name=name))
    new_projects = app.soap.get_project_list()
    old_projects.append(Project(name=name))
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects,
                                                                 key=Project.id_or_max)
