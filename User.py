from SessionUser import SessionUser


class User(SessionUser):
    def __init__(self, dpname, may_see_admin, may_create_new_list, username):
        self.may_create_new_list = may_create_new_list
        self.may_see_admin = may_see_admin
        self.logged_in = True
        self.dpname = dpname
        self.username = username
