
from kivy.config import Config
Config.set('graphics' ,'width', 400)
Config.set('graphics' ,'height', 500)

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class CalcApp(App):
    def build(self):
        self.formula = '0'
        bl = BoxLayout(orientation='vertical', padding=[5])
        gl = GridLayout(cols=4, spacing=2.5, size_hint=(1, .7))
        
        self.lbl = Label(text=self.formula, font_size=48, size_hint=(1, .3), text_size=(400-10, 500*.3), halign='right', valign='center')
        bl.add_widget(self.lbl)
        
        gl.add_widget(Button(text='AC', on_press=self.ac))
        gl.add_widget(Widget())
        gl.add_widget(Button(text='Уд. символ', on_press=self.c))
        gl.add_widget(Button(text='/', on_press=self.add))
        
        gl.add_widget(Button(text='7', on_press=self.add))
        gl.add_widget(Button(text='8', on_press=self.add))
        gl.add_widget(Button(text='9', on_press=self.add))
        gl.add_widget(Button(text='*', on_press=self.add))
        
        gl.add_widget(Button(text='4', on_press=self.add))
        gl.add_widget(Button(text='5', on_press=self.add))
        gl.add_widget(Button(text='6', on_press=self.add))
        gl.add_widget(Button(text='-', on_press=self.add))
        
        gl.add_widget(Button(text='1', on_press=self.add))
        gl.add_widget(Button(text='2', on_press=self.add))
        gl.add_widget(Button(text='3', on_press=self.add))
        gl.add_widget(Button(text='+', on_press=self.add))
        
        gl.add_widget(Widget())
        gl.add_widget(Button(text='0', on_press=self.add))
        gl.add_widget(Button(text='.', on_press=self.add))
        gl.add_widget(Button(text='=', on_press=self.rav))
        
        bl.add_widget(gl)
        
        return bl
    
    def add(self, instanse):
        if self.formula == '0':
            self.formula = ''
            
        self.formula += str(instanse.text)
        print(self.formula)
        self.update_label()
        
    def update_label(self):
        self.lbl.text = self.formula
        
    def rav(self, instance):
        self.formula = str(eval(self.lbl.text))
        self.update_label()
        
    def ac(self, instance):
        self.formula = '0'
        self.update_label()
        
    def c(self, instance):
        self.lbl.text = self.lbl.text[:-1] 
        self.formula = self.lbl.text
        self.update_label()



if __name__ == "__main__":
    CalcApp().run()