from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        print("The user searched for '{}'".format(self.search_input.text))


class WeatherApp(App):
    def current_location(self):
        print("WeatherApp method")


if __name__ == '__main__':
    WeatherApp().run()