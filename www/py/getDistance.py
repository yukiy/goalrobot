#!/usr/bin/python
# -*- coding: utf-8 -*-

#---GET  /getDistance.py?date=[yyyymmdd]&activity=[cycling/transport/walking/total]&type=[json]

import cgi
import json
import urllib
import urllib2
import datetime

walking = 0
transport = 0
cycling = 0
total = 0
date = ""
returnType = ""
activity = ""

form = cgi.FieldStorage()

#---get date (default: today's date)
if "date" in form:
    date = form["date"].value
else:
    today = datetime.datetime.today()
    date = str(today.year) + str(today.month) + str(today.day)

#---get return type (default: html)
if "type" in form and form["type"].value == "json":
    returnType = "json"

#---get activity (default: total)
if "activity" in form:
    activity = form["activity"].value

#---create URL for API
domain = "https://api.moves-app.com"
api = "/api/1.1/user/summary/daily/"
url = domain + api + date

#---get token -> https://dev.moves-app.com/docs/authentication
access_token = "YOUR_ACCESS_TOKEN"
val = {
    "access_token": access_token
}
param = urllib.urlencode(val)
requrl = url + "?" + param


#---place data
res = urllib2.urlopen(requrl)
data = cgi.FieldStorage()
data = json.loads(res.read())
if len(data[0]["summary"]) > 2:
    cycling = data[0]["summary"][2]["distance"]
if len(data[0]["summary"]) > 1:
    transport = data[0]["summary"][1]["distance"]
if len(data[0]["summary"]) > 0:
    walking = data[0]["summary"][0]["distance"]

total = walking + transport + cycling


if returnType == "json":
    if activity == "cycling":
        myJson = json.dumps([cycling], indent=2)
    elif activity == "transport":
        myJson = json.dumps([transport], indent=2)
    elif activity == "walking":
        myJson = json.dumps([walking], indent=2)
    elif activity == "total":
        myJson = json.dumps([total], indent=2)
    else:
        myJson = json.dumps({"cycling": cycling,
                            "transport": transport,
                            "walking": walking,
                            "total": total},
                            indent=2)

    print "Content-type: application/json\n"
    print myJson

else:
    print "Content-Type: text/html\n\n"

    if activity == "cycling":
        print str(cycling)
    elif activity == "transport":
        print str(transport)
    elif activity == "walking":
        print str(walking)
    elif activity == "total":
        print str(total)
    else:
        print "cycling  = " + str(cycling) + "<br/>"
        print "transport  = " + str(transport) + "<br/>"
        print "walking  = " + str(walking) + "<br/>"
        print "total = " + str(total) + "<br/>"
