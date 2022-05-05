from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from client import registration
from kivy.uix.popup import Popup


class RegistrationWindow(Screen):
    Builder.load_file('registration.kv')
    name = ObjectProperty(None)
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def signupbtn(self):
        if registration(self.name.text, 
                                 self.username.text,
                                 self.password.text, 
                                 self.email.text):
            self.manager.current = 'login'
        else:
            Popup(title = 'Invalid Registration', size_hint = (0.4, 0.3)).open()
