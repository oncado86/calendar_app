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
    def sql(self):
        raise NotImplementedError("This is not implemented 'sql' from ISqliteDbHelper")

    @sql.setter
    @interface
    def sql(self, query: str):
        raise NotImplementedError("This is not implemented 'sql' from ISliceDbHelper")
