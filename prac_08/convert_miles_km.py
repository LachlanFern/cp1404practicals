from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    km_output = StringProperty("0.0")

    def build(self):
        Window.size = (600, 300)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """handles conversion of miles into kilometres"""
        result = self.get_miles() * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change ):
        """handles up and down button to change mile increment by 1"""
        result = self.get_miles() + change
        self.root.ids.mile_input.text = str(result)
        self.handle_convert()

    def get_miles(self):
        """extracts a float value of miles from text and validates being a number"""
        try:
            value = float(self.root.ids.mile_input.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
