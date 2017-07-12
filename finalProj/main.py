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
import hookingin
# import model

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

class JarensHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("static/jarenssoullfoodstartup.html")



class NewHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write("different")
        base_url = "https://accounts.spotify.com/authorize/?"
        url_params = {'client_id': "ab201d1acc304ba28610b4cebc2dda42", 'response_type': "code", 'redirect_uri' : "http://localhost:12080/leek/"}
        request_url = base_url + urllib.urlencode(url_params)

        self.redirect(request_url)


class AnotherHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('soullfoodstartuppage.html')

        #logging in the app
        code=self.request.get("code")
        base_url = "https://accounts.spotify.com/api/token"
        client_id =  "ab201d1acc304ba28610b4cebc2dda42"
        client_secret = "4d06f94d19f64670b55f5f19619670ef"
        url_params = {'grant_type': "authorization_code", 'code': code, 'redirect_uri': "http://localhost:12080/leek/", 'client_id':client_id, 'client_secret':client_secret}
        data = urllib.urlencode(url_params)
        response = urllib2.urlopen(base_url, data).read()

        #loading and isolating
        parsed_dictionary = json.loads(response)
        token_type = parsed_dictionary['token_type']
        access = parsed_dictionary['access_token']
        expires = parsed_dictionary['expires_in']
        refresh = parsed_dictionary['refresh_token']
        #Getting artist id
        query_dictionary = { 'q': "Chance the Rapper", 'type': "artist"}
        calling = hookingin.callspotify("search", access, query_dictionary)
        person_id = calling['artists']['items'][0]['id']

        #self.response.write(person_id)
        # bases_url = "https://api.spotify.com/v1/recommendations"
        # header_dictionary = {'Authorization': access}
        # request = urllib2.Request(bases_url)#, headers = header_dictionary)
        # request.add_header('Authorization', "Bearer " + access)
        # response = urllib2.urlopen(request).read()
        # self.response.write(response)

        #giving recommendations for other artists
        query_dictionary = { 'seed_artists': person_id}
        calling = hookingin.callspotify("recommendations", access, query_dictionary)
        track_id = calling['tracks'][0]['id']
        artist_name = calling['tracks'][0]['artists'][0]['name']
        self.response.write(album_id)
        # self.response.write(track_id)
        # query_dictionary = { 'seed_genres': }
        # self.response.out.write(template.render())

        query_dictionary = {'Authorization': access, }

        #{u'token_type': u'Bearer', u'refresh_token': u'AQDIxy6yViN0CPQkamvE1NxqMUotUUD_CuwOMq4rEUD2IDpdca3j1rDb-xHHQ2-Sk9J4gnir1iFQfwLVRFWaWagS7Z22Dy_WX9LMygpsz9O2CInVwo9v0iQcMKN30VOH3ks', u'expires_in': 3600, u'access_token': u'BQDxbgvLYoRmhviggcmYZHeoaRuyz9umYiNeF4bDXWMtIY_WlOz4wLpH5fRwXvZjZPf0QRdbQEdNWyhJEzxG96TCvBSX0HIP50CVJg9XGAWO21z4GgltmLe0D4C8wwSFSznSpqWKR-dLPtlr_vA'}

#class SecondHandler(webapp2.RequestHandlers):
    #def get

# class SongHandler(webapp2.RequestHandler):
#     def post(self):
#         song1 = model.Song()
#         song1.name = self.request.get("name")
#         song1.name = self.request.get("artist")
#         song1.duration = int(self.request.get("duration"))
#         song1.new = bool(self.request.get("new"))
#         song1.put(
#         self.response.write("Put the song")
#         )
# class GetHandler(webapp2.RequestHandler):
#     def get(self):
#         name = self.request.get("name")
#         query = model.Song.query(model.Song.name == name)
#         one_song = query.get()


app = webapp2.WSGIApplication([
     #('/', MainHandler),
     ('/', JarensHandler),
     ('/spotify',NewHandler),
     ('/leek/', AnotherHandler),
    #  ('/storesong', SongHandler),
    #   ('/getsong', GetHandler)
], debug=True)
