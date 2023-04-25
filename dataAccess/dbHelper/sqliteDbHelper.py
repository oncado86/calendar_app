import sqlite3 as sql
import os

from dataAccess.dbHelper.iSqliteDbHelper import ISqliteDbHelper
from core.db_tables import DbTabes

class SqliteDbHelper(ISqliteDbHelper):
    def __init__(self) -> None:
        super().__init__()
        self._dp_path = f"{os.getcwd()}{os.sep}data{os.sep}takvim_uygulamasi.db"
        self._sql_query = ""
        self._db_tables= DbTabes()
