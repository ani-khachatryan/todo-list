from kivy.uix.screenmanager import Screen
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder


class TasksScreen(Screen):
    Builder.load_file('tasks_screen.kv')
    def back(self):
        self.manager.current = 'login'
        self.manager.transition.direction = 'right'

class TaskList(RecycleView):
    #Tasks = client.get_tasks()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Tasks = ['anasun', 'ailandak muxam', 'kulisneri poshi', 'aaaa']
        self.data = [{'text': 'xren', 'aa': 'bomj', 'id': task, 'caller': self} for task in Tasks]