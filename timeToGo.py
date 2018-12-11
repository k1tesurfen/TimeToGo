#!/usr/bin/env python3
import json
from urllib.request import urlopen

barHtml = """
<html>
    <head>
    </head>
    <body style="padding: 3px; margin: auto; font-size: 12px;">8 in {}</body>
</html>
"""
    
url = "http://bus.fs-et.de/busSuedJson.php?limit=20"
response = urlopen(url)
data = response.read()
values = json.loads(data)
array = values['departures']
for d in array:
    if d['line']=='8':
        res=(barHtml.format(str(d['countdown'])).replace('\n', ''))
        break   
    else:
        res=barHtml.format('--').replace('\n', '')
print(res) 
print('----TEXTBAR----')
print('BARTYPE=WEB')
print('BARWIDTH=70')
