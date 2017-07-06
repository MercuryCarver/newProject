#!/usr/bin/env pythonWha
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


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader("templates"))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        my_vars={"name": "CSSIer"}
        template = jinja_environment.get_template('template.html')
        dictionary = {'template_name': self.request.get('name')}
        self.response.out.write(template.render(dictionary))
        app = webapp2.WSGIApplication

class MainHandler(webapp2.RequestHandler):
    def get(self):
        guestbook_name = self.request.get('madlib')
        #dictionary= {'Adjective, Noun, Name, Verb, Number, Color '}
        dictionary= {'noun': 'car'}
        jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
        app = webapp2.WSGIApplication
        templates = jinja_environment.get_template('templateproject.html')
        self.response.write(templates.render(dictionary))






class PassHandler(webapp2.RequestHandler):
    def post(self):
        real_name = "malik"
        real_pass = "123abc"
        username = self.request.get("username")
        password = self.request.get("password")
        self.response.write(username + "  " + password)
        if password == real_pass and username == real_name:
            self.response.write

            ("Login Successful")
        else:
            self.response.write("Password not recognized")




class FormHandler(webapp2.RequestHandler):
    def get(self):
        Good=self.request.get('color')
        self.response.write('Is this your favorite color ' + Good)
        Cool=self.request.get('name')
        self.response.write('Are you sure this is your name ' + Cool)
        Secret=self.request.get('firstName')
        self.response.write('Are you sure you entered correctly ' + Secret)
        Restaraunt=self.request.get('oliveGarden')
        self.response.write('Whats your favorite food from ' + Restaraunt)
        Radio=self.request.get('station')
        self.response.write('Do you like ' + Radio)




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/submission', FormHandler),
    ('/login', PassHandler)
], debug=True)
