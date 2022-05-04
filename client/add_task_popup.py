from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker

class AddTaskPopup(Popup):
    Builder.load_file('add_task_popup.kv')
    description = ObjectProperty()
    def show_date_picker(self):
        picker = MDDatePicker()
        picker.bind(on_save = self.save_date)
        picker.open()

    def save_date(self, instance, value, date_range):
        self.ids.date.text = str(value)

    def add_task(self):
        #addTaskToServer #TODO
        print(self.description.text)
        self.dismiss()