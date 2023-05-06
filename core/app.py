from entity.event import Event
from entity.eventType import EventType
from entity.user import User
from business.event.eventManager import EventManager
from business.eventType.eventTypeManager import EventTypeManager
from business.user.userManager import UserManager
from random import randint
from datetime import datetime

from PyQt5.QtWidgets import (
    QTableWidget as table_widget,
    QHeaderView as header_view,
    QTableWidgetItem as table_widget_item,
    QMessageBox as message_box,
)


class APP:
    """Uygulamayla ilgili arka plan katmanlarının tutulduğu katman

    @see: EventManager, EventTypeManager, UserManager, AdminManager
    @see: User, Event, EventType
    @category: Business, Manager, Tool"""

    def __init__(self) -> None:
        self._manager: MANAGER = MANAGER()
        self._pages: PAGES = PAGES()
        self._tools: TOOLS = TOOLS()
        self._user: User = User()
        self._table: TABLEWIDGET = TABLEWIDGET()

    @property
    def managers(self):
        """Manager sınıflarını verir

        Returns:
            manager: manager
        """
        return self._manager

    @property
    def pages(self):
        """UI için giriş yapma sayfasının indeksini verir
        Returns:
            int: page number"""
        return self._pages

    @property
    def tools(self):
        """Uygulamanın bir çok yerinde kullanılabileceke operastonlar

        Returns:
            tools (class): araçlar"""
        return self._tools

    @property
    def user(self) -> User:
        """Oturum açmış olan kullanıcıyı verir

        Returns:
            User: oturum açan kullanıcı
        """
        return self._user

    @user.setter
    def user(self, current_user: User):
        """Oturum açan kullanıcıyı ayarlar

        Args:
            current_user (User): oturum açan kullanıcı
        """
        self._user = current_user

    @property
    def table(self):
        """Veri tabanından gelen ilili verilerin, tablo aracında gösterilebilmesi için gerekli olan operasyonları verir

        Returns:
            tablewidget (class): tablo araçları
        """
        return self._table


class MANAGER:
    """Uygulamayla ilgili Manager sınıflarının tutulduğu sınıf

    @see: EventManager, EventTypeManager, UserManager, AdminManager
    @category: Business, Manager, Tool
    """

    def __init__(self) -> None:
        self._user: UserManager = UserManager()
        self._event_manager: EventManager = EventManager()
        self._event_type_manager: EventTypeManager = EventTypeManager()

    @property
    def user(self):
        """User sınıfını verir

        Returns:
            manager: user"""
        return self._user

    @property
    def event(self):
        """Event sınıfını verir

        Returns:
            manager: event
        """
        return self._event_manager

    @property
    def event_type(self):
        """EventType sınıfını verir

        Returns:
            manager: event type
        """
        return self._event_type_manager


class PAGES:
    """Arayüzdeki sayfaların organizasyonu için gerekli özellikleri verir

    @category: Tool Class

    Returns:
        int: sayfa indeksi
    """

    @property
    def login(self):
        """UI (User Interface) için giriş yapma sayfasının indeksini verir

        Returns:
            int: giriş sayfası"""
        return 0

    @property
    def create_account(self):
        """UI (User Interface) için hesap oluşturma sayfasının indeksini verir

        Returns:
            int: hesap oluşturma sayfas"""
        return 1

    @property
    def user(self):
        """UI (User Interface) için hesap oluşturma sayfasının indeksini verir

        Returns:
            int: kullanıcı sayfası"""
        return 2

    @property
    def admin(self):
        """UI (User Interface) için hesap oluşturma sayfasının indeksini verir

        Returns:
            int: admin sayfası"""
        return 3

    @property
    def default_page_index(self):
        """UI (User Interface) içim varsayılan sayfa indeksini verir

        Returns:
            int: varsayılan sayfa
        """
        return 0


class TOOLS:
    """Uygulamanın bir çok yerinde kullanılabileceke operastonlar

    @category: Tool Class"""

    # ****************************** STRINGS *****************************
    def str_wellcome(self, user: User) -> str:
        """Karşılama mesajını verir

        Args:
            user (User): oturum açan kullanaıcı

        Returns:
            str: karşılama mesajı
        """
        return f"Hoşgeldiniz {user.user_name}"

    # ERRORS ******************************
    @property
    def str_code_match_error(self) -> str:
        """Doğrulama kodu eşleşmiyor

        Returns:
            str: hata mesajı
        """
        return "Doğrulama kodu eşleşmiyor"

    @property
    def str_admin_cannot_deleted(self) -> str:
        """Admin yetkisi varken bir kullanıcı silinemez

        Returns:
            str: hata mesajı
        """
        return "Admin yetkisi varken bir kullanıcı silinemez"

    @property
    def str_user_not_found(self) -> str:
        """Bu kullanıcı adı ya da TC No bulunamadı

        Returns:
            str: hata mesajı
        """
        return "Bu kullanıcı adı ya da TC No bulunamadı"

    @property
    def str_user_already(self) -> str:
        """Bu kullanıcı adı ya da TC No kullanılmaktadır

        Returns:
            str: hata mesajı
        """
        return "Bu kullanıcı adı ya da TC No kullanılmaktadır"

    @property
    def str_event_type_already(self) -> str:
        """Bu etkinlik türü zaten var

        Returns:
            str: hata mesajı
        """
        return "Bu etkinlik türü zaten var"

    @property
    def str_pasword_match_error(self) -> str:
        """Şifreler eşleşmiyor!

        Returns:
            str: hata mesajı
        """
        return "Şifreler eşleşmiyor!"

    @property
    def str_username_or_password_error(self) -> str:
        """Kullanıcı adı ya da şifre yanlış

        Returns:
            str: hata mesajı
        """
        return "Kullanıcı adı ya da şifre yanlış"

    @property
    def str_information_missing(self) -> str:
        """Bilgiler eksik, lütfen bütün bilgileri giriniz

        Returns:
            str: hata mesajı
        """
        return "Bilgiler eksik, lütfen bütün bilgileri giriniz"

    @property
    def str_invalid_email(self) -> str:
        """Lütfen geçerli bir eposta adresi girin

        Returns:
            str: hata mesajı
        """
        return "Lütfen geçerli bir eposta adresi girin"

    @property
    def str_event_type_not_found(self) -> str:
        """Etkinlik tipi bulunamadı

        Returns:
            str: hata mesajı
        """
        return "Etkinlik tipi bulunamadı"

    @property
    def str_create_account_error(self) -> str:
        """Kayıt Hatası

        Returns:
            str: hata mesajı
        """
        return "Kayıt Hatası"

    @property
    def str_event_already(self) -> str:
        """Bu etkinlilk zaten kayıtlı

        Returns:
            str: hata mesajı
        """
        return "Bu etkinlilk zaten kayıtlı"

    @property
    def str_unexpected_problem(self) -> str:
        """Beklenmedik bir sorunla karşılaşıldı, lütfen daha sonra tekrar deneyin.

        Returns:
            str: hata mesajı
        """
        return "Beklenmedik bir sorunla karşılaşıldı, lütfen daha sonra tekrar deneyin."

    @property
    def str_event_description_missing(self) -> str:
        """Etkinli açıklaması eksik

        Returns:
            str: hata mesajı
        """
        return "Etkinli açıklaması eksik"

    @property
    def str_event_overlaps(self) -> str:
        """Etkinlik başka bir etkinlik ile çakışıyor

        Returns:
            str: hata mesajı
        """
        return "Etkinlik başka bir etkinlik ile çakışıyor"

    # STATES ******************************
    @property
    def str_create(self) -> str:
        """Oluşturma

        Returns:
            str: eylen tipi
        """
        return "Oluşturma"

    @property
    def str_delete(self) -> str:
        """Silme

        Returns:
            str: eylen tipi
        """
        return "Silme"

    @property
    def str_update(self) -> str:
        """Güncelleme

        Returns:
            str: eylen tipi
        """
        return "Güncelleme"

    # USER TYPES ******************************
    @property
    def admin_user(self) -> str:
        """Kullanıcı tipini verir

        Returns:
            str: kullanıcı tipi
        """
        return "0"

    @property
    def basic_user(self) -> str:
        """Kullanıcı tipini verir

        Returns:
            str: kullanıcı tipi
        """
        return "1"

    # RANDOM ******************************
    def rand_int(self) -> str:
        """Rasgele sayı üretir

        Returns:
            str: rasgele sayı
        """
        return str(randint(1000, 9999))

    # MESAGE ******************************
    def str_successful(self, islem: str) -> str:
        return f"{islem} işlemi başarılı."

    # ****************************** INTS *****************************
    # TIME ******************************
    @property
    def hour(self) -> int:
        """Güncel saat bilgisini verir

        Returns:
            int: güncel saat bilgisi
        """
        return datetime.now().hour

    @property
    def minute(self) -> int:
        """Güncel dakika bilgisini verir

        Returns:
            int: güncel dakika bilgisi
        """
        return datetime.now().minute

    # ****************************** DATETIME *****************************
    # DATE ******************************
    @property
    def time(self) -> datetime:
        """Günzel zamanı verir

        Returns:
            datetime: güncel zaman
        """
        now: str = datetime.now().strftime("%H:%M:%S")
        return datetime.strptime(now, "%H:%M:%S")

    def time_difference(self, time_now: datetime, time_event_start: str) -> float:
        """Etkinlik zamanına kaç saniye kaldığı bilgisini verir

        Args:
            time_now (datetime): güncel zaman
            time_event_start (str): etkinlik başlangıç saati

        Returns:
            float: kalan saniye
        """
        time_next: datetime = datetime.strptime(time_event_start, "%H:%M:%S")
        return (time_next - time_now).total_seconds()

    def timer_later_events(self, events: list[Event]) -> list[Event]:
        """Sonraki etkinliklerin listesini verir

        Args:
            events (list[Event]): etkinlik listesi

        Returns:
            list[Event]: etkinlik listesi
        """
        now: datetime = self.time
        event_list: list[Event] = []
        for event in events:
            start_time = datetime.strptime(event.start_time, "%H:%M:%S")
            if start_time > now:
                event_list.append(event)
        return event_list

    # ****************************** ENTITIES *****************************

    def fix_user_values(self, user: User) -> User:
        """Kullanıcı verilerinin baş-son boşluklarını temizler ve kayda hazır hale getirir

        Args:
            user (User): kullanıcı bilgileri

        Returns:
            User: kullaanıcı bilgileri
        """
        user.tc = user.tc.strip()
        user.user_name = user.user_name.upper().strip()
        user.first_name = user.first_name.upper().strip()
        user.last_name = user.last_name.upper().strip()
        user.email = user.email.strip()
        user.password = user.password.strip()
        user.address = user.address.strip()
        user.phone = user.phone.strip()

        return user

    def fix_event_values(self, event: Event) -> Event:
        """Event verilerinin baş-son boşluklarını temizler ve kayda hazır hale getirir

        Args:
            event (Event): event bilgileri

        Returns:
            EVent: event bilgileri
        """

        event.user = self.fix_user_values(event.user)
        event.date = event.date.strip()
        event.start_time = event.start_time.strip()
        event.finish_time = event.finish_time.strip()
        event.description = event.description.strip().capitalize()
        return event

    # ****************************** BOOLEAN *****************************

    def valid_user(self, user: User) -> bool:
        """Kullanıcı bilgilerinin eksiksiz olduğunu doğrular

        Args:
            user (User): kullanıcı bilgileri

        Returns:
            bool: doğruluk durumu
        """
        if (
            len(user.tc) > 0
            and len(user.user_name) > 0
            and len(user.first_name) > 0
            and len(user.last_name) > 0
            and len(user.email) > 0
            and len(user.password) > 0
            and len(user.address) > 0
            and len(user.phone) > 0
        ):
            return True
        return False

    def valid_event(self, event: Event) -> bool:
        """Etlinlik bilgilerinin eksiksiz olduğunu doğrular

        Args:
            event (Event): etkinlik bilgileri

        Returns:
            bool: doğruluk durumu
        """
        if (
            len(event.date) > 0
            and len(event.start_time) > 0
            and len(event.finish_time) > 0
            and len(event.description) > 0
            and len(event.event_type.name) > 0
            and event.event_type.id > 0
            and event.user.id > 0
        ):
            return True
        return False

    def valid_email(self, email: str) -> bool:
        """Girilen mail bilgisinin mail adresi durumunu doğrular

        Args:
            email (str): eposta adresi

        Returns:
            bool: doğruluk durumu
        """
        if "@" in email:
            return True
        return False

    def valid_str(self, str_1: str, str_2: str) -> bool:
        """Girilen iki string ifadenin birbirine eşit olup olmadığını kontrol eder

        Args:
            str_1 (str): string ifade
            str_2 (str): string ifade

        Returns:
            bool: doğruluk durumu
        """
        if str_1 == str_2:
            return True
        return False

    # ****************************** NONE *****************************

    def event_alert(self, event: Event) -> None:
        """Etkinlik başladığında / etlinkik başlamasına belirtilen dakika kaldığında bilgilendirme mesajının görüntülenmesini sağlar

        Args:
            event (Event): etkinlik bilgisi
        """
        after_time: int = event.remember_time
        description: str = event.description
        start_time: str = event.start_time
        finish_time: str = event.finish_time
        etype: str = event.event_type.name
        message: str = f"{description} etkinliği artık başladı!"
        detial: str = f"Etkinlik açıklaması: {description}\nBaşlama Saati: {start_time}\nBitiş Saati: {finish_time}\nEtkinlik Tipi: {etype}"
        if after_time > 0:
            message = f"{description} etkinliği {after_time} dakika sonra başlayacak!"
        msg_box = message_box()
        msg_box.setIcon(message_box.Information)
        msg_box.setWindowTitle("Etkinlik Hatırlatması")
        msg_box.setText(message)
        msg_box.setDetailedText(detial)
        msg_box.setStandardButtons(message_box.Ok)
        msg_box.exec()


class TABLEWIDGET:
    """Arayüzde kullanılan tablo aracı ile ilgili operasyonları verir

    @category: Tool Class"""

    # ****************************** PROPERTIES *****************************
    @property
    def labels_events(self) -> list[str]:
        """Etkinlik tablosundaki kolon isimlerini verir

        Returns:
            list[str]: kolon isimleri
        """
        return ["Başlangıç", "Bitiş", "Açıklama"]

    @property
    def labels_users(self) -> list[str]:
        """Kullanıcı tablosundaki kolon isimlerini verir

        Returns:
            list[str]: kolon isimleri
        """
        return ["Kullanıcı Adı", "Ad", "Soyad"]

    @property
    def labels_event_types(self) -> list[str]:
        """Etkinlik tipi tablosundaki kolon isimlerini verir

        Returns:
            list[str]: kolon isimleri
        """
        return ["Etkinlik Türlü"]

    # ****************************** SET TABLE *****************************
    def set_table(
        self, table: table_widget, coloum: int, row: int, labels: list[str]
    ) -> None:
        """Arayüzde kullanılan tabloları ayarlar

        Args:
            table (table_widget): ayarlanacak olan tablo
            coloum (int): kolon sayısı
            row (int): satır sayısı
            labels (list[str]): kolon isimleri
        """
        table.setColumnCount(coloum)
        table.setRowCount(row)
        table.setHorizontalHeaderLabels(labels)
        table.horizontalHeader().setSectionResizeMode(header_view.ResizeMode.Stretch)
        table.verticalHeader().setSectionResizeMode(header_view.ResizeMode.Stretch)

    # ****************************** FILL DATAS *****************************
    def fill_user_data(self, table: table_widget, dataset: list[User]) -> None:
        """Kullanıcı verilerini ilgili tablosunda gösterir

        Args:
            table (table_widget): tablo ismi
            dataset (list[User]): kullanıcılar listesi
        """
        user_values = []
        for user in dataset:
            user_values.append([user.user_name, user.first_name, user.last_name])

        for row in range(len(dataset)):
            for col in range(3):
                table.setItem(row, col, table_widget_item(f"{user_values[row][col]}"))

    def fill_evnettype_data(
        self, table: table_widget, dataset: list[EventType]
    ) -> None:
        """Etkinlik tiplerini ilgili tabloda gösterir

        Args:
            table (table_widget): tablo ismi
            dataset (list[EventType]): etkinlik tipi listesi
        """
        for row in range(len(dataset)):
            table.setItem(row, 0, table_widget_item((f"{dataset[row].name}")))

    def fill_event_data(self, table: table_widget, data: list[Event]) -> None:
        """Etkinlik verilerini ilgili tabloda gösterir

        Args:
            table (table_widget): tablo ismi
            data (list[Event]): etkinlik listesi
        """
        values = []

        for value in data:
            values.append([value.start_time, value.finish_time, value.description])

        for row in range(len(data)):
            for col in range(3):
                table.setItem(row, col, table_widget_item(f"{values[row][col]}"))
