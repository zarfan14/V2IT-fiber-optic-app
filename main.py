
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button

class FiberCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.length_input = TextInput(hint_text="Panjang kabel", input_filter="float", size_hint_y=None, height=40)
        self.add_widget(self.length_input)

        self.unit_spinner = Spinner(text="m", values=["m", "km"], size_hint_y=None, height=40)
        self.add_widget(self.unit_spinner)

        self.loss_input = TextInput(hint_text="Redaman kabel (dB/km)", input_filter="float", size_hint_y=None, height=40)
        self.add_widget(self.loss_input)

        self.connector_input = TextInput(hint_text="Jumlah konektor", input_filter="int", size_hint_y=None, height=40)
        self.add_widget(self.connector_input)

        self.splice_input = TextInput(hint_text="Jumlah sambungan (splice)", input_filter="int", size_hint_y=None, height=40)
        self.add_widget(self.splice_input)

        calc_btn = Button(text="Hitung Redaman", size_hint_y=None, height=50)
        calc_btn.bind(on_press=self.calculate_loss)
        self.add_widget(calc_btn)

        self.result_label = Label(text="Total Redaman: - dB", size_hint_y=None, height=40)
        self.add_widget(self.result_label)

    def calculate_loss(self, instance):
        try:
            length = float(self.length_input.text)
            unit = self.unit_spinner.text
            if unit == "km":
                length_km = length
            else:
                length_km = length / 1000

            loss_per_km = float(self.loss_input.text)
            connector_count = int(self.connector_input.text)
            splice_count = int(self.splice_input.text)

            connector_loss = 0.75 * connector_count
            splice_loss = 0.3 * splice_count
            fiber_loss = loss_per_km * length_km

            total_loss = fiber_loss + connector_loss + splice_loss
            self.result_label.text = f"Total Redaman: {total_loss:.2f} dB"
        except:
            self.result_label.text = "Input tidak valid"

class V2ITFiberOpticApp(App):
    def build(self):
        return FiberCalculator()

if __name__ == '__main__':
    V2ITFiberOpticApp().run()
