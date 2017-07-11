#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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
        template = jinja_environment.get_template('soullfoodstartuppage.html')
        term= self.request.get("term")
        url_params = {'q': term, 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
        #giphy_response = urllib2.urlopen(
            #"http://api.giphy.com/v1/gifs/search?q=+ryan+gosling&api_key=dc6zaTOxFJmzC&limit=10")
        #giphy_response = urllib.urlopen(base_url + urllib.urlencode(url_params)).read()
        #parsed_giphy_dictionary = json.loads(giphy_response)
        #gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        # app = webapp2.WSGIApplication
        #
        # self.response.out.write(template.render(url_params))
        # self.response.write(gif_url)

class NewHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write("different")
        base_url = "https://accounts.spotify.com/authorize/?"
        url_params = {'client_id': "ab201d1acc304ba28610b4cebc2dda42", 'response_type': "code", 'redirect_uri' : "http://localhost:12080/leek/"}
        request_url = base_url + urllib.urlencode(url_params)
        redirect_uri = 'REDIRECT_URI'; "http://localhost:12080/leek/"
        scopes = 'user-read-private user-read-email'

        self.redirect(request_url)


class AnotherHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("does it work")
        code=self.request.get("code")
        base_url = "https://accounts.spotify.com/api/token"
        client_id =  "ab201d1acc304ba28610b4cebc2dda42"
        client_secret = "4d06f94d19f64670b55f5f19619670ef"
        url_params = {'grant_type': "authorization_code", 'code': code, 'redirect_uri': "http://localhost:12080/leek/", 'client_id':client_id, 'client_secret':client_secret}
        data = urllib.urlencode(url_params)
        response = urllib2.urlopen(base_url, data).read()
        parsed_dictionary = json.loads(response)
        token_type = parsed_dictionary['token_type']
        access = parsed_dictionary['access_token']
        expires = parsed_dictionary['expires_in']
        refresh = parsed_dictionary['refresh_token']
        bases_url = "https://api.spotify.com/v1/browse/categories"
        header_dictionary = {'Authorization': access}
        request = urllib2.Request(bases_url)#, headers = header_dictionary)
        request.add_header('Authorization', "Bearer " + access)
        response = urllib2.urlopen(request).read()
        self.response.write(response)



        #{u'token_type': u'Bearer', u'refresh_token': u'AQDIxy6yViN0CPQkamvE1NxqMUotUUD_CuwOMq4rEUD2IDpdca3j1rDb-xHHQ2-Sk9J4gnir1iFQfwLVRFWaWagS7Z22Dy_WX9LMygpsz9O2CInVwo9v0iQcMKN30VOH3ks', u'expires_in': 3600, u'access_token': u'BQDxbgvLYoRmhviggcmYZHeoaRuyz9umYiNeF4bDXWMtIY_WlOz4wLpH5fRwXvZjZPf0QRdbQEdNWyhJEzxG96TCvBSX0HIP50CVJg9XGAWO21z4GgltmLe0D4C8wwSFSznSpqWKR-dLPtlr_vA'}

#class SecondHandler(webapp2.RequestHandlers):
    #def get

app = webapp2.WSGIApplication([
     #('/', MainHandler),
     ('/', NewHandler),
     ('/leek/', AnotherHandler),
], debug=True)
