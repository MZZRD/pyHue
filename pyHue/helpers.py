import requests


class Light:

    def __init__(self, url):
        self.url = url

        # get state from api
        self.light = requests.get(url).json()
        state = self.light.get("state")

        self.on = state.get("on")
        self.bri = state.get("bri")
        self.hue = state.get("hue")
        self.sat = state.get("sat")
        self.effect = state.get("effect")

    def toggle(self):
        self.on = not self.on
        body = '{"on":%s}' % str(self.on).lower()
        print(body)
        r = requests.put("%s/state" % self.url, body)
