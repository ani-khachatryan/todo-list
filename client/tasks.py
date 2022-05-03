from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file('tasks.kv')

class Boxk(BoxLayout):
    pass

class TasksScreen(Screen):
    pass

class TaskButton(Button):
    def press(self):
        print(self.aa)

class Tasks(RecycleView):
    #Tasks = client.get_tasks()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Tasks = ['anasun', 'ailandak muxam', 'kulisneri poshi', 'aaaa']
        self.data = [{'text': task, 'aa': 'bomj'} for task in Tasks]