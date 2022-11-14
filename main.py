from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '853')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from signin.screen import *
from student.student import *

Builder.load_file("signin/access.kv")
Builder.load_file("student/stud_assest.kv")

class MainWindow(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        
class MainApp(App):
    def build(self):
        self.root = MainWindow()
        
    
if __name__ == "__main__":
    ma = MainApp()
    ma.run()