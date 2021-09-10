import urllib.request
import json
from urllib.request import urlopen, Request
import urllib.request


urlData = "https://wttr.in/Detroit?format=j1"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()

encoding = webURL.info().get_content_charset('utf-8')
j = json.loads(data.decode(encoding))
print(j["weather"][0]["hourly"][0]["visibilityMiles"] + " Miles")