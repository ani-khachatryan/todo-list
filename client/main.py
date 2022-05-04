from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

import login
import registration
import tasks_screen
import client

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"
        self.theme_cls.primary_hue = "200"  # "500"
        self.theme_cls.theme_style = "Dark"  # "Light"

        manager = ScreenManager()

        manager.add_widget(login.LoginWindow(name='login'))
        manager.add_widget(registration.RegistrationWindow(name='signup'))
        manager.add_widget(tasks_screen.TasksScreen(name='tasks'))
        return manager

if __name__ == '__main__':
    LoginApp().run()
