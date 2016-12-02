#simple API using HTTP client library
#By hms91 

import requests
import json
#key from wunderground.com to enable the use of their weather API
key = "[7c5e41c395b1f11a]"

#get a response from wunderground.com
data = requests.get('http://api.wunderground.com/api/'+ key +'/geolookup/conditions/q/Kenya/Nairobi.json').json()

#set the current city to the location variable
location = data['location']['city']

#set the temperature from our json to temp_c
temp_c = data['current_observation']['temp_c']

#print out the results
print "The current temperature in %s is: %s C" % (location, temp_c)

