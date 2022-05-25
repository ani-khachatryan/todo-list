from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang import Builder
from client import User

class TaskPopup(Popup):
    def __init__(self, caller, **kwargs):
        self.caller = caller
        super(Popup, self).__init__(**kwargs)


class TaskButton(Button):
    def __init__(self, date, description, id, task_screen, **kwargs):
        self.date = date
        self.text = description
        self.task_screen = task_screen
        self.id = id
        super(Button, self).__init__(**kwargs)
    Builder.load_file('task_button.kv')
    def press(self):
        pop = TaskPopup(self)
        pop.open()
    def delete(self):
        User.delete_task(self.id)
        for task in self.task_screen.tasks:
            if task[0] == self.id:
                btn = task[1]
        self.task_screen.ids['container'].remove_widget(btn)