from datetime import datetime
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

'''
from kivy.core.window import Window as win
win.size = (480,853)
win.pos = .5
'''

Builder.load_file('signin/signin.kv')

class LoginWindow(Screen):
    def _initialise(self):
        time = datetime.now()
        date = time.strftime("%Y")
        date1 = self.ids.t1
        date1.text = "©" + date + ". University of Ilorin, Ilorin. All right reserved | Developed by Fandroid Tech."
        time = int(time.strftime("%H"))
        
        if time < 12:
            greet = self.ids.greet
            greet.font_size = 36
            greet.bold = True
            greet.text = "Good Morning"
        elif time >= 12 | time < 15:
            greet = self.ids.greet
            greet.font_size = 36
            greet.bold = True
            greet.text = "Good Afternoon"            
        else:
            greet = self.ids.greet
            greet.font_size = 36
            greet.bold = True
            greet.text = "Good Evening"
        
    def on_kv_post(self, base_widget):
        self._initialise()
        
    def validate_user(self):
        uname = self.ids.user
        pwd = self.ids.pwd
        
        username = uname.text
        password = pwd.text
        info = self.ids.info
        show_pwd = self.ids.forget_pwd
        
        if username == '' or password == '':
            if username == '':
                uname.focus = True
                username = ''
                info.text = '[color=#FF0000][b]username is required[/b][/color]'   
                          
            else:
                pwd.focus = True
                password = ''
                info.text = '[color=#FF0000][b]password is required[/b][/color]'
               
        else:
            if username == '1' and password == '1':
                #uname.text = ''
                #pwd.text = ''
                uname.focus = True 
                #Used for Debugging, To be removed later...
                #info.text = '[color=#00FF00][b]Logged in successfully[/b][/color]'
                show_pwd.disabled = True
                self.parent.current = "scr_stud"
                self.parent.transition.direction = "left"
                info.text = ""
                
            elif username != '1' and password != '1':
                uname.focus = True
                uname.text = ''
                pwd.text = ''
                info.text = '[color=#FF0000][b]Invalid username and/or password[/b][/color]'
                show_pwd.disabled = True
            else:
                if username != '1':
                    uname.text = ''
                    uname.focus = True
                    info.text = '[color=#FF0000][b]Invalid username[/b][/color]'
                    show_pwd.disabled = True
                elif password != '1':
                    pwd.text = ''
                    info.text = '[color=#FF0000][b]Invalid password[/b][/color]'
                    show_pwd.disabled = False   
                      
    def close(self):
        return exit()