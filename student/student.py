from kivy.config import Config

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '853')
from datetime import datetime

from kivy.core.window import Window as win
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from student.stud_operator import PersonalDetails

Builder.load_file('student/personal_details.kv')
main_win = Builder.load_file('student/studdash.kv')


class Dropdown(BoxLayout):
    button_list = ListProperty()
    font_size = 9
    def __init__(self, button_list, scrn_mngr, **kwargs):
        
        super().__init__(**kwargs)
        self.button_list = button_list     
        self.mngr = scrn_mngr
    def on_button_list(self, object, values):
        
        for name, fnc in values:
            self.add_widget(Button(text=name, font_size= self.font_size, on_press = fnc, background_color=(0,0,0,.2), background_normal='', bold=True))
            

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
            
    # All the Toggle button EventTrigggers are all defined below
    def p_main_menu(self):
        self.remove_inserted_widget()
    
    def details(self):
        self.remove_inserted_widget()
    
    def change_password(self):
        self.remove_inserted_widget()
        
    def logout(self):
        me = self.parent.parent.parent.parent.parent.parent
        me.current = 'scr_si'
        self.remove_inserted_widget()
        self.parent.parent.parent.\
            parent.parent.parent.\
            transition.direction = "right"
    
    #Main_Menu Toggle Button functions
    def p_reg(self):
        self.remove_inserted_widget()
       
    def curr_charge(self):
        self.remove_inserted_widget()
    
    def sch_charge(self):
        self.remove_inserted_widget()
        
    def course_reg(self):
        self.remove_inserted_widget()
        
    def complete_courses(self):
        self.remove_inserted_widget()
        
    def payment(self):
        self.remove_inserted_widget()
    
    def result(self):
        self.remove_inserted_widget()
        
    def revalidation(self):
        self.remove_inserted_widget()
        
    def clearance(self):
        self.remove_inserted_widget()
        
    def screening_result(self):
        self.remove_inserted_widget()
        
        
        
class MainDashboard(NewBox, BoxLayout):
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
    
    def close(self):
        self.parent.parent.current = "scr_si"
        self.parent.parent.transition.direction = "right"