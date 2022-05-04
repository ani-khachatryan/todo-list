from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang import Builder

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
        pass
        #self.caller.data.append