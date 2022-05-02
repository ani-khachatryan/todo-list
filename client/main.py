from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
import os
#from kivy.uix.listview import ListItemButton
import client


Builder.load_file('login.kv')
Builder.load_file('registration.kv')
#Builder.load_file('tasks.kv')

class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    def validate(self):
        self.user = client.login(self.username.text, self.password.text)
        if len(self.user) == 1:
            pass
            #invalid login
        else:
            pass
            #login
            self.manager.current = 'tasks'
        print(self.user)

    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

class RegistrationWindow(Screen):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def signupbtn(self):
        self.user = client.registration(self.username.text, 
                                        self.username.text,
                                        self.password.text, 
                                        self.email.text)
        print(type(self.user))
        print(self.user)
        #self.user is ok ????
        self.manager.current = 'login'

class TaskScreen(Screen):
    pass
    #Tasks = client.get_tasks()
    #Tasks = ['anasun', 'ailandak muxam', 'kulisneri poshi']

class LoginApp(App):
    def build(self):
        manager = ScreenManager()

        manager.add_widget(LoginWindow(name='login'))
        manager.add_widget(RegistrationWindow(name='signup'))
        manager.add_widget(TaskScreen(name='tasks'))
        return manager

if __name__ == '__main__':
    LoginApp().run()
