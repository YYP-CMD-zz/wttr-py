import urllib.request
import json
from urllib.request import urlopen, Request
import urllib.request

urlData = "https://wttr.in/Detroit?format=j1"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()

encoding = webURL.info().get_content_charset('utf-8')
j = json.loads(data.decode(encoding))

#Information
LOC = (j["nearest_area"][0]["areaName"][0]["value"])
VIS = (j["weather"][0]["hourly"][0]["visibilityMiles"] + " Miles")
SUN = (j["weather"][0]["astronomy"][0]["sunrise"])


#formatting
LOC_format = "{:15}".format("| Location:: ") + "{:<15}".format("| " + LOC) + ("|")
VIS_format ="{:15}".format("| Visibilty: ") + "{:<15}".format("| " + VIS) + ("|")
SUN_format ="{:15}".format("| Sunrise: ") + "{:<15}".format("| " + SUN) + ("|")





#format lines
test ="------------------------------"

#Printing area

print(test)
print(LOC_format)
print(SUN_format)
print(VIS_format)
print(test)
