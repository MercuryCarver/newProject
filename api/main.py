import webapp2
import json
import random
import urllib2
import urllib
import jinja2

jinja_environment = jinja2.Environment(
   loader=jinja2.FileSystemLoader("."))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        base_url = "http://api.giphy.com/v1/gifs/search?"
        term= self.request.get("term")
        url_params = {'q': term, 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
        template = jinja_environment.get_template('api.html')
        #giphy_response = urllib2.urlopen(
            #"http://api.giphy.com/v1/gifs/search?q=+ryan+gosling&api_key=dc6zaTOxFJmzC&limit=10")
        giphy_response = urllib2.urlopen(base_url + urllib.urlencode(url_params)).read()
        parsed_giphy_dictionary = json.loads(giphy_response)
        gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        app = webapp2.WSGIApplication

        self.response.out.write(template.render(url_params))
        self.response.write(gif_url)

#class SecondHandler(webapp2.RequestHandlers):
    #def get

app = webapp2.WSGIApplication([
     ('/', MainHandler)
], debug=True)
