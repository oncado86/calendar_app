from core.app import APP
from PyQt5.QtWidgets import (
    QMainWindow as main_window,
    QApplication as application,
)

from PyQt5.QtCore import QDate, QTime, QTimer
from entity.eventType import EventType
from entity.user import User
from entity.event import Event
from ui.cp_ui import Ui_MainWindow as ui_main_window


class CalendarApp(ui_main_window, main_window):
    """Uygulamanın düzgün çalışabilmesi için; PyQt5 arayüz kütüphanesinin kurulmuş olması gerekmektedir.
    Ayrıntılı bilgi için: https://pypi.org/project/PyQt5/ adresini ziyaret ediniz.
    """

    # * --------------------------------------------------------------
    # * INIT
    # * --------------------------------------------------------------
    def __init__(self) -> None:
        """
        Program açıkdığında (bu) yapıcı metot tetiklenir.
        Böylece arayüz kullanıcıya gösterilmiş olur.
        Sayısal veriler üretip ekranda kullanıcıya gösterilir.
        """
        super().__init__()

        self.apman: APP = APP()
        self.init_ui()

        self.userlist: list[User] = []
        self.event_type_list: list[EventType] = []
        self.event_list: list[Event] = []
        self.timer_event_list: list[Event] = []
        self.finished_event: Event = Event()
        self._timer()

    # * --------------------------------------------------------------
    # * TIMER
    # * --------------------------------------------------------------
    def _timer(self) -> None:
        """Zaman sayacındaki sayı kadar saniye saymayı ayarlar"""
        self.timer: QTimer = QTimer()
        self.timer_count: float = 0
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timer_counter)

    def timer_counter(self) -> None:
        """Zaman sayacındaki sayı bitene kadar geri sayım yapar"""
        if self.timer_count > 0:
            self.timer_count -= 1
            if self.timer_count <= 0:
                self.apman.tools.event_alert(self.finished_event)
                self.timer.stop()
                self.remember_events()

    def timer_start(self) -> None:
        """Geri sayımı tetikler"""
        self.timer.start()

    # * --------------------------------------------------------------
    # * INIT_UI
    # * --------------------------------------------------------------
    def init_ui(self) -> None:
        """Arayüzü ayarlar ve ekranda gösterir."""
        self.ui: ui_main_window = ui_main_window()
        self.ui.setupUi(self)

        # Arayüz fonksiyonları
        self.ui.lbl_user.setVisible(False)
        self.change_security_codes()
        self.ui.page_widget.currentChanged.connect(self.change_security_codes)

        # Butonlar
        self.button_funcs()
        self.ui.btn_log_out.setVisible(False)

        # Değişime duyarlı olanlar
        # Table
        self.ui.tw_admin_users.itemSelectionChanged.connect(self.fill_user_for_admin)
        self.ui.tw_admin_event_types.itemSelectionChanged.connect(
            self.fill_event_type_for_admin
        )
        self.ui.tw_user_events.itemSelectionChanged.connect(self.fill_event)
        self.ui.tw_admin_events.itemSelectionChanged.connect(self.fill_event)

        # Combobox
        self.ui.admin_combo_box_user_name.currentTextChanged.connect(self.fill_event)

        # Calender
        self.ui.user_calendar.selectionChanged.connect(self.fill_event)
        self.ui.admin_calendar.selectionChanged.connect(self.fill_event)

        # Event Start Time Change: USER
        self.ui.user_te_start_time.timeChanged.connect(self.start_time_change)
        # Event Finish Time Change: USER
        self.ui.user_te_finish_time.timeChanged.connect(self.finish_time_change)

        # Event Start Time Change: ADMIN
        self.ui.admin_te_start_time.timeChanged.connect(self.start_time_change)
        # Event Finish Time Change: ADMIN
        self.ui.admin_te_finish_time.timeChanged.connect(self.finish_time_change)

        # Line Edit
        self.ui.le_admin_search_user.textChanged.connect(self.get_user_list)
        self.ui.le_admin_search_event_type.textChanged.connect(self.get_event_type_list)
        self.ui.admin_le_description_search.textChanged.connect(self.get_event_list)
        self.ui.user_le_description_search.textChanged.connect(self.get_event_list)

        # Arayüzü ekranda göster
        self.show()

    ##################################################################
    # * --------------------------------------------------------------
    # * FILLS
    # * --------------------------------------------------------------
    # FILL USER FOR ADMIN
    def fill_user_for_admin(self) -> None:
        try:
            if len(self.userlist) > 0 and (
                0 <= self.ui.tw_admin_users.currentRow() <= len(self.userlist)
            ):
                user: User = self.userlist[self.ui.tw_admin_users.currentRow()]
                self.ui.le_admin_user_account_tc.setText(user.tc)
                self.ui.le_admin_user_account_user_name.setText(user.user_name)
                self.ui.le_admin_user_account_first_name.setText(user.first_name)
                self.ui.le_admin_user_account_last_name.setText(user.last_name)
                self.ui.le_admin_user_account_password.setText(user.password)
                self.ui.le_admin_user_account_phone.setText(user.phone)
                self.ui.le_admin_user_account_email.setText(user.email)
                self.ui.le_admin_user_account_address.setPlainText(user.address)
        except Exception:
            self.show_statusbar_message(self.apman.tools.str_unexpected_problem)
        finally:
            self.change_security_codes()

    # FILL EVENT TYPE FOR ADMIN
    def fill_event_type_for_admin(self) -> None:
        self.ui.le_admin_event_type_name.clear()
        try:
            if len(self.event_type_list) > 0 and (
                0
                <= self.ui.tw_admin_event_types.currentRow()
                <= len(self.event_type_list)
            ):
                etype: EventType = self.event_type_list[
                    self.ui.tw_admin_event_types.currentRow()
                ]
                self.ui.le_admin_event_type_name.setText(etype.name)
                self.ui.le_admin_search_event_type.setFocus()
        except Exception:
            self.show_statusbar_message(self.apman.tools.str_unexpected_problem)

    # FILL EVENT
    def fill_event(self):
        description_search = self.ui.user_le_description_search
        calendar = self.ui.user_calendar
        combo_box_event_type = self.ui.user_combo_box_event_type
        description = self.ui.user_le_description
        te_start_time = self.ui.user_te_start_time
        te_finish_time = self.ui.user_te_finish_time
        selected_row: int = self.ui.tw_user_events.currentRow()
        remember_time = self.ui.user_combo_box_remember_time

        if self.apman.user.user_type == self.apman.tools.admin_user:
            description_search = self.ui.admin_le_description_search
            calendar = self.ui.admin_calendar
            selected_row = self.ui.tw_admin_events.currentRow()
            combo_box_event_type = self.ui.admin_combo_box_event_type
            description = self.ui.admin_le_description
            te_start_time = self.ui.admin_te_start_time
            te_finish_time = self.ui.admin_te_finish_time
            remember_time = self.ui.admin_combo_box_remember_time

        description_search.clear()

        self.get_event_list()
        self.timer_event_list = self.apman.tools.timer_later_events(self.event_list)
        self.remember_events()

        try:
            if len(self.event_list) > 0 and (0 <= selected_row <= len(self.event_list)):
                event: Event = self.event_list[selected_row]
                date: list[str] = event.date.split("-")
                year, mount, day = int(date[0]), int(date[1]), int(date[2])
                calendar.setSelectedDate(QDate(year, mount, day))
                combo_box_event_type.setCurrentText(event.event_type.name)
                description.setText(event.description)

                start_time: list[str] = (event.start_time).split(":")
                finis_time: list[str] = (event.finish_time).split(":")
                start_hour, start_minute = int(start_time[0]), int(start_time[1])
                finis_hour, finis_minute = int(finis_time[0]), int(finis_time[1])
                te_start_time.setTime(QTime(start_hour, start_minute))
                te_finish_time.setTime(QTime(finis_hour, finis_minute))
                remember_time.setCurrentText(str(event.remember_time))

        except Exception:
            self.show_statusbar_message(self.apman.tools.str_unexpected_problem)

    ##################################################################
    # * --------------------------------------------------------------
    # * GETS
    # * --------------------------------------------------------------
    # GET USER LIST
    def get_user_list(self) -> None:
        """Kayıtlı kullanıcıların bilgilerini getirip ilgili tabloya yükler"""
        self.userlist.clear()
        self.ui.le_admin_user_account_tc.clear()
        self.ui.le_admin_user_account_user_name.clear()
        self.ui.le_admin_user_account_first_name.clear()
        self.ui.le_admin_user_account_last_name.clear()
        self.ui.le_admin_user_account_password.clear()
        self.ui.le_admin_user_account_password_conf.clear()
        self.ui.le_admin_user_account_phone.clear()
        self.ui.le_admin_user_account_email.clear()
        self.ui.le_admin_user_account_address.clear()

        self.userlist = self.apman.managers.user.get_all_users(
            self.ui.le_admin_search_user.text()
        )

        self.ui.tw_admin_users.clear()
        self.apman.table.set_table(
            self.ui.tw_admin_users,
            3,
            len(self.userlist),
            self.apman.table.labels_users,
        )

        self.apman.table.fill_user_data(self.ui.tw_admin_users, self.userlist)

        self.ui.admin_combo_box_user_name.clear()
        for user in self.userlist:
            self.ui.admin_combo_box_user_name.addItem(user.user_name)

    # GET EVENT TYPE LIST
    def get_event_type_list(self) -> None:
        """Sistemdeki etkinlik tipi bilgileirini getirip ilgili tabloya yükler"""
        self.event_type_list.clear()
        self.ui.le_admin_event_type_name.clear()
        self.event_type_list = self.apman.managers.event_type.get_all_event_types(
            self.ui.le_admin_search_event_type.text()
        )

        self.ui.tw_admin_event_types.clear()
        self.apman.table.set_table(
            self.ui.tw_admin_event_types,
            1,
            len(self.event_type_list),
            self.apman.table.labels_event_types,
        )

        self.apman.table.fill_evnettype_data(
            self.ui.tw_admin_event_types, self.event_type_list
        )

        event_type_names: list[str] = []
        event_cb = self.ui.user_combo_box_event_type
        if self.apman.user.user_type == self.apman.tools.admin_user:
            event_cb = self.ui.admin_combo_box_event_type
        for events in self.event_type_list:
            event_type_names.append(events.name)
        event_cb.clear()
        event_cb.addItems(event_type_names)

    # GET EVENT
    def get_event_list(self) -> None:
        """Sistemdeki etkinlikleri getirip ilgili tabloya yükler."""
        self.event_list.clear()
        text: str = self.ui.user_le_description_search.text()
        user: User = self.apman.user
        date: str = str(self.ui.user_calendar.selectedDate().toPyDate())
        description = self.ui.user_le_description
        start_time = self.ui.user_te_start_time
        finish_time = self.ui.user_te_finish_time
        table = self.ui.tw_user_events

        if self.apman.user.user_type == self.apman.tools.admin_user:
            text = self.ui.admin_le_description_search.text()
            date = str(self.ui.admin_calendar.selectedDate().toPyDate())
            user_name: str = self.ui.admin_combo_box_user_name.currentText()
            user = self.apman.managers.user.get_user(
                self.apman.managers.user.get_user_id(user_name)
            )

            description = self.ui.admin_le_description
            start_time = self.ui.admin_te_start_time
            finish_time = self.ui.admin_te_finish_time
            table = self.ui.tw_admin_events

        description.clear()
        start_time.setTime(QTime(0, 0))
        finish_time.setTime(QTime(0, 1))

        self.event_list = self.apman.managers.event.get_all_events(user, date, text)
        table.clear()

        self.apman.table.set_table(
            table,
            3,
            len(self.event_list),
            self.apman.table.labels_events,
        )

        self.apman.table.fill_event_data(table, self.event_list)

    ##################################################################
    # * --------------------------------------------------------------
    # * CREATE
    # * --------------------------------------------------------------
    # CREATE ACCOUNT
    def create_acc(self, values: tuple[User, str, str, str]) -> None:
        """Sisteme kayıt olmayı sağlar"""

        user, user_pass_conf, code, code_conf = values

        if not self.apman.tools.valid_user(user):
            self.show_statusbar_message(self.apman.tools.str_information_missing)
            self.change_security_codes()
            self.clear_code_valid()
        elif not self.apman.tools.valid_email(user.email):
            self.show_statusbar_message(self.apman.tools.str_invalid_email)
            self.change_security_codes()
            self.clear_code_valid()

            self.ui.le_user_account_email.setFocus()
            self.ui.le_admin_user_account_email.setFocus()

        elif not self.apman.tools.valid_str(user.password, user_pass_conf):
            self.show_statusbar_message(self.apman.tools.str_pasword_match_error)
            self.change_security_codes()
            self.clear_code_valid()

            self.ui.le_user_account_password.setFocus()
            self.ui.le_user_account_password.selectAll()
            self.ui.le_admin_user_account_password.setFocus()
            self.ui.le_admin_user_account_password.selectAll()

        elif not self.apman.tools.valid_str(code, code_conf):
            self.show_statusbar_message(self.apman.tools.str_code_match_error)
            self.change_security_codes()
            self.clear_code_valid()

            self.ui.le_user_account_code_valid.setFocus()
            self.ui.le_user_account_code_valid.selectAll()
            self.ui.le_admin_user_account_code_valid.setFocus()
            self.ui.le_admin_user_account_code_valid.selectAll()

        else:
            user = self.apman.tools.fix_user_values(user)
            if not self.apman.managers.user.is_user(user):
                # -------->> CREATE ACCOUNT <<--------
                user.user_type = self.apman.tools.basic_user
                if self.apman.managers.user.insert(user):
                    self.show_statusbar_message(
                        self.apman.tools.str_successful(self.apman.tools.str_create)
                    )
                    self.change_security_codes()
                    self.clear_create_account_screen()
                else:
                    self.show_statusbar_message(
                        self.apman.tools.str_create_account_error
                    )
                    self.change_security_codes()
                    self.clear_code_valid()
            else:
                self.show_statusbar_message(self.apman.tools.str_user_already)
                self.change_security_codes()
                self.clear_code_valid()

                self.ui.le_user_account_tc.setFocus()
                self.ui.le_user_account_tc.selectAll()
                self.ui.le_admin_user_account_tc.setFocus()
                self.ui.le_admin_user_account_tc.selectAll()

    # CREATE EVENT TYPE
    def create_event_type(self) -> None:
        """Sisteme etkinlik tipi kaydetmeyi sağlar"""
        name: str = self.ui.le_admin_event_type_name.text()
        if not self.apman.managers.event_type.is_event_type(name) and len(name) > 0:
            etype: EventType = EventType()
            etype.name = name
            self.apman.managers.event_type.insert(etype)
            self.get_event_type_list()
            self.show_statusbar_message(
                self.apman.tools.str_successful(self.apman.tools.str_create)
            )
            self.ui.le_admin_event_type_name.clear()

    # CREATE EVENT
    def create_event(self):
        event: Event = Event()
        event_date = self.ui.user_calendar
        event_description = self.ui.user_le_description
        start_time = self.ui.user_te_start_time
        finish_time = self.ui.user_te_finish_time
        cb_et_name = self.ui.user_combo_box_event_type
        event.user = self.apman.user
        event.remember_time = int(self.ui.user_combo_box_remember_time.currentText())

        if self.apman.user.user_type == self.apman.tools.admin_user:
            event_date = self.ui.admin_calendar
            event_description = self.ui.admin_le_description
            start_time = self.ui.admin_te_start_time
            finish_time = self.ui.admin_te_finish_time
            cb_et_name = self.ui.admin_combo_box_event_type
            selected_user_name = self.ui.admin_combo_box_user_name.currentText()
            user_id = self.apman.managers.user.get_user_id(selected_user_name)
            event.user = self.apman.managers.user.get_user(user_id)
            event.remember_time = int(
                self.ui.admin_combo_box_remember_time.currentText()
            )

        event.date = str(event_date.selectedDate().toPyDate())
        event.description = event_description.text()
        event.start_time = f"{start_time.text()}:00"
        event.finish_time = f"{finish_time.text()}:00"
        et_name: str = cb_et_name.currentText()
        et_id: int = self.apman.managers.event_type.get_event_type_id(et_name)
        event.event_type.name = et_name
        event.event_type.id = et_id

        if not self.apman.tools.valid_event(event):
            self.show_statusbar_message(self.apman.tools.str_information_missing)
            self.ui.user_le_description.setFocus()
        else:
            event = self.apman.tools.fix_event_values(event)
            if not self.apman.managers.event.is_event(event):
                if self.apman.managers.event.insert(event):
                    self.show_statusbar_message(
                        self.apman.tools.str_successful(self.apman.tools.str_create)
                    )
                    self.timer.stop()
                    self.fill_event()

                    self.ui.le_admin_event_type_name.setFocus()

                else:
                    self.show_statusbar_message(self.apman.tools.str_unexpected_problem)
            else:
                self.show_statusbar_message(self.apman.tools.str_event_already)

    ##################################################################
    # * --------------------------------------------------------------
    # * UPDATE
    # * --------------------------------------------------------------
    # UPDATE ACCOUNT
    def update_acc(self, values: tuple[User, str, str, str]) -> None:
        """Sistemeki bir kullanıcının bilgilerini güncellemeyi sağlar

        Args:
            values (tuple[User, str, str, str): kullanıcı ve kayıt bilgileri"""
        user, user_pass_conf, code, code_conf = values

        if not self.apman.tools.valid_user(user):
            self.show_statusbar_message(self.apman.tools.str_information_missing)
            self.change_security_codes()
            self.clear_code_valid()
        elif not self.apman.tools.valid_email(user.email):
            self.show_statusbar_message(self.apman.tools.str_invalid_email)
            self.change_security_codes()
            self.clear_code_valid()

            self.ui.le_user_account_email.setFocus()
            self.ui.le_admin_user_account_email.setFocus()

        elif not self.apman.tools.valid_str(user.password, user_pass_conf):
            self.show_statusbar_message(self.apman.tools.str_pasword_match_error)
            self.change_security_codes()
            self.clear_code_valid()

            self.ui.le_user_account_password.setFocus()
            self.ui.le_user_account_password.selectAll()
            self.ui.le_admin_user_account_password.setFocus()
            self.ui.le_admin_user_account_password.selectAll()

        elif not self.apman.tools.valid_str(code, code_conf):
            self.show_statusbar_message(self.apman.tools.str_code_match_error)
            self.change_security_codes()

            self.ui.le_user_account_code_valid.setFocus()
            self.ui.le_user_account_code_valid.selectAll()
            self.ui.le_admin_user_account_code_valid.setFocus()
            self.ui.le_admin_user_account_code_valid.selectAll()

        else:
            user = self.apman.tools.fix_user_values(user)
            if self.apman.managers.user.is_user(user):
                # -------->> UPDATE ACCOUNT <<--------
                if self.apman.managers.user.update(user):
                    self.show_statusbar_message(
                        self.apman.tools.str_successful(self.apman.tools.str_update)
                    )
                    self.change_security_codes()
                    self.clear_code_valid()
                    self.ui.le_user_account_password_conf.clear()
                    self.ui.le_admin_user_account_password_conf.clear()
                    self.get_user_list()

                else:
                    self.show_statusbar_message(self.apman.tools.str_unexpected_problem)
                    self.change_security_codes()
                    self.clear_code_valid()
            else:
                self.show_statusbar_message(self.apman.tools.str_user_not_found)
                self.change_security_codes()
                self.clear_code_valid()

    # UPDATE EVENT
    def update_event(self, event: Event) -> None:
        """Sitemdeki bir etkinliği güncellemeyi sağlar

        Args:
            event (Event): etkinlik bilgileri
        """
        if len(event.description) == 0:
            self.show_statusbar_message(self.apman.tools.str_event_description_missing)
            self.ui.user_le_description.setFocus()
        else:
            if self.apman.managers.event.is_event(event):
                # -------->> UPDATE EVENT <<--------
                if self.apman.managers.event.update(event):
                    self.show_statusbar_message(
                        self.apman.tools.str_successful(self.apman.tools.str_update)
                    )
                    self.fill_event()
                else:
                    self.show_statusbar_message(self.apman.tools.str_unexpected_problem)
            else:
                self.show_statusbar_message(self.apman.tools.str_event_overlaps)

    # UPDATE EVENT TYPE
    def update_event_type(self) -> None:
        """Sistemdeki bir etkinlik tipini güncellemeyi sağlar"""
        etype_count: int = len(self.event_type_list)
        name: str = self.ui.le_admin_event_type_name.text()
        cur_row: int = self.ui.tw_admin_event_types.currentRow()

        if etype_count > 0 and len(name) > 0 and cur_row >= 0:
            etype = self.event_type_list[cur_row]
            if (
                self.apman.managers.event_type.is_event_type(etype.name)
                and len(name) > 0
            ):
                etype.name = name
                self.apman.managers.event_type.update(etype)
                self.get_event_type_list()
                self.show_statusbar_message(
                    self.apman.tools.str_successful(self.apman.tools.str_update)
                )
            else:
                self.show_statusbar_message(self.apman.tools.str_unexpected_problem)
            self.ui.le_admin_event_type_name.clear()

    ##################################################################
    # * --------------------------------------------------------------
    # * DELETE
    # * --------------------------------------------------------------
    # DELETE EVENT TYPE
    def delete_event_type(self) -> None:
        """Sistemdeki bir etkinlik tipini silmeyi sağlar"""
        etype_count: int = len(self.event_type_list)
        name: str = self.ui.le_admin_event_type_name.text()
        cur_row: int = self.ui.tw_admin_event_types.currentRow()

        if etype_count > 0 and len(name) > 0 and cur_row >= 0:
            etype: EventType = self.event_type_list[cur_row]
            if self.apman.managers.event_type.delete(etype):
                self.show_statusbar_message(
                    self.apman.tools.str_successful(self.apman.tools.str_delete)
                )
                self.ui.le_admin_event_type_name.clear()
                self.get_event_type_list()
            else:
                self.show_statusbar_message(self.apman.tools.str_event_type_not_found)

    # DELETE EVENT
    def delete_event(self) -> None:
        """Sistemden bir etkinlik silmeyi sağlar"""
        selected_row: int = self.ui.tw_user_events.currentRow()
        if self.apman.user.user_type == self.apman.tools.admin_user:
            selected_row = self.ui.tw_admin_events.currentRow()

        event: Event = self.event_list[selected_row]

        if self.apman.managers.event.delete(event):
            self.show_statusbar_message(
                self.apman.tools.str_successful(self.apman.tools.str_delete)
            )
            self.fill_event()
        else:
            self.show_statusbar_message(
                self.apman.tools.str_successful(self.apman.tools.str_unexpected_problem)
            )

    # DELETE USER
    def delete_user(self) -> None:
        """Sistemden bir kullanıcı silmeyi sağlar"""
        selected_row: int = self.ui.tw_admin_users.currentRow()
        user_count: int = len(self.userlist)
        code: str = self.ui.le_admin_user_account_code.text()
        code_conf: str = self.ui.le_admin_user_account_code_valid.text()

        if user_count > 0 and selected_row >= 0:
            user: User = self.userlist[selected_row]
            if not self.apman.tools.valid_str(code, code_conf):
                self.show_statusbar_message(self.apman.tools.str_code_match_error)
                self.change_security_codes()
                self.ui.le_admin_user_account_code.setFocus()
            elif self.apman.managers.user.delete(user):
                self.show_statusbar_message(
                    self.apman.tools.str_successful(self.apman.tools.str_delete)
                )
                self.get_user_list()
            else:
                self.show_statusbar_message(
                    self.apman.tools.str_successful(
                        self.apman.tools.str_unexpected_problem
                    )
                )

    ##################################################################
    # * --------------------------------------------------------------
    # * GET ENTITIES VALUES
    # * --------------------------------------------------------------
    # USER VALUES
    def user_values(self) -> tuple[User, str, str, str]:
        user: User = User()
        user_pass_conf: str = ""
        code: str = ""
        code_conf: str = ""

        if self.apman.user.user_type == self.apman.tools.admin_user:
            user.id = self.userlist[self.ui.tw_user_events.currentRow()].id
            user.tc = self.ui.le_admin_user_account_tc.text()
            user.user_name = self.ui.le_admin_user_account_user_name.text()
            user.first_name = self.ui.le_admin_user_account_first_name.text()
            user.last_name = self.ui.le_admin_user_account_last_name.text()
            user.email = self.ui.le_admin_user_account_email.text()
            user.password = self.ui.le_admin_user_account_password.text()
            user_pass_conf = self.ui.le_admin_user_account_password_conf.text()
            user.phone = self.ui.le_admin_user_account_phone.text()
            user.address = self.ui.le_admin_user_account_address.toPlainText()
            code = self.ui.le_admin_user_account_code.text()
            code_conf = self.ui.le_admin_user_account_code_valid.text()

        elif self.apman.user.user_type == self.apman.tools.basic_user:
            user.id = self.apman.user.id
            user.tc = self.ui.le_user_account_tc.text()
            user.user_name = self.ui.le_user_account_user_name.text()
            user.first_name = self.ui.le_user_account_first_name.text()
            user.last_name = self.ui.le_user_account_last_name.text()
            user.email = self.ui.le_user_account_email.text()
            user.password = self.ui.le_user_account_password.text()
            user_pass_conf = self.ui.le_user_account_password_conf.text()
            user.phone = self.ui.le_user_account_phone.text()
            user.address = self.ui.le_user_account_address.toPlainText()
            code = self.ui.le_user_account_code.text()
            code_conf = self.ui.le_user_account_code_valid.text()

        else:
            user.tc = self.ui.le_creat_acc_tc.text()
            user.user_name = self.ui.le_creat_acc_user_name.text()
            user.first_name = self.ui.le_creat_acc_first_name.text()
            user.last_name = self.ui.le_creat_acc_last_name.text()
            user.email = self.ui.le_creat_acc_email.text()
            user.password = self.ui.le_creat_acc_password.text()
            user_pass_conf = self.ui.le_creat_acc_password_conf.text()
            user.phone = self.ui.le_creat_acc_phone.text()
            user.address = self.ui.le_creat_acc_address.toPlainText()

            code = self.ui.le_creat_acc_code.text()
            code_conf = self.ui.le_creat_acc_code_valid.text()

        return user, user_pass_conf, code, code_conf

    # EVENT VALUES
    def event_values(self) -> Event:
        event: Event = Event()
        current_row: int = self.ui.tw_user_events.currentRow()
        calendar = self.ui.user_calendar
        event_type_name: str = self.ui.user_combo_box_event_type.currentText()
        event_description: str = self.ui.user_le_description.text()
        start_time = str(self.ui.user_te_start_time.time().toPyTime())
        finish_time = str(self.ui.user_te_finish_time.time().toPyTime())
        remember_time = self.ui.user_combo_box_remember_time

        if self.apman.user.user_type == self.apman.tools.admin_user:
            current_row = self.ui.tw_admin_events.currentRow()
            calendar = self.ui.admin_calendar
            event_type_name = self.ui.admin_combo_box_event_type.currentText()
            event_description = self.ui.admin_le_description.text()
            start_time = str(self.ui.admin_te_start_time.time().toPyTime())
            finish_time = str(self.ui.admin_te_finish_time.time().toPyTime())
            remember_time = self.ui.admin_combo_box_remember_time

        event.id = self.event_list[current_row].id
        event.date = str(calendar.selectedDate().toPyDate())
        event.event_type.name = event_type_name
        event.event_type.id = self.apman.managers.event_type.get_event_type_id(
            event.event_type.name
        )
        event.description = event_description
        event.start_time = start_time
        event.finish_time = finish_time
        event.remember_time = int(remember_time.currentText())

        return event

    ##################################################################
    # * --------------------------------------------------------------
    # * BUTTON FONCS
    # * --------------------------------------------------------------
    def button_funcs(self) -> None:
        """Uygulama içindeki butonların işlevselliğinin ayarlanması"""

        # LOGIN
        self.ui.btn_login_login.clicked.connect(self.login)

        # LOGOUT
        self.ui.btn_log_out.clicked.connect(self.logout)

        # GO TO CREATE ACCOUNT
        self.ui.btn_login_create_acc.clicked.connect(
            lambda: self.ui.page_widget.setCurrentIndex(self.apman.pages.create_account)
        )

        # CANCEL CREATE ACCOUNT
        self.ui.btn_creat_acc_back.clicked.connect(
            lambda: self.ui.page_widget.setCurrentIndex(self.apman.pages.login)
        )

        # CREATE
        # CREATE ACCOUNT : USER
        self.ui.btn_creat_acc_save.clicked.connect(
            lambda: self.create_acc(self.user_values())
        )
        # CREATE EVENT TYPE: ADMIN
        self.ui.btn_admin_event_type_add.clicked.connect(self.create_event_type)
        # CREATE EVENT : USER
        self.ui.btn_user_add_event.clicked.connect(self.create_event)
        # CREATE EVENT : ADMIN
        self.ui.btn_admin_add_event.clicked.connect(self.create_event)

        # UPDATE
        # UPDATE EVENT: USER
        self.ui.btn_user_update_event.clicked.connect(
            lambda: self.update_event(self.event_values())
        )
        # UPDATE EVENT: ADMIN
        self.ui.btn_admin_update_event.clicked.connect(
            lambda: self.update_event(self.event_values())
        )
        # UPDATE ACCOUNT: USER VALUES
        self.ui.btn_user_account_save.clicked.connect(
            lambda: self.update_acc(self.user_values())
        )
        # UPDATE USER ACCOUNT: ADMIN
        self.ui.btn_admin_user_account_save.clicked.connect(
            lambda: self.update_acc(self.user_values())
        )
        # UPDATE EVENT TYPE: ADMIN
        self.ui.btn_admin_event_type_update.clicked.connect(self.update_event_type)

        # DELETE
        # DELETE EVENT : USER
        self.ui.btn_user_delete_event.clicked.connect(self.delete_event)
        # DELETE EVENT : ADMIN
        self.ui.btn_admin_delete_event.clicked.connect(self.delete_event)
        # DELETE EVENT TYPE: ADMIN
        self.ui.btn_admin_event_type_delete.clicked.connect(self.delete_event_type)
        # DELETE USER: ADMIN
        self.ui.btn_admin_user_account_del.clicked.connect(self.delete_user)

    ##################################################################
    # * --------------------------------------------------------------
    # * LOGIN-LOGOUT FONCS
    # * --------------------------------------------------------------
    def login(self) -> None:
        """Sisteme giriş yapmayı sağlar"""
        log_user: User = User()
        log_user.user_name = self.ui.le_login_user_name.text()
        log_user.password = self.ui.le_login_passport.text()

        code: str = self.ui.le_login_code.text()
        code_valid: str = self.ui.le_login_code_valid.text()

        if not (
            len(log_user.user_name) >= 1
            or len(log_user.password) >= 1
            or len(code_valid) >= 1
        ):
            self.ui.statusbar.showMessage(
                self.apman.tools.str_information_missing, 3000
            )
            self.change_security_codes()
        elif not self.apman.tools.valid_str(code, code_valid):
            self.show_statusbar_message(self.apman.tools.str_code_match_error)
            self.change_security_codes()
            self.ui.le_login_code_valid.setFocus()
            self.ui.le_login_code_valid.selectAll()
        else:
            log_user = self.apman.tools.fix_user_values(log_user)
            if self.apman.managers.user.is_user(log_user):
                get_user = self.apman.managers.user.get_user(
                    self.apman.managers.user.get_user_id(log_user.user_name)
                )
                if self.apman.tools.valid_str(
                    get_user.user_name, log_user.user_name
                ) and self.apman.tools.valid_str(get_user.password, log_user.password):
                    # -------->> LOGIN <<--------
                    self.apman.user = get_user
                    self.apman.user.id = self.apman.managers.user.get_user_id(
                        get_user.user_name
                    )
                    self.clear_login_screen()
                    self.change_security_codes()
                    self.show_statusbar_message(
                        self.apman.tools.str_wellcome(self.apman.user)
                    )
                    self.ui.btn_log_out.setVisible(True)
                    self.ui.lbl_user.setText(get_user.user_name)
                    self.ui.lbl_user.setVisible(True)
                    # ----------------------------

                    self.go_users_page(get_user)
                else:
                    self.show_statusbar_message(
                        self.apman.tools.str_username_or_password_error
                    )
                    self.change_security_codes()
                    self.clear_code_valid()
            else:
                self.show_statusbar_message(self.apman.tools.str_user_not_found)
                self.ui.btn_login_create_acc.setFocus()
                self.change_security_codes()
                self.clear_code_valid()

    def logout(self) -> None:
        self.ui.page_widget.setCurrentIndex(self.apman.pages.login)
        self.ui.btn_log_out.setVisible(False)
        self.ui.tool_box_user.setCurrentIndex(self.apman.pages.default_page_index)
        self.ui.tool_box_admin.setCurrentIndex(self.apman.pages.default_page_index)
        self.ui.lbl_user.clear()
        self.ui.lbl_user.setVisible(False)
        self.apman.user = User()

    def go_users_page(self, user: User) -> None:
        """Sisteme giriş yapan kullanıcının ana sayfasına gitmesini sağlar

        Args:
            user (User): kullanıcı bilgileri
        """
        self.get_event_type_list()

        finis_time = QTime(self.apman.tools.hour, self.apman.tools.minute + 2)
        start_time = QTime(QTime(self.apman.tools.hour, self.apman.tools.minute + 1))

        if user.user_type == self.apman.tools.admin_user:
            self.ui.page_widget.setCurrentIndex(self.apman.pages.admin)
            self.get_user_list()

            self.ui.admin_te_finish_time.setTime(finis_time)
            self.ui.admin_te_start_time.setTime(start_time)

            self.fill_event()
            self.remember_events()

        else:
            self.ui.page_widget.setCurrentIndex(self.apman.pages.user)
            self.ui.le_user_account_tc.setText(user.tc)
            self.ui.le_user_account_user_name.setText(user.user_name)
            self.ui.le_user_account_first_name.setText(user.first_name)
            self.ui.le_user_account_last_name.setText(user.last_name)
            self.ui.le_user_account_password.setText(user.password)
            self.ui.le_user_account_phone.setText(user.phone)
            self.ui.le_user_account_email.setText(user.email)
            self.ui.le_user_account_address.setPlainText(user.address)
            self.ui.user_te_finish_time.setTime(finis_time)
            self.ui.user_te_start_time.setTime(start_time)
            self.fill_event()
            self.remember_events()

    ##################################################################
    # * --------------------------------------------------------------
    # * ClEAR SCREEN FONCS
    # * --------------------------------------------------------------
    def clear_create_account_screen(self) -> None:
        """Hesap oluşturma ekranını temizler"""
        self.ui.le_creat_acc_tc.clear()
        self.ui.le_creat_acc_user_name.clear()
        self.ui.le_creat_acc_first_name.clear()
        self.ui.le_creat_acc_last_name.clear()
        self.ui.le_creat_acc_email.clear()
        self.ui.le_creat_acc_password.clear()
        self.ui.le_creat_acc_password_conf.clear()
        self.ui.le_creat_acc_phone.clear()
        self.ui.le_creat_acc_address.clear()
        self.ui.le_creat_acc_code_valid.clear()

    def clear_code_valid(self) -> None:
        self.ui.le_login_code_valid.clear()
        self.ui.le_creat_acc_code_valid.clear()
        self.ui.le_user_account_code_valid.clear()
        self.ui.le_admin_user_account_code_valid.clear()

    def clear_login_screen(self) -> None:
        """Giriş ekranını temizler"""
        self.ui.le_login_code_valid.clear()
        self.ui.le_creat_acc_code_valid.clear()
        self.ui.le_login_passport.clear()
        self.ui.le_login_user_name.clear()

    ##################################################################
    # * --------------------------------------------------------------
    # * CHANGE FONCS
    # * --------------------------------------------------------------
    def start_time_change(self) -> None:
        """Etkinlikler için başlangıç-bitiş zamanlarının uyumlu olmasını sağlar"""
        start_time: QTime = self.ui.user_te_start_time.time()
        finish_time: QTime = self.ui.user_te_finish_time.time()
        te_start_time = self.ui.user_te_start_time
        te_finish_time = self.ui.user_te_finish_time

        if self.apman.user.user_type == self.apman.tools.admin_user:
            start_time = self.ui.admin_te_start_time.time()
            finish_time = self.ui.admin_te_finish_time.time()
            te_start_time = self.ui.admin_te_start_time
            te_finish_time = self.ui.admin_te_finish_time

        if start_time.hour() >= finish_time.hour():
            te_finish_time.setTime(QTime(start_time.hour(), finish_time.minute()))

        if (
            start_time.minute() >= finish_time.minute()
            and start_time.hour() >= finish_time.hour()
        ):
            te_start_time.setTime(QTime(finish_time.hour(), finish_time.minute() - 1))

    def finish_time_change(self) -> None:
        """Etkinlikler için başlangıç-bitiş zamanlarının uyumlu olmasını sağlar"""
        start_time: QTime = self.ui.user_te_start_time.time()
        finish_time: QTime = self.ui.user_te_finish_time.time()
        te_start_time = self.ui.user_te_start_time

        if self.apman.user.user_type == self.apman.tools.admin_user:
            start_time = self.ui.admin_te_start_time.time()
            finish_time = self.ui.admin_te_finish_time.time()
            te_start_time = self.ui.admin_te_start_time

        if start_time.hour() >= finish_time.hour():
            te_start_time.setTime(QTime(finish_time.hour(), start_time.minute()))

        if (
            start_time.minute() >= finish_time.minute()
            and start_time.hour() >= finish_time.hour()
            and not (
                start_time.hour() == finish_time.hour()
                and start_time.minute() == 0
                and finish_time.minute() == 1
            )
        ):
            te_start_time.setTime(QTime(finish_time.hour(), finish_time.minute() - 1))

    def change_security_codes(self) -> None:
        """Doğrulama kodlarını temizler"""
        self.ui.le_login_code.setText(self.apman.tools.rand_int())
        self.ui.le_creat_acc_code.setText(self.apman.tools.rand_int())
        self.ui.le_user_account_code.setText(self.apman.tools.rand_int())
        self.ui.le_admin_user_account_code.setText(self.apman.tools.rand_int())

    ##################################################################
    # * --------------------------------------------------------------
    # * STATUSBAR MESSAGE FONC
    # * --------------------------------------------------------------
    def show_statusbar_message(self, message: str) -> None:
        """Uygulama içi etkinlikler hakkında durum çubuğunda bilgi mesajları verir

            Args:
        message (str): bilgilendirme mesajı"""
        self.ui.statusbar.showMessage(message, 3000)

    ##################################################################
    # * --------------------------------------------------------------
    # * REMEMBER EVENT FONC
    # * --------------------------------------------------------------
    def remember_events(self) -> None:
        """Uygulama açıldığında ya da etkinlikler ile ilgili işlemler yapıldığında,
        güncel zamana en yakın etkinliğin hatırlatılmasını tetikler
        """
        if len(self.timer_event_list) > 0:
            self.finished_event = self.timer_event_list.pop(0)
            now_time = self.apman.tools.time
            event_start = self.finished_event.start_time
            time_difference = self.apman.tools.time_difference(now_time, event_start)
            self.timer_count = time_difference - (
                self.finished_event.remember_time * 60
            )
            self.timer_start()


##################################################################
# * --------------------------------------------------------------
# * APP RUN
# * --------------------------------------------------------------
if __name__ == "__main__":
    import sys

    app = application(sys.argv)
    win = CalendarApp()
    win.show()
    sys.exit(app.exec_())
