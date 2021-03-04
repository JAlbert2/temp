import cgi
from .models import xapiRaw
form = cgi.FieldStorage()
g = form.getvalue('gorilla')
d = form.getvalue('dolphin')
f = form.getvalue('fox')
file = open('file.txt','w')
file.write(str(g))
file.write(str(d))
file.write(str(f))
file.close
score = 0

statement = '''{"actor":{"account":{"name":"[Jonah]",”mbox”:”[sparkedscience0@gmail.com],"homePage":"[http://sperkedscience.com]"},"objectType":"Agent"},
"verb":{"id":"[testMC]","display":{"en-US":"[answered]"}},
"object":{"id":"[testMC]","objectType":"Activity","definition":{"extensions":{"http://h5p.org/x-api/h5p-local-content-id":[testMC]},"name":{"en-US":"[testMC]"}}"interactionType":"choice","correctResponsesPattern":["[x]"],"choices":[{"id":"1","description":{"en-US":"[orilla\\n"}},{"id":"1","description":{"en-US":"Dolphin\\n"}},{"id":"3","description":{"en-US":"Fox\\n"}}]},
"context":{"contextActivities":{"category":[{"id":"[LinkToLibrary]”,"objectType":"Activity"}]}},
"result":{"score":{"min":[0],"max":[1],"raw":'''+str(score)+'''},"completion":[completion],"success":[success],"response":"[answerChoice]"}}'''