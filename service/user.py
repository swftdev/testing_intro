# This will become a db model
class User:
    userId = 0
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.watched = []
        self.favorites = []
        self.id = self.userId
        self.userId += 1

    def __repr__(self):
        return self.name

class UserService:
    def __init__(self):
        self.users = []

    def signUp(self, username, password):
        self.users.append(User(username, password))

    def signIn(self, username, password):
        # right now it will return a user only if one is found and creds match
        for u in self.users:
            if u.name == username:
                if u.password == password:
                    return u
