from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class AddLocationForm(BoxLayout):
    def search_location(self):
        print("Explicit is better than implicit.")


class WeatherApp(App):
    def current_location(self):
        print("WeatherApp method")


if __name__ == '__main__':
    WeatherApp().run()