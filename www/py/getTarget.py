#!/usr/bin/python
# -*- coding: utf-8 -*-

f = open("target.txt", "r")
val = f.read()
f.close()

print "Content-Type: text/html\n\n"
print val
