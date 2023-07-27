"""
CP1404 Practical Kivy
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILE_TO_KILOMETRE_CONVERSION = 1.60934


class ConvertMilesToKilometres(App):
    conversion_result = StringProperty()
    user_input_number = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.conversion_result = ""
        self.user_input_number = ""
        return self.root

    def handle_conversion(self, miles):
        try:
            conversion = float(miles) * MILE_TO_KILOMETRE_CONVERSION
            self.conversion_result = str(conversion)
        except ValueError:
            self.conversion_result = "0.0"

    def handle_increment(self, miles, increment):
        try:
            miles_incremented = float(miles) + increment
            self.user_input_number = str(miles_incremented)
        except ValueError:
            self.user_input_number = str(increment)


app = ConvertMilesToKilometres()
app.run()
