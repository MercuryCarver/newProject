import json
import urllib2
import urllib


def callspotify(endpoint, access_token, query_argument):
    bases_url = "https://api.spotify.com/v1/" + endpoint + "?"
    request_url = bases_url + urllib.urlencode(query_argument)#, headers = header_dictionary)
    request = urllib2.Request(request_url)
    request.add_header('Authorization', "Bearer " + access_token)
    response = urllib2.urlopen(request).read()
    dictionary = json.loads(response)
    return dictionary
