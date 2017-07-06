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
