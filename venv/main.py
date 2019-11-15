import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior


class MyApp(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    MyApp().run()
