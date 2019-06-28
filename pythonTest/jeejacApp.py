import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class myLabel(Label):
    pass

class JeeJac(App):
    def build(self):
        return myLabel()

if __name__ == "__main__":
    JeeJac().run()