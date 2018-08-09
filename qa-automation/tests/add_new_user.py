from fixtures.application import Application
from fixtures.userdata import NewUserData, UserData
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.open_home_page()
    app.login_process(UserData(username="ilya-benetton@mercaux.com", password_key="123321"))
    app.add_new_user(NewUserData(first_name="Auto1222", last_name="Test", new_email="auto@test212.ru", new_password="123"))


#def test_delete_user(app):
    #app.open_home_page()
    #app.login_process(UserData(username="ilya-benetton@mercaux.com", password_key="123321"))
    #app.delete_user()