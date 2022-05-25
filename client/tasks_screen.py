from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivymd.uix.picker import MDDatePicker
from kivy.lang import Builder
from client import User
from task_button import TaskButton

class TasksScreen(Screen):
    Builder.load_file('tasks_screen.kv')
    tasks = []
    def back(self):
        self.manager.current = 'login'
        self.manager.transition.direction = 'right'


class AddTaskPopup(Popup):
    def __init__(self, caller, **kwargs):
        super(AddTaskPopup, self).__init__(**kwargs)
        self.caller = caller

    Builder.load_file('add_task_popup.kv')
    description = ObjectProperty(None)

    def show_date_picker(self):
        picker = MDDatePicker()
        picker.bind(on_save = self.save_date)
        picker.open()

    def save_date(self, instance, value, date_range):
        self.ids.date.text = str(value)

    def add_task(self):
        if self.ids.date.text == 'enter task date':
            Popup(title = 'Invalid Date!', size_hint = (0.4, 0.3)).open()
        else:
            date_ = self.ids.date.text
            new_id = User.add_task(self.description.text, date_)
            new_id = new_id[0]
            task_btn = TaskButton(date_, self.description.text, new_id, self.caller)
            self.caller.tasks.append([new_id, task_btn])
            self.caller.ids['container'].add_widget(task_btn)
            self.dismiss()
