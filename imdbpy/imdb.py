#!/usr/bin/python
import json
import urllib2
    
        
def search(name, year="", length="short"):
    url = "http://www.omdbapi.com/?t=%s&y=%s&plot=%s&r=json" %(name, year, length)
    result = json.load(urllib2.urlopen(url))
    return result
