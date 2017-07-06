import webapp2
import json
import random
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        giphy_data_source = urllib2.urlopen(
             "http://api.giphy.com/v1/gifs/search?q=+ryan+gosling&api_key=dc6zaTOxFJmzC&limit=10")
        giphy_json_content = giphy_data_source.read()
        parsed_giphy_dictionary = json.loads(giphy_json_content)
        gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        self.response.write(gif_url)

app = webapp2.WSGIApplication([
     ('/', MainHandler)
], debug=True)
