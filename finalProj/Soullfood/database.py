from google.appengine.ext import ndb
class Song(ndb.Model):
  name = ndb.StringProperty()
  artist = ndb.StringProperty()
  duration = ndb.IntegerProperty()
  new = ndb.BooleanProperty()
