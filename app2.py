from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDRectangleFlatButton, MDFlatButton
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from Helpers import username_helper
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem


class MYAPP(MDApp):
    def build(self):
        # self.theme_cls.primary_palette = "Teal"
        # self.theme_cls.primary_hue = "A700"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        btn = MDRectangleFlatButton(text='LOGIN', pos_hint={'center_x': 0.5, 'center_y': 0.4}
                                    , on_release=self.show_data)
        ##btn1 = MDFloatingActionButton(icon="zodiac-gemini",pos_hint={'center_x': 0.5, 'center_y': 0.5},)
        # btn2 = MDIconButton(icon="setting",pos_hint={'center_x': 0.4, 'center_y': 0.5})
        # btn3 = MDRoundImageButton(pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.username = Builder.load_string(username_helper)

        screen.add_widget(self.username)
        screen.add_widget(btn)
        return screen

    def show_data(self, obj):
        if self.username.text is '':
            check_string = "Enter a Username"
        else:
            check_string = self.username.text + ' Thanks for Visiting'
        button1 = MDFlatButton(text='Close', on_release=self.close_dialog)
        button2 = MDFlatButton(text='Get inside')
        self.theme_cls.theme_style = 'Light'
        self.dialog = MDDialog(title='WELCOME !!', text=check_string, size_hint=(0.7, 1),
                               buttons=[button1, button2])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

   # def open_dialog(self,obj):
        #btn = OneLineIconListItem(text="HELLO", icon='lock')
    #    self.dialog.()

MYAPP().run()
