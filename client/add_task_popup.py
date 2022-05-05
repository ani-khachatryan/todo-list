from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker
from tasks_screen import TaskList
from client import User

class AddTaskPopup(Popup):
    Builder.load_file('add_task_popup.kv')
    description = ObjectProperty(None)
    def show_date_picker(self):
        picker = MDDatePicker()
        picker.bind(on_save = self.save_date)
        picker.open()

    def save_date(self, instance, value, date_range):
        self.ids.date.text = str(value)

    def add_task(self):
        if self.ids.date.text == None:
            Popup(title = 'Invalid Date!', size_hint = (0.4, 0.3)).open()
        else:
            date = self.ids.date.text
            new_id = User.add_task(self.description.text, date)
            TaskList.add_task(self.description.text, date, new_id)
            self.dismiss()
