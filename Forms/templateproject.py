import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2




class MainHandler(webapp2.RequestHandler)
    def get(self):
        guestbook_name = self.request.get('madlib')
        dictionary= {'Adjective, Noun, Name, Verb, Number, Color '}
        self.response.write{template.render(dictionary)}
class TempE()
    def get(self)
