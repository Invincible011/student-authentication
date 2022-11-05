from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '853')
from kivy.app import App
from kivy.lang import Builder
from screen import *
'''import sys
sys.path.append('/python codes/STUDENT_AUTHENTICATION/student')'''

#Builder.load_file('student/studdash.kv')
Builder.load_file('signin.kv')
Builder.load_file('signup.kv')
kv = Builder.load_file('access.kv')


class AuthenticationApp(App):
    def build(self):
        return kv
        
if __name__ == "__main__":
    si = AuthenticationApp()
    si.run()
