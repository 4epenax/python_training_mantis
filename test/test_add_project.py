import pytest
from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " "*2
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [
    Project(name=random_string("new", 8))
]


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project, db):
    old_projects = db.get_project_list()
    app.project.create(project)
    new_projects = db.get_project_list()
    old_projects.append(project)
    assert old_projects == new_projects
