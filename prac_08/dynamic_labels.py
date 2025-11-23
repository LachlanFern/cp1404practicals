from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class NameListApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_number = {"Peter": 1, "Lois": 2, "Chris": 3, "Meg": 4}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')

        for name in self.name_to_number:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


if __name__ == "__main__":
    NameListApp().run()
