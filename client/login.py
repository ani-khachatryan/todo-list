from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from client import login

Builder.load_file('login.kv')

class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    def validate(self):
        pass
        #self.user = login(self.username.text, self.password.text)
        #if len(self.user) == 1:
        #    pass
            #invalid login
        #else:
            #login
        #    self.manager.current = 'tasks'
        #    self.manager.transition.direction = 'left'
        #print(self.user)
