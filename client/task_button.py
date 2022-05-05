from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang import Builder
from client import User

class TaskPopup(Popup):
    def __init__(self, caller, **kwargs):
        self.caller = caller
        super(TaskPopup, self).__init__(**kwargs)

class TaskButton(Button):
    Builder.load_file('task_button.kv')
    def press(self):
        pop = TaskPopup(self)
        pop.open()
    def delete(self):
        User.delete_task(self.id)
        self.caller.data = [task for task in self.caller.data if task[id] != self.id]