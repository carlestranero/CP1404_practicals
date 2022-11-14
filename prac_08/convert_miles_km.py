from kivy.app import App
from kivy.lang import Builder

CONVERSION_RATE = 1.60934

class ConvertMilesToKm(App):

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) * CONVERSION_RATE
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass

    def handle_increment(self, value, increment):
        """increment the input"""
        miles = self.string_to_number(value) + increment
        self.root.ids.input_number.text = str(miles)

    def string_to_number(self, string):
        """convert string to number"""
        try:
            number = float(string)
        except ValueError:
            number = 0.0
        return number




ConvertMilesToKm().run()
