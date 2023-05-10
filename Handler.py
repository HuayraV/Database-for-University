import sqlite3 as sql
from settings import *


class DatabaseLogic():
    def __init__(self):
        with sql.connect(SETTINGS.get('Db_name')) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS "students" (
                "stud_id"	INTEGER UNIQUE,
                "firstname"	TEXT,
                "lastname"	TEXT,
                "direction"	TEXT,
                "course"	INTEGER DEFAULT 1,
                PRIMARY KEY("stud_id")
            )""")
            cur.execute("""CREATE TABLE IF NOT EXISTS "mod_subjects" (
                "mod_id"	        INTEGER,
                "subject"	        TEXT,
                "score_lectures"	INTEGER DEFAULT 0,
                "score_seminars"	INTEGER DEFAULT 0,
                "score_labs"	    INTEGER DEFAULT 0,
                "score_practice"	INTEGER DEFAULT 0
            )""")
            con.commit()
