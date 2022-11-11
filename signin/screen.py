from kivy.uix.screenmanager import Screen
from datetime import datetime
from kivy.lang import Builder

'''
from kivy.core.window import Window as win
win.size = (480,853)
win.pos = .5
'''
Builder.load_file('signin/signin.kv')
Builder.load_file('signin/signup.kv')

class LoginWindow(Screen):
    def _initialise(self):
        time = datetime.now()
        date = time.strftime("%Y")
        #print(f"Am going to ROOT WIDGET:, and It's {self.parent.get_screen('login_scr').ids.t1.text}")
        date1 = self.parent.get_screen('login_scr').ids.t1
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
        #print("IDS: ", self.ids)
        
    def validate_user(self):
        uname = self.ids.user
        pwd = self.ids.pwd
        
        username = uname.text
        password = pwd.text
        info = self.ids.info
        show_pwd = self.ids.forget_pwd
        
        #label = self.ids.markup
        #label.text = '[color=#F0F8FF]Not a Member[/color][color=#033E3E][b]Sign up[/b][/color]'       
        if username == '' or password == '':
            if username == '':
                uname.focus = True
                username = ''
                info.text = '[color=#FF0000][b]username is required[/b][/color]'   
                          
            else:
                pwd.focus = True
                password = ''
                info.text = '[color=#FF0000][b]password is required[/b][/color]'
                '''  else:
                    pwd.focus = True
                    password = ''
                    info.text = '[color=#FF0000][b]password is required[/b][/color]'''
                 
        else:
            if username == 'admin' and password == 'admin':
                uname.text = ''
                pwd.text = ''
                uname.focus = True 
                #Used for Debugging, To be removed later...
                info.text = '[color=#00FF00][b]Logged in successfully[/b][/color]'
                show_pwd.disabled = True
                self.parent.current = 'signup_scr'
                
            elif username != 'admin' and password != 'admin':
                uname.focus = True
                uname.text = ''
                pwd.text = ''
                info.text = '[color=#FF0000][b]Invalid username and/or password[/b][/color]'
                show_pwd.disabled = True
            else:
                if username != 'admin':
                    uname.text = ''
                    uname.focus = True
                    info.text = '[color=#FF0000][b]Invalid username[/b][/color]'
                    show_pwd.disabled = True
                elif password != 'admin':
                    pwd.text = ''
                    info.text = '[color=#FF0000][b]Invalid password[/b][/color]'
                    show_pwd.disabled = False     
    def dispose(self):
        return exit()


class SignUpWindow(Screen):
    def _initialise(self):
        time = datetime.now()
        #date = time.strftime("%Y")
        #print(f"Am going to ROOT WIDGET:, and It's {self.parent.get_screen('login_scr').ids.t1.text}")
        #date1 = self.parent.get_screen('signup_scr').ids.footer
        #date1.text = "©" + date + ". University of Ilorin, Ilorin. All right reserved | Developed by Fandroid Tech."
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
        #print("IDS: ", self.ids)
          
    def validate_user(self):
        pass

    def dispose(self):
        return exit()