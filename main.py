import json
import os
import sys
from datetime import datetime
from tkinter.messagebox import OKCANCEL

import requests
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTreeWidgetItem, QMessageBox, QDialog
from googleapiclient.errors import HttpError

from calendar_api import CalendarWorker
from timetable import TimeTable

from uis.MainWindow import Ui_MainWindow
from uis.PushToCalendar import Ui_Dialog

class Scheduler(QMainWindow):
    def __init__(self):
        super(Scheduler, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.treeWidget.itemClicked.connect(self.on_item_clicked)
        self.ui.buttonPushSetup.clicked.connect(self.on_button_push_to_calendar_clicked)

    def fill_table(self, timetable: TimeTable):
        fw, sw = timetable.parse_timetable(push=False, until='', calendar_id='', calendar_worker=None)

        for day in range(0, 6):
            for lesson in range(0, 6):
                self.ui.timeTable1.setItem(lesson, day, QTableWidgetItem(fw[lesson + day*6]))
                self.ui.timeTable2.setItem(lesson, day, QTableWidgetItem(sw[lesson + day*6]))

        self.ui.timeTable1.resizeRowsToContents()
        self.ui.timeTable2.resizeRowsToContents()

    def fill_tree(self, data, parent_item=None):
        for key, value in data.items():
            if isinstance(value, dict):
                # Create a new QTreeWidgetItem with the key as the title
                item = QTreeWidgetItem([key])
                if parent_item is None:
                    self.ui.treeWidget.addTopLevelItem(item)
                else:
                    parent_item.addChild(item)
                # Recursively add child items
                self.fill_tree(value, item)
            else:
                # If the value is a URL, add it as a child item
                child_item = QTreeWidgetItem([key])
                child_item.setData(0, Qt.ItemDataRole.UserRole, value)
                parent_item.addChild(child_item)

    def on_item_clicked(self, item):
        url = item.data(0, Qt.ItemDataRole.UserRole)

        try:
            if not url:
                return

            response = requests.get(url)

            if not response:
                QMessageBox.information(self, 'Http Error', f'File not found. Server returned {response}', QMessageBox.StandardButton.Ok)
                return

            with open('timetable.xlsx', 'wb') as file:
                file.write(response.content)

            self.fill_table(TimeTable('timetable.xlsx'))
            self.ui.buttonPushSetup.setEnabled(True)
        except HttpError as ex:
            QMessageBox.information(self, 'Http Error', f'File not found. Server returned {ex.content}', QMessageBox.StandardButton.Ok)
        except:
            QMessageBox.critical(self, 'Error', str(sys.exc_info()[1]))

    @staticmethod
    def on_button_push_to_calendar_clicked():
        push_to_calendar = PushToCalendar()
        push_to_calendar.exec()


class PushToCalendar(QDialog):
    def __init__(self):
        super(PushToCalendar, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.calendar.setMinimumDate(QDate.currentDate())

        self.calendar_worker = CalendarWorker()

        self.ui.buttonUpdate.clicked.connect(self.on_button_update_clicked)
        self.ui.buttonPush.clicked.connect(self.on_button_push_clicked)

    def on_button_push_clicked(self):
        if not os.path.exists('timetable.xlsx'):
            return

        if self.get_current_calendar_id() is None:
            QMessageBox.information(self,
                                    'No calendar selected',
                                    'You should select Your calendar in combobox. Click update if it is empty.',
                                    QMessageBox.StandardButton.Ok)
            return

        timetable = TimeTable('timetable.xlsx')

        answer = QMessageBox.question(self,
                             'Final approval',
                             f'You are about to push some events to Your calendar `{self.ui.comboBoxCalendars.currentText()}`.\n'
                             f'Events will be scheduled from {timetable.get_start_date().strftime('%d.%m.%Y')} to {self.ui.calendar.selectedDate().toString('dd.MM.yyyy')}.\n'
                             f'This action cannot be undone.',
                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if answer == QMessageBox.StandardButton.Yes:
            timetable.parse_timetable(push=True,
                                      until=self.ui.calendar.selectedDate().toString('yyyyMMdd'),
                                      calendar_id=self.get_current_calendar_id(),
                                      calendar_worker=self.calendar_worker)

    def on_button_update_clicked(self):
        calendars = self.calendar_worker.get_calendars_list()

        if len(calendars.items()) > 0:
            self.ui.buttonPush.setEnabled(True)

        self.ui.comboBoxCalendars.clear()
        for item in calendars.items():
            self.add_item_to_combobox(item[1], item[0])


    def add_item_to_combobox(self, name, user_data):
        self.ui.comboBoxCalendars.addItem(name)
        index = self.ui.comboBoxCalendars.count() - 1
        self.ui.comboBoxCalendars.setItemData(index, user_data, Qt.ItemDataRole.UserRole)

    def get_current_calendar_id(self) -> str:
        current_index = self.ui.comboBoxCalendars.currentIndex()
        user_data = self.ui.comboBoxCalendars.itemData(current_index, Qt.ItemDataRole.UserRole)
        return user_data

def load_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

if __name__ == '__main__':
    app = QApplication([])
    window = Scheduler()
    window.fill_tree(load_json('groups_tree.json'))
    app.exec()
