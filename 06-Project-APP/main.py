# from kivy.app import App
# from kivi.lang import Builder
# from kyvi.uix.screenmanager import Screemanager, Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json
import glob
from datetime import datetime
from pathlib import Path
import random
Builder.load_file('design.kv')


class LoginScreen(Screen):

    def sign_up(self):
        # de esta manera decimos a que pantalla
        # queremos cambiar
        self.manager.current = "sign_up_screen"

    def forgot_password(self):
        self.manager.transition.direction = "up"
        self.manager.current = "forgot_password"

    def login(self, uname, pword):
        with open('users.json') as file:
            users = json.load(file)
            print(users)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "login_screen_success"
        else:
            # si por ejemplo no es correcto la informacion
            # agregamos una linea como estan dentor de un label
            self.ids.login_wrong.text = "Wrong username or password"
            self.ids.username.text = ""
            self.ids.password.text = ""


class RootWidget(ScreenManager):
    pass

# para cada pantalla tiene su clase


class SignUpScreen(Screen):
    #
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        print(users)

        users[uname] = {
            "username": uname,
            "password": pword,
            "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        }
        # recordar metodo dump
        with open("users.json", "w") as file:
            json.dump(users, file)
        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        # cambiar ahcia donde se cambia de pantalla
        #'left', 'right', 'up', 'down'
        self.manager.transition.direction = "down"
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        avaiable_feelings = glob.glob("quotes/*txt")
        print(avaiable_feelings)

        avaiable_feelings = [Path(filename).stem for filename in
                             avaiable_feelings]
        if feel in avaiable_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)

        else:
            self.ids.quote.text = "Try another feeling"


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class ForgotPasswordScreen(Screen):

    def forgot_password(self):
        self.manager.current = "forgot_password"

    def verify_user(self, uname):
        with open('users.json') as file:
            users = json.load(file)
            print(users)
        if uname in users:
            self.ids.recovery_pw.text = f"Your password is: {users[uname]['password']}"

    def go_to_login(self):
        # cambiar ahcia donde se cambia de pantalla
        #'left', 'right', 'up', 'down'
        self.manager.transition.direction = "down"
        self.manager.current = "login_screen"


class MainApp(App):

    def build(self):
        # aqui retornamos el objecto(dentro de design.kv) no la clase
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
