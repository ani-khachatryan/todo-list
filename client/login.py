from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from numpy import size
from client import login

Builder.load_file('login.kv')


class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    def validate(self):
        if login(username.text, password.text) == True:
            self.manager.current = 'tasks'
            self.manager.transition.direction = 'left'
        else:
            Popup(title = 'Invalid Login', size_hint = (0.4, 0.3)).open()
