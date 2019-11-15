import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget): # Reason the content from the my.kv file is on the bottom left corner of the screen when running the program is because "widget" has a defined size/position
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self): # Defines the button method for "on_press" in my.kv
        print("Name:", self.name.text)
        print("Email:", self.email.text)
        self.name.text = "" # Clears text box after printing to console
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()


# Using the .kv code allows separation of design code from non-design code, which has some benefits over not doing that.