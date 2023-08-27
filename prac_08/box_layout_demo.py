"""
CP1404 Practical using Kivy
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """ BoxLayoutDemo is a Kivy App for greeting entered name """
    def build(self):
        """Build the Kivy GUI"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Changes output_label text to greet input_name text"""
        print("greet")
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clears output_label and input_name texts"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
