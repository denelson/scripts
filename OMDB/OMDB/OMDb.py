import json
import requests
import xml.etree.cElementTree as ET
import datetime

def getMovieDetailsByTitle(title):
    
    url = "http://www.omdbapi.com/?t="+title+"&plot=short&r=json"
    response = requests.get(url)
    
    if (response.ok):
        
        print "fetching data from omdbapi.com"
        jData = json.loads(response.content)
        #print jData +'\n'
        
  
       
        
        
        root = ET.Element("Movie")
        name = ET.SubElement(root,"Name")
        releaseDate = ET.SubElement(root,"ReleaseDate")
        genre = ET.SubElement(root,"Genre")
        director = ET.SubElement(root,"Director")
        rating = ET.SubElement(root,"Rating")
        plot = ET.SubElement(root,"Plot")
        
        print jData["Released"]
        name.text = title
        releaseDate.text = datetime.datetime.strptime(jData["Released"],"%d %b %Y").strftime("%Y-%m-%d")
        genre.text = jData["Genre"].split(',')[0]
        director.text =  jData["Director"].split(',')[0]
        rating.text = jData["imdbRating"]
    
        tree = ET.ElementTree(root)
        ET.dump(root)
    
title = raw_input("Enter title:")

getMovieDetailsByTitle(title)
