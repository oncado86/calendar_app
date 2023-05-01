from abc import abstractmethod as interface


class ISqliteDbHelper:
    """Veritabanı erişim katmanı için gerekli olan metotların imzalarını tutar.

    @category: Interface, Data Access"""

    @property
    @interface
    def connect(self):
        raise NotImplementedError(
            "This is not implemented 'connect' from ISqliteDbHelper"
        )

    @property
    @interface
    def query(self) -> str:
        raise NotImplementedError("This is not implemented 'sql' from ISqliteDbHelper")

    @query.setter
    @interface
    def query(self, query: str) -> None:
        raise NotImplementedError("This is not implemented 'sql' from ISqliteDbHelper")

    @property
    @interface
    def tbl_values(self):
        raise NotImplementedError(
            "This is not implemented 'tbl_values' from ISqliteDbHelper"
        )
