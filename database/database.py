import yaml
import psycopg2
from psycopg2.extras import RealDictCursor


class Database:

    @classmethod
    def select(cls, table, columns="*", where=None, limit=None, group_by=None):
        command = "SELECT {} FROM {}".format(
            columns if not isinstance(columns, list) else ','.join(columns),
            table,
        )

        if where:
            command += " WHERE {}".format(where)
        if limit:
            command += " LIMIT {}".format(limit)

        if group_by:
            command += " GROUP BY {}".format(group_by)

        command += ";"
        return cls._execute(command)

    @classmethod
    def insert(cls, table, values):
        arguments = ""
        for numb, value in enumerate(values):
            arguments += "{}".format(
                value if isinstance(value, int) else "'{}'".format(value)
            )
            if numb + 1 < len(values):
                arguments += ","

        command = "INSERT INTO {} VALUES ({});".format(
            table,
            arguments,
        )
        return cls._execute(command, False)

    @classmethod
    def delete(cls, table, where):
        return cls._execute(
            "DELETE FROM {} WHERE {};".format(
                table,
                where
            ),
            False
        )

    @classmethod
    def update(cls, table, variables, where):
        command = ""
        for key, value in variables.items():
            if isinstance(value, int):
                command += "{}={}".format(key, value)
            else:
                command += "{}='{}'".format(key, value)

        return cls._execute(
            "UPDATE {} SET {} WHERE {};".format(
                table,
                command,
                where
            ),
            False
        )

    # private

    @staticmethod
    def _get_params():
        with open("database/configuration.yaml", "r") as f:
            return yaml.load(f.read())["database"]

    @classmethod
    def _get_connection(cls):
        pass

    @classmethod
    def _execute(cls, command, fetch=True):
        pass


class Postgres(Database):

    # private

    @classmethod
    def _get_connection(cls):
        params = cls._get_params()

        return psycopg2.connect(
            host=params["host"],
            port=params["port"],
            user=params["user"],
            password=params["password"],
            database=params["name"]
        )

    @classmethod
    def _execute(cls, command, fetch=True):
        with cls._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(command)
                if fetch:
                    return cur.fetchall()


# print(Postgres.select("lector"))

# schema
'''
CREATE TABLE predmet (predmet_id serial PRIMARY KEY, predmet_info char(64));
CREATE TABLE student (student_id serial PRIMARY KEY, student_info char(64));
CREATE TABLE lector (lector_id serial PRIMARY KEY, lector_info char(64), person_id integer DEFAULT 0);
CREATE TABLE groups (group_id serial PRIMARY KEY, group_info char(64));

CREATE TABLE group_students (group_id integer REFERENCES groups, student_id integer REFERENCES student);

CREATE TABLE predmets_schedule (predmet_id integer REFERENCES predmet, date timestamp, id_group integer REFERENCES groups, lector_id integer REFERENCES lector);

CREATE TABLE attendance (student_id integer REFERENCES student, date timestamp);

create table users(username char(32), password char(32), state char(16));
insert into users values('romanov', '12345678', '');
ALTER TABLE users ADD COLUMN id integer DEFAULT 91;

create table pairs (lector_id integer, pair_id integer, student_id integer);
'''
