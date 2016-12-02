#simple API using HTTP client library
#By hms91 

import urllib
import json

#Keeps our program in loop
while True:

    #get user's input
    address1 = raw_input('Enter Country: ')
    address2 = raw_input('Enter City: ')

    #check for empty 
    if len(address1) == "" : break
    if len(address2) == "" : break

    #url to access wunderground.com api
    #use http library to get response from wunderground.com
    #7c5e41c395b1f11a key from the site to allow us access
    url = 'http://api.wunderground.com/api/7c5e41c395b1f11a/geolookup/conditions/q/'+address1+'/'+address2+'.json'
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()

    #make sure that we received good data
    try: js = json.loads(str(data))
    except: js = None

    #assign values from returned json data 
    weather = js["current_observation"]["weather"]
    weather1 = js["current_observation"]["relative_humidity"]
    weather2 = js["current_observation"]["feelslike_string"]

    #tell the user the current weather and what it feels like
    print "The Current weather in %s %s is: %s %s It will feel like %s" % (address2, address1, weather, weather1, weather2)

