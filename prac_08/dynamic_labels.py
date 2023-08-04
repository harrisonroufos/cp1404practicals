"""
CP1404 Practical Kivy
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """ DynamicLabels is a Kivy App for displaying names """

    def __init__(self):
        """Construct main app"""
        super().__init__()
        self.names = ["Joe Biden", "Donald Trump", "Barack Obama"]

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


app = DynamicLabels()
app.run()
