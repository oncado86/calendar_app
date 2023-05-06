import sqlite3 as sql
import os

from dataAccess.dbHelper.iSqliteDbHelper import ISqliteDbHelper
from core.dbTables import DbTabes


class SqliteDbHelper(ISqliteDbHelper):
    """SQL işlemleri için yardımcı sınıf
    ISqliteDbHelper arayüzünü uygular

    Args:
        ISqliteDbHelper (interface)

    @see: ISqliteDbHelper
    @category: SQL Helper, Data Access"""

    def __init__(self) -> None:
        super().__init__()
        self._db_path = f"{os.getcwd()}{os.sep}data{os.sep}calender_app.db"
        self._sql_query = ""
        self._db_tables = DbTabes()

    @property
    def tbl_values(self) -> DbTabes:
        """SQL işlemlerinde tablolar ile ilgili bilgileri verir

        Returns:
            DbTabes: SQL tablo bilgileri
        """
        return self._db_tables

    @property
    def connect(self):
        """SQL işlemlerinde veritabanına bağlantı kurar

        Returns:
            sql connect: veritabanı bağlantısı
        """
        return sql.connect(self._db_path)

    @property
    def query(self) -> str:
        """SQL işlemlerinde kullanılacak olan sorgu tümcesini verir

        Returns:
            str: sql sorgusu
        """
        return self._sql_query

    @query.setter
    def query(self, sql_query: str) -> None:
        """SQL işlemlerinde kullanılacak olan sorgu tümcesini ayarlar

        Args:
            sql_query (str): sql sorgusu
        """
        self._sql_query = sql_query
