from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDTimePicker


class WindowManager(ScreenManager):
    pass


class AddTask(Screen):
    pass


class Tasks(Screen):

    def date_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.open()
        date_dialog = MDDatePicker()
        date_dialog.open()

    pass


class BoxLayout1(Screen):
    my_text = StringProperty("0 tasks")
    task_count = 0
    empty_task = BooleanProperty(True)

    def clicked(self):
        self.task_count += 1
        self.my_text = f" Task: {self.task_count}"
        self.empty_task = False

    pass


class ScheduleView(Screen):
    pass


class MainWidget(Widget):
    pass


class TheLabApp(MDApp):
    pass


TheLabApp().run()

