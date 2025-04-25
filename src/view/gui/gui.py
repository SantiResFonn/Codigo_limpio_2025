import sys
import os

# Agregar la carpeta src a las rutas de búsqueda
basedir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(basedir, "src"))


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from src.model.BuyLogic import *

class CompraApp(App):
    """Clase principal de la aplicación Kivy que crea la interfaz gráfica y maneja la lógica de la compra."""
    def build(self):
        Window.clearcolor = (0.2, 0.2, 0.2, 1)  # Fondo oscuro
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10, size_hint_y=None)  # Crea el layout principal de la aplicación
        main_layout.height = Window.height * 0.6  # Ajusta la altura para que no ocupe toda la pantalla
        main_layout.pos_hint = {"center_y": 0.5}  # Centra el contenido verticalmente
        form_layout = BoxLayout(orientation='vertical', spacing=10)  # Crea un layout secundario para la entrada de datos.

        self.inputs = {}  # Diccionario para almacenar los campos de entrada
        # Lista de etiquetas y nombres de campo para crear los campos de entrada
        fields = [
            ("Valor de la compra", 'valor_compra'),
            ("Valor del IVA (%)", 'valor_iva'),
            ("Impuesto al consumo (%)", 'valor_impuesto_consumo'),
            ("Impuesto al licor (%)", 'impuesto_licor'),
            ("¿Impuesto de bolsa? (Si/No)", 'impuesto_bolsa')
        ]
        
        for label_text, field_name in fields:  # Bucle para crear cada par de etiqueta y campo de entrada
            box = BoxLayout(size_hint_y=None, height=40, spacing=10)
            label = Label(text=label_text, size_hint_x=0.5, color=(1, 1, 1, 1))
            input_field = TextInput(multiline=False, size_hint_x=0.5, background_color=(1, 1, 1, 0.8))
            self.inputs[field_name] = input_field
            box.add_widget(label)
            box.add_widget(input_field)
            form_layout.add_widget(box)
        
        # Etiqueta para mostrar el resultado de manera más visible
        self.result_label = Label(
            text="",
            size_hint_y=None,
            height=60,
            font_size='20sp',
            color=(1, 1, 0, 1)  # Color amarillo para destacar
        )
        
        # Etiqueta para indicar que es el valor total
        self.result_title_label = Label(
            text="Valor total de la compra:",
            size_hint_y=None,
            height=40,
            font_size='18sp',
            color=(1, 1, 1, 1)
        )
        
        button = Button(
            text="Calcular total",
            size_hint_y=None,
            height=50,
            background_color=(0.1, 0.6, 0.3, 1)
        )  # Botón para calcular el total
        button.bind(on_press=self.calculate)
        
        main_layout.add_widget(form_layout)
        main_layout.add_widget(self.result_title_label)  # Agrega la etiqueta del título
        main_layout.add_widget(self.result_label)  # Agrega la etiqueta del resultado
        main_layout.add_widget(button)
        
        return main_layout

    def calculate(self, instance):
        """Método que se llama al presionar el botón de calcular. Valida la entrada y calcula el total de la compra."""
        try:
            self.validate_input()
            resultado = calcular_total_compra(
                float(self.inputs['valor_compra'].text),
                float(self.inputs['valor_iva'].text),
                float(self.inputs['valor_impuesto_consumo'].text),
                float(self.inputs['impuesto_licor'].text),
                self.inputs['impuesto_bolsa'].text
            )
            self.result_label.text = f"${resultado:,.2f}"  # Formato de moneda
        except ValueError as e:
            popup = Popup(title='Error', content=Label(text=str(e)), size_hint=(0.8, 0.4))
            popup.open()

    def validate_input(self):
        """Método que valida la entrada del usuario. Verifica que los campos no estén vacíos y que contengan valores numéricos válidos."""
        if not self.inputs['valor_compra'].text.isdigit():
            raise ValueError("ERROR: El valor de la compra debe ser un número")
        if not self.inputs['valor_iva'].text.isdigit():
            raise ValueError("ERROR: El valor del IVA debe ser un número")
        if not self.inputs['valor_impuesto_consumo'].text.isdigit():
            raise ValueError("ERROR: El valor del Impuesto al consumo debe ser un número")
        if not self.inputs['impuesto_licor'].text.isdigit():
            raise ValueError("ERROR: El valor del Impuesto al licor debe ser un número")
        if self.inputs['impuesto_bolsa'].text.lower() not in ["si", "no"]:
            raise ValueError("ERROR: Parametro de impuesto de bolsa no valido (Si/No) ")
        
        
if __name__ == "__main__":
    CompraApp().run()