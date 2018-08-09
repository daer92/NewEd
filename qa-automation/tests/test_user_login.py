# -*- coding: utf-8 -*-

from fixtures.application import Application
from fixtures.userdata import UserData
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login(app):
        app.open_home_page()
        app.login_process(UserData(username="ilya-benetton@mercaux.com", password_key="123321"))
        app.logout()


def test_incorrect_login(app):
        app.open_home_page()
        app.login_process(UserData(username="dddd@incorrect.com", password_key="2222222"))
