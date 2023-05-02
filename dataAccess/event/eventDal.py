from dataAccess.dbHelper.sqliteDbHelper import SqliteDbHelper as db_helper
from dataAccess.eventType.eventTypeDal import EventTypeDal
from dataAccess.user.userDal import UserDal
from entity.event import Event
from entity.user import User


class EventDal(db_helper):
    """Olay veri erişim katmanı ile ilgili operasyonların imzalarının bulunduğu sınıf.
    SqliteDbHelper sınıfından miras alır

    @see: SqliteDbHelper
    @category: Data Access"""

    def __init__(self) -> None:
        super().__init__()
        self._udal = UserDal()
        self._etdal = EventTypeDal()

    def insert(self, event: Event) -> None:
        """Veritabanına olay eklemeyi sağlar

        Args:
            event (Event): olay
        """
        self.query = f"INSERT INTO {self.tbl_values.events}({self.tbl_values.u_id}, {self.tbl_values.e_id}, {self.tbl_values.date}, {self.tbl_values.start}, {self.tbl_values.finish}, {self.tbl_values.description}) VALUES({event.user.id}, {event.event_type.id}, '{event.date}', '{event.start_time}', '{event.finish_time}', '{event.description}')"

        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            cn.commit()

    def update(self, event: Event) -> None:
        """Veritabanındaki bir olay güncellemeyi sağlar

        Args:
            event (Event): olay bilgisi
        """

        self.query = f"UPDATE {self.tbl_values.events} SET {self.tbl_values.u_id} = {event.user.id}, {self.tbl_values.e_id} = {event.event_type.id}, {self.tbl_values.date} = '{event.date}', {self.tbl_values.start} = '{event.start_time}', {self.tbl_values.finish} = '{event.finish_time}', {self.tbl_values.description} = '{event.description}' WHERE {self.tbl_values.id} = {event.id}"

        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            cn.commit()

    def delete(self, event: Event) -> None:
        """Veritabanından bir olay  silmeyi sağlar.

        Args:
            event (Event): olay bilgisi
        """
        self.query = f"DELETE FROM {self.tbl_values.events} WHERE {self.tbl_values.id} = {event.id}"

        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            cn.commit()

    def get_all_events(self, user: User, date: str, description="") -> list[Event]:
        """Veritabanındaki tüm olayları bir liste halinde verir

        Returns:
            list[Event]: olay listesi
        """
        self.query = f"SELECT * FROM {self.tbl_values.events} WHERE {self.tbl_values.u_id} = {user.id} AND {self.tbl_values.date}='{date}' AND {self.tbl_values.description} LIKE '%{description}%' ORDER BY {self.tbl_values.start}"

        event_list: list[Event] = []
        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            rows = im.fetchall()

            for row in rows:
                evnt: Event = Event()
                evnt.id = row[0]
                evnt.user.id = row[1]
                evnt.event_type.id = row[2]
                evnt.date = row[3]
                evnt.start_time = row[4]
                evnt.finish_time = row[5]
                evnt.description = row[6]
                evnt.remember_time = row[7]
                event_list.append(evnt)

        return event_list

    def is_event(self, event: Event) -> bool:
        """Olay bilgilerini veritabanı ile kıyaslayıp, veritabanında istenilen tarih ve saatte kayıt olup olmadığını kontrol etmeni sağlar

        Args:
            event (Event): olay bilgileri

        Returns:
            bool: olay durumu
        """
        start_finish_time_list = []

        self.query = f"SELECT {self.tbl_values.start}, {self.tbl_values.finish} FROM {self.tbl_values.events} WHERE {self.tbl_values.date} = '{event.date}' AND {self.tbl_values.u_id} ={event.user.id}"

        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            rows = im.fetchall()

            for row in rows:
                start_finish_time_list.append([row[0], row[1]])

        for value in start_finish_time_list:
            start, finish = value[0].split(":"), value[1].split(":")
            start_hour, start_minute = int(start[0]), int(start[1])
            finish_hour, finish_minute = int(finish[0]), int(finish[1])

            e_start = event.start_time.split(":")
            e_finish = event.finish_time.split(":")
            e_start_hour, e_star_minute = int(e_start[0]), int(e_start[1])
            e_finish_hour, e_finish_minute = int(e_finish[0]), int(e_finish[1])

            if (
                start_hour <= e_start_hour <= finish_hour
                and start_minute <= e_star_minute <= finish_minute
            ) or (
                start_hour <= e_finish_hour <= finish_hour
                and start_minute <= e_finish_minute <= finish_minute
            ):
                return True
        return False

    def get_event_id(self, date: str, start: str, finish: str):
        """Veritabanında kayıtlı olan olayın id bilgisini verir

        Args:
            date (str): olay tarihi
            start (str): olay başlangıç saati
            finish (str): olay bitiş saati

        Returns:
            int: olay id"""
        self.query = f"SELECT {self.tbl_values.id} FROM {self.tbl_values.events} WHERE {self.tbl_values.date} = '{date}' AND {self.tbl_values.start} = '{start}' AND {self.tbl_values.finish} = '{finish}'"

        with self.connect as cn:
            im = cn.cursor()
            im.execute(self.query)
            return im.fetchone()[0]

