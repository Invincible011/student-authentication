from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '853')
from kivy.app import App
from kivy.lang import Builder
from stud_operator import *

Builder.load_file('personal_details.kv')
main_win = Builder.load_file('studdash.kv')

class StudentApp(App):
    def build(self):
        return main_win
        
if __name__ == "__main__":
    st = StudentApp()
    st.run()