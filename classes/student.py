from database.database import Postgres
from nstu_api.NSTUTRPOAPI.NSTUAPI import NSTUAPI


class Student:
    def __init__(self, name, token):
        self.i_name = name
        
        if not Postgres.select(table="student", where="student_info='{}'".format(self.i_name)):
            student_id = Postgres.select(table="student", columns="max(student_id)")[0]["max"]
            if student_id:
                student_id = int(student_id) + 1
            else:
                student_id = 1

            info = NSTUAPI().get_student_info(token)[1]
            Postgres.insert(table="student", values=[student_id, info["FIO"]])

            if not Postgres.select(table="groups", where="group_info='{}'".format(info["group"])):
                group_id = Postgres.select(table="groups", columns="max(group_id)")[0]["max"]
                if group_id:
                    group_id = int(group_id) + 1
                else:
                    group_id = 1

                Postgres.insert(table="groups", values=[group_id, info["group"]])
                Postgres.insert(table="group_students", values=[group_id, student_id])

    