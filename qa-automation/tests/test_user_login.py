# -*- coding: utf-8 -*-

from modules.logindata import UserData



def test_login(app):
        app.open_home_page()
        app.session.login_process(UserData(username="ilya-benetton@mercaux.com", password_key="123321"))
        app.session.logout()


def test_incorrect_login(app):
        app.open_home_page()
        app.session.login_process(UserData(username="dddd@incorrect.com", password_key="2222222"))
