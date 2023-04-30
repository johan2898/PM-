from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivymd.uix.pickers import MDTimePicker, MDDatePicker
import sqlite3


class MainLayout(FloatLayout):
    screen_manager = ObjectProperty(None)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        # create/connet to db
        conn = sqlite3.connect("tasks_db.db")
        # cursor
        c = conn.cursor()
        c.execute("""CREATE TABLE tasks(schedule text, tittle text, duedate text)
        """)
        conn.commit()
        conn.close()
        return Builder.load_file("manager.kv")

    def clear(self):
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

    def on_save(self, instance, value, date_range):
        self.root.ids.duedate.text = str(value)

    def on_cancel(self, instance, value):
        self.root.ids.duedate.text = ""

    def date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def submit(self):
        # create/connet to db
        conn = sqlite3.connect("tasks_db.db")
        # cursor
        c = conn.cursor()
        c.execute("INSERT INTO tasks VALUES(:schedule, :tittle, :duedate)", {
            'schedule': self.root.ids.datainsert.name,
            'tittle': self.root.ids.duedate.text,
            'duedate': self.root.ids.duedate.text,
        })
        conn.commit()
        conn.close()
        self.root.ids.duedate.text = ''
        self.root.ids.taskdecrip.text = ''

    def show_record(self):
        conn = sqlite3.connect("tasks_db.db")
        # cursor
        c = conn.cursor()
        c.execute("SELECT schedule FROM tasks")
        records = c.fetchall()
        word = ''
        for record in records:
            word = f"{word}\n {record}"
            self.root.ids.welcome_label.text = f'{word}'
        conn.commit()
        conn.close()


MainApp().run()
