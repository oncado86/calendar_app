from sqlalchemy import values
from dataAccess.dbHelper.sqliteDbHelper import SqliteDbHelper as db_helper
from entity.eventType import EventType


class EventTypeDal(db_helper):
    """Olay Tipleri veri erişim katmanı ile ilgili operasyonların imzalarının bulunduğu sınıf.
    SqLiteDbHelper sınıfından miras alır

    @see: SqliteDbHelper
    @category: Data Access"""

    def __init__(self) -> None:
        super().__init__()

    def insert(self, event_type: EventType) -> None:
        """Veritabanına olay tipi eklemeyi sağlar

        Args:
            event_type (EventType): olay tipi
        """
        self.query = f"INSERT INTO {self.tbl_values.event_types}({self.tbl_values.name}) VALUES('{event_type.name}')"

        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            cn.commit()

    def update(self, event_type: EventType) -> None:
        """Veritabanındaki bir olay tipini güncellemeyi sağlar

        Args:
            event_type (EventType): olay tipi
        """
        self.query = f"UPDATE {self.tbl_values.event_types} SET {self.tbl_values.name}='{event_type.name}' WHERE {self.tbl_values.id} = {event_type.id}"

        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            cn.commit()

    def get_event_type_id(self, event_name: str):
        """Veritabanından olay adı ile etkinliğin id bilgisini getirmeyi sağlar

        Args:
            event_name (str): olay tip adı

        Returns:
            int: olay tip id
        """
        self.query = f"SELECT {self.tbl_values.id} FROM {self.tbl_values.event_types} WHERE {self.tbl_values.name}='{event_name}'"

        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            return im.fetchone()[0]

    def is_event_type(self, event_name: str) -> bool:
        """Olay adı ile etkinliğin veritabanına kayıtlı olup olmadığını kontrol edetmeyi sağlar

        Args:
            event_name (str): olay adı

        Returns:
            bool: olay tipi durumu
        """
        self.query = f"SELECT COUNT(*) FROM {self.tbl_values.event_types} WHERE {self.tbl_values.name}='{event_name}'"

        count = 0
        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            count = im.fetchone()[0]

        return count > 0

    def get_all_event_types(self, name="") -> list[EventType]:
        """Veritabanındaki tüm olaylar tiplerini bir liste halinde verir

        Returns:
            list[EventType]: olay tipi listesi
        """
        self.query = f"SELECT * FROM {self.tbl_values.event_types} WHERE {self.tbl_values.name} LIKE '%{name}%' ORDER BY {self.tbl_values.name}"

        event_type_list: list[EventType] = []
        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            values = im.fetchall()

            for value in values:
                e_type: EventType = EventType()
                e_type.id = value[0]
                e_type.name = value[1]
                event_type_list.append(e_type)

        return event_type_list

    def delete(self, event_type: EventType) -> None:
        """Veritabanından bir olay tipini silmeyi sağlar.

        Args:
            event_type (EventType): olay tipi bilgisi
        """
        self.query = f"DELETE FROM {self.tbl_values.event_types} WHERE {self.tbl_values.id} = {event_type.id}"

        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            cn.commit()

    def get_event_type(self, event_id: int) -> EventType:
        """Veritabanından etkinlik verilerini getirmeyi sağlar.

        Args:
            id (int): etkinlik id

        Returns:
            EventType: etkinlik bilgileri
        """

        self.query = f"SELECT * FROM {self.tbl_values.event_types} WHERE {self.tbl_values.id} = {event_id}"

        event = EventType()
        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            values = im.fetchall()

            for value in values:
                event.id = value[0]
                event.name = value[1]

        return event
