#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi

target = 0

form = cgi.FieldStorage()

print "Content-Type: text/html\n\n"

if "target" in form:
    target = form["target"].value
    if target.isdigit():
        f = open('target.txt', 'w+')
        f.write(str(target))
        f.close()
        print "Your target is now: <br/>" + str(target) + " m"
    else:
        print "Invalid value"

else:
    print "no value"
