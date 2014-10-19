#!/usr/bin/python

import urllib
import urllib2
import cgitb
import cgi

#import webbrowser
print "Content-Type: text/html"
print
form = cgi.FieldStorage()
url = form["name"].value

#data = urllib.urlencode(values)
req = urllib2.Request(url)
response = urllib2.urlopen(req)
page = response.read()
title_begin = page.find('<title>')
title_end = page.find('</title>')
title = page[title_begin+len('<title>'):title_end]
print "<a href="+url+">"+title+"</a>"