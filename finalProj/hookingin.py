import json
import urllib2
import urllib
import logging


def callspotify(endpoint, access_token, query_argument):
    bases_url = "https://api.spotify.com/v1/" + endpoint + "?"
    request_url = bases_url + urllib.urlencode(query_argument)#, headers = header_dictionary)
    request = urllib2.Request(request_url)
    request.add_header('Authorization', "Bearer " + access_token)
    response = urllib2.urlopen(request).read()
    dictionary = json.loads(response)
    return dictionary

def callyoutube(query):
    bases_url = "https://www.googleapis.com/youtube/v3/search" + "?"
    query_dictionary = { 'q': query,
    'key':"AIzaSyAtPFVJwmWolpn75QI3g0ZeNI2er0r2_Io",
    'part':"snippet",
    "maxResults":1,
    'videoSyndicated': "true",
    'type':"video"}
    request_url = bases_url + urllib.urlencode(query_dictionary)#, headers = header_dictionary)
    logging.info(request_url)

    request = urllib2.Request(request_url)
    response = urllib2.urlopen(request).read()
    dictionary = json.loads(response)
    return dictionary
