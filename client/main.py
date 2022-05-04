from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
#from kivy.uix.listview import ListItemButton

import login
import registration
import tasks
import client

class LoginApp(App):
    def build(self):
        manager = ScreenManager()

        manager.add_widget(login.LoginWindow(name='login'))
        manager.add_widget(registration.RegistrationWindow(name='signup'))
        manager.add_widget(tasks.TasksScreen(name='tasks'))
        return manager

if __name__ == '__main__':
    LoginApp().run()
