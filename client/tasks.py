from kivy.uix.screenmanager import Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.lang import Builder


class TasksScreen(Screen):
    Builder.load_file('tasks.kv')
    def back(self):
        self.manager.current = 'login'
        self.manager.transition.direction = 'right'

class AddTaskPopup(Popup):
    Builder.load_file('add_task_popup.kv')
    description = ObjectProperty()
    name = ObjectProperty()
    def add_task(self):
        #addTaskToServer #TODO
        print(self.name.text)
        self.dismiss()

class TaskList(RecycleView):
    #Tasks = client.get_tasks()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Tasks = ['anasun', 'ailandak muxam', 'kulisneri poshi', 'aaaa']
        self.data = [{'text': task, 'aa': 'bomj'} for task in Tasks]