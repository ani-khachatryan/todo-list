from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from numpy import size
from client import login

from task_button import TaskButton
from client import User

Builder.load_file('login.kv')


class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    def validate(self):
        if login(self.username.text, self.password.text):
            self.manager.current = 'tasks'
            self.manager.transition.direction = 'left'
            tasks = User.get_tasks()
            task_buttons = self.app.task_screen_instance.ids['container']
            for task in tasks:
                task_btn = TaskButton(task[3], task[2], task[0], self.app.task_screen_instance)
                self.app.task_screen_instance.tasks.append([task[0], task_btn])
                task_buttons.add_widget(task_btn)
        else:
            Popup(title = 'Invalid Login', size_hint = (0.4, 0.3)).open()
