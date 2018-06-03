from database.database import Postgres

class Lecturer:

    def __init__(self, name):
        self.i_name = name
        self.i_authorized_flag = False
        self.i_id = 0

    def authorize(self, password):
        lector = Postgres.select(
            "users",
            where="password='{}' and username='{}'".format(
                password,
                self.i_name
            )
        )

        if lector:
            self.i_authorized_flag = True
            self.i_id = lector[0]["id"]
            return self.get_id()


    def get_authorized_flag(self):
        return self.i_authorized_flag

    def get_id(self):
        return self.i_id
