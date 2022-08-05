"""
##########################################################################################################################################
#  Author   :  AHMAD RIFKY IDRUS
#  COMPANY  : PRIVATE
#  PROJECT  : decode from Osintgram
DATEDIFF( 'day',date("01/01/1970 00:00:00"),date([Timestamp]))  --> ok
##########################################################################################################################################


"""
import sys

import requests
import time
import json
import urllib
import re

namaFile = sys.argv[1]
f = open(namaFile, "r")
for txt in f:
  #print (txt)
  x = txt.split("|")
  myurl = x[2].strip()
  myurl = urllib.parse.quote_plus(myurl)
  #print (myurl)
  header1 = {
    "Connection":'keep-alive',
    "Accept-Encoding":'gzip, deflate, br'
  }
  #replace YourKey below with https://developers.google.com/maps/documentation/maps-static/get-api-key  hints --> https://www.youtube.com/watch?v=2_HZObVbe-g
  response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+myurl+'/&&key=YourKey', headers=header1)
  #response = requests.get('https://5rmv5.mocklab.io/json/1', headers=header1)

  #print("Status code: ", response.status_code)
  #print("Printing Entire Post Request")
  #print(response.json())
  #print (response.text)
  data = json.loads(response.text)
  if re.findall('lat',response.text):
   #print ("YESSSSSSSSS")
   lat = str(data['results'][0]['geometry']['location']['lat'])
   long = str(data['results'][0]['geometry']['location']['lng'])
   theLongLat = lat,',',long
   inilah = ''.join(theLongLat)
   print (inilah+","+x[3].strip())
f.close()
