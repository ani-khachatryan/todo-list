from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from client import registration

Builder.load_file('registration.kv')

class RegistrationWindow(Screen):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def signupbtn(self):
        self.user = registration(self.username.text, 
                                 self.username.text,
                                 self.password.text, 
                                 self.email.text)
        print(type(self.user))
        print(self.user)
        #self.user is ok ????
        self.manager.current = 'login'