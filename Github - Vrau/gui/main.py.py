import kivy
kivy.require('2.0.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label

        
class LoginWindow(BoxLayout):

    email = ObjectProperty(None)

    # Validação do email

    def loginBtn(self):
        if self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            validLogin()
            # sm.current = "method"
        else:
            invalidLogin()
        
                
class MethodWindow(BoxLayout):

    def srcBtn(self):   # Search Button
        pass

    def insBtn(self):   # Insert Button
        pass

    
class WindowManager(ScreenManager):
    pass



def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid email.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def validLogin():
    pop = Popup(title='Valid Login',
                  content=Label(text='Valid email.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


# kv = Builder.load_file("myapp.kv")
# Somente fazer isso se o nome do arquivo ".kv" não for o mesmo da classe do aplicativo

sm = WindowManager()

# Problemas
# screens = [LoginWindow(name="login"), MethodWindow(name="method")]
# for screen in screens:
#     sm.add_widget(screen)

# sm.current = "login"


class MyApp(App):
    def build(self):
        return LoginWindow()
    
        

if __name__ == '__main__':
    MyApp().run()