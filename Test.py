import kivy
import random
from sample_google_search import search_url

import keyboard

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_file('test.kv')

def see(stuff):
    return ' '.join(stuff.split()[2:]), '0'

class MyLayout(Widget):
    def press(self): 
        for i in range(4):
            exec(f'self.ids.re{i}.text, self.ids.c{i}. text = (0,0)')
        prompt = self.ids.text_input.text.replace('Enter Search Prompt: ', '')
        self.ids.text_input.text = 'Enter Search Prompt: \n'
        url_list = search_url(prompt)

        for i in range(4):
            exec(f'self.ids.re{i}.text, self.ids.c{i}. text = tuplist[{i}]')
        return prompt

class ECoEat(App):
    def build(self):
        return MyLayout()

# class Backend():  
#     def __init__(self):
#         url = search_url(self)
#         print(url)


if __name__ == '__main__':
    app = ECoEat()
    app.run()