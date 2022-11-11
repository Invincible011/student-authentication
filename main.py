from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '853')
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from signin.screen import LoginWindow
from student.student import MainDashboard
from kivy.uix.boxlayout import BoxLayout

 #main = Builder.load_file("signin/signin.kv")


class MainWindow(BoxLayout):
    sigin_page = LoginWindow()
    student_page = MainDashboard()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.scr_si.add_widget(self.sigin_page)
        
class MainApp(App):
    def build(self):
        return Button(text=('Hello world!'))
    
    
if __name__ == "__main__":
    ma = MainApp()
    ma.run()