import sys
sys.path.append("src")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from model.BuyLogic import *

class CompraApp(App):
    def build(self):
        Window.clearcolor = (0.2, 0.2, 0.2, 1)  # Fondo oscuro
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10,size_hint_y=None )
        main_layout.height = Window.height * 0.6  # Ajusta la altura para que no ocupe toda la pantalla
        main_layout.pos_hint = {"center_y": 0.5}  # Centra el contenido verticalmente
        form_layout = BoxLayout(orientation='vertical', spacing=10)

        self.inputs = {}
        fields = [
            ("Valor de la compra", 'valor_compra'),
            ("Valor del IVA (%)", 'valor_iva'),
            ("Impuesto al consumo (%)", 'valor_impuesto_consumo'),
            ("Impuesto al licor (%)", 'impuesto_licor'),
            ("¿Impuesto de bolsa? (Si/No)", 'impuesto_bolsa')
        ]
        
        for label_text, field_name in fields:
            box = BoxLayout(size_hint_y=None, height=40, spacing=10)
            label = Label(text=label_text, size_hint_x=0.5, color=(1, 1, 1, 1))
            input_field = TextInput(multiline=False, size_hint_x=0.5, background_color=(1, 1, 1, 0.8))
            self.inputs[field_name] = input_field
            box.add_widget(label)
            box.add_widget(input_field)
            form_layout.add_widget(box)
        
        self.result_label = Label(text="", size_hint_y=None, height=40, color=(1, 1, 1, 1))
        button = Button(text="Calcular total", size_hint_y=None, height=50, background_color=(0.1, 0.6, 0.3, 1))
        button.bind(on_press=self.calculate)
        
        main_layout.add_widget(form_layout)
        main_layout.add_widget(self.result_label)
        main_layout.add_widget(button)
        
        return main_layout

    def calculate(self, instance):
        valores = {key: self.inputs[key].text for key in self.inputs}
        resultado = calcular_total_compra(**valores)
        self.result_label.text = str(resultado)

if __name__ == "__main__":
    CompraApp().run()