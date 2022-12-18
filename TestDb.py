from Article import Article
from Db import Db
from SessionUser import SessionUser
from User import User

import string
import random

# Config start

ADMIN = ['admin']
MAXLIST = 5

# Config end

users = {
    'admin': ('password', 'admin@service.net', 'Admin', 'Mustername', '0123 123456', 'street', '8', '1234'),
    'user': ('user', 'ab@cd.ef', 'Noah', 'Rottermanner', '', '', '', '')
}
sessions = {}
lists = {
    'admin': [1],
    'user': []
}
articles = {
    1: [Article(1, 'name', 'groesse', 'preis'), Article(2, 'name2', 'groesse2', 'preis2')]
}


class TestDb(Db):
    def getuser(self, session):
        for user, sess in sessions.items():
            if sess == session:
                return User(users[user][2], user in ADMIN, len(lists[user]) < MAXLIST, user)
        return SessionUser()

    def login(self, username, password):
        if username not in users or users[username][0] != password:  # Benutzername oder Passwort falsch
            return None

        sessions[username] = "".join([random.choice(string.ascii_letters) for x in range(10)])
        print(sessions[username])
        return sessions[username].encode()

    def getlists(self, user):
        if user.username in lists:
            return [x for x in range(1, len(lists[user.username]) + 1)]
        return []

    def getlist(self, user, id):
        try:
            if int(id) > len(lists[user.username]):
                return None
            list = lists[user.username][int(id) - 1]
            return articles[list]
        except:
            return None
