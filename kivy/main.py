from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import json
# import pyowm
import requests


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()
    # owm = pyowm.OWM('d1e7a3acedbc6be7d78ded4620e2943b')

    def search_location(self):
        # TODO: najit jmeno mesta ve velkem jsonu
        # TODO: misto jmena mozna pouzit ID: api.openweathermap.org/data/2.5/weather?id=524901&APPID=1111111111
        # Get URL From Weather API + Input
        appid = 'd1e7a3acedbc6be7d78ded4620e2943b'
        search_template = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}"
        # search_template = "http://api.openweathermap.org/data/2.5/" + "find?q={}&type=like"
        # search_url = search_template.format(self.search_input.text)
        search_url = search_template.format('London,uk', appid)

        urlresults = (requests.get(search_url)).text

        # Converts Json to Python Dictionary
        urlresults = json.loads(urlresults)
        cities = ["{} ({})".format(urlresults["city"]["name"], urlresults["city"]["country"])]

        print cities
        # print("The user searched for '{}'".format(self.search_input.text))

    def found_location(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data

        cities = ["{}, ({})".format(d['name'], d['sys']['country']) for d in data['list']]
        self.search_results.item_strings = cities


class WeatherApp(App):
    def current_location(self):
        print("WeatherApp method")


if __name__ == '__main__':
    WeatherApp().run()