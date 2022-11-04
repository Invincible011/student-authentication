from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '853')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from screen import *

'''from kivy.core.window import Window as win
win.size = (480,853)
win.pos = .5'''

Builder.load_file('signin.kv')
Builder.load_file('signup.kv')
kv = Builder.load_file('access.kv')


class AuthenticationApp(App):
    def build(self):
        return kv
        
if __name__ == "__main__":
    si = AuthenticationApp()
    si.run()
