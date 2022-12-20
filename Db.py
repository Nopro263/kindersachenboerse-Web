from SessionUser import SessionUser
from User import User


class Db:
    def __init__(self):
        pass

    def getuser(self, session):
        return SessionUser()

    def getlists(self, user):
        return

    def getlist(self, user, id):
        pass

    def login(self, username, password):
        return "SESSION"

    def logout(self, session):
        return

    def register(self, username, email, fname, lname, teln, street, house, plz):
        return

    def createlist(self, user):
        return

    def createarticle(self, user, name, price, size, list):
        return

    def deletearticle(self, user, list, article):
        return
