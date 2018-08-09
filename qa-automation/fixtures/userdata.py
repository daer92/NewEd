
class UserData:
    def __init__(self, username, password_key):
        self.username = username
        self.password_key = password_key


class NewUserData:
    def __init__(self, first_name, last_name, new_email, new_password):
        self.first_name = first_name
        self.last_name = last_name
        self.new_email = new_email
        self.new_password = new_password
