from fixtures.application import Application
from modules.new_userdata import NewUserData
from modules.logindata import UserData




def test_add_new_user(app):
        app.open_home_page()
        app.session.login_process(UserData(username="ilya-benetton@mercaux.com", password_key="123321"))
        app.selector.add_new_user_select()
        app.input.add_new_user_input(NewUserData(first_name="Auto", last_name="Test", new_email="auto@test1.ru", new_password="123"))
