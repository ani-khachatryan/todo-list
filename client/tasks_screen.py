from kivy.uix.screenmanager import Screen
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder
from client import User

class TasksScreen(Screen):
    Builder.load_file('tasks_screen.kv')
    def back(self):
        self.manager.current = 'login'
        self.manager.transition.direction = 'right'

class TaskList(RecycleView):
    Tasks = User.get_tasks()
    def add_task(self, text, date, id):
        self.data.append({'text': text, 'task_date': date, 'id': id, 'caller': self})
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Tasks = ['anasun', 'ailandak muxam', 'kulisneri poshi', 'aaaa']
        self.data = [{'text': task[2], 'task_date': task[3], 'id': task[0], 'caller': self} for task in self.Tasks]