from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '853')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class DelApp(App):
    pass
        
if __name__ == "__main__":
    si = DelApp()
    si.run()