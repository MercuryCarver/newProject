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
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

    def get(self):
        guestbook_name = self.request.get('madlib')
        #dictionary= {'Adjective, Noun, Name, Verb, Number, Color '}
        app = webapp2.WSGIApplication
        templates = jinja_environment.get_template('homepage.html')
        mg3= self.request.get("Mood")
        mg = self.request.get("Genre")
        mg2= self.request.get("Weather")
        dictionary= {"mg3":mg2 , "mg": mg3, "mg2": mg}
        self.response.write(templates.render(dictionary))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
