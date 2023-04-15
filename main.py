from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class WindowManager(ScreenManager):
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


class TheLabApp(App):
    pass


TheLabApp().run()
