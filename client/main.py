from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

from login import LoginWindow
from registration import RegistrationWindow
from tasks_screen import TasksScreen
import client

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"
        self.theme_cls.primary_hue = "200"  # "500"
        self.theme_cls.theme_style = "Dark"  # "Light"

        manager = ScreenManager()

        self.login_window_instance = LoginWindow(name='login')
        self.login_window_instance.app = self
        manager.add_widget(self.login_window_instance)
        manager.add_widget(RegistrationWindow(name='signup'))
        self.task_screen_instance = TasksScreen(name='tasks')
        manager.add_widget(self.task_screen_instance)
        return manager

if __name__ == '__main__':
    LoginApp().run()
