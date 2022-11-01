from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '853')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

'''from kivy.core.window import Window as win
win.size = (480,853)
win.pos = .5'''

class ULABEL(Label):
    pass

class UBTN(Button):
    pass

class UTEXT(TextInput):
    pass
class LoginWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def validate_user(self):
        uname = self.ids.user
        pwd = self.ids.pwd
        
        username = uname.text
        password = pwd.text
        info = self.ids.info
        #label = self.ids.markup
        #label.text = '[color=#F0F8FF]Not a Member[/color][color=#033E3E][b]Sign up[/b][/color]'       
        if username == '' or password == '':
            if username == '':
                uname.focus = True
                username = ''
                info.text = '[color=#FF0000][b]username is required[/b][/color]'   
                          
            elif password == '':
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
                info.text = '[color=00FF00][b]Logged in successfully[/b][/color]'

            elif username != 'admin' and password != 'admin':
                uname.focus = True
                uname.text = ''
                pwd.text = ''
                info.text = '[color=FF0000][b]Invalid username and/or password[/b][/color]'
            else:
                if username != 'admin':
                    uname.text = ''
                    uname.focus = True
                    info.text = '[color=#FF0000][b]Invalid username[/b][/color]'
                elif password != 'admin':
                    pwd.text = ''
                    info.text = '[color=#FF0000][b]Invalid password[/b][/color]'
        
    def change(self):
        self.ids.signin.background_color = (1, 1, 1, 1 )
        
    def dispose(self):
        return exit()

class SigninApp(App):
    def build(self):
        return LoginWindow()
        
if __name__ == "__main__":
    si = SigninApp()
    si.run()
