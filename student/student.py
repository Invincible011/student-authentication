from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '853')
from datetime import datetime
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from stud_operator import *
from kivy.core.window import Window as win
from kivy.properties import ListProperty, ObjectProperty

Builder.load_file('personal_details.kv')
main_win = Builder.load_file('studdash.kv')


class Dropdown(BoxLayout):
    button_list = ListProperty(None)
    
    def __init__(self, button_list, **kwargs):
        super().__init__(**kwargs)
        self.button_list = button_list     
    
    def on_button_list(self, object, values):
        
        for i in values:
            self.add_widget(Button(text=i, font_size= 9, background_color=(0,0,0,.2), background_normal='', bold=True))


class NewBox(BoxLayout):
    dropdown = ObjectProperty(None)
    mynone = ObjectProperty([])
    
    def remove_inserted_widget(self, *args, **kwargs):
        if self.dropdown:
            self.remove_widget(self.dropdown)
            self.dropdown = self.mynone
            
    def insert_widget(self, widget, r_widget):
        if self.dropdown:
            self.remove_inserted_widget()
        found = False
        wid = []
        children = self.children[::-1]
        for button in children:
            if button == r_widget:
                found = True
                continue
            if found:
                wid.append(button)
                self.remove_widget(button)
        self.add_widget(widget)
        self.dropdown = widget
        for w in wid:
            self.add_widget(w)

        
class MainDashboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def togglemenutab(self):

        toggle = self.ids.menu        
        if toggle.width == 140:
            toggle.width = 0
        else:
            toggle.width =140
    
    def on_kv_post(self, base_widget):
        self._initialise_log()
        
    def _initialise_log(self):
        log = self.ids.log_time
        time = datetime.now()
        week = time.strftime("%A")
        month = time.strftime("%B")
        year = time.strftime("%Y")
        
        log.text = f"Today: {week}, {month}, {year}."
        
        
class StudentApp(App):
    def build(self):
        return MainDashboard()
        
        
if __name__ == "__main__":
    st = StudentApp()
    st.run()