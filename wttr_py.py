import urllib.request
import json
from urllib.request import urlopen, Request
import urllib.request
from tkinter import *



urlData = "https://wttr.in/Detroit?format=j1"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()

encoding = webURL.info().get_content_charset('utf-8')
j = json.loads(data.decode(encoding))

#Information
LOC = (j["nearest_area"][0]["areaName"][0]["value"])
VIS = (j["weather"][0]["hourly"][0]["visibilityMiles"] + " Miles")
SUN = (j["weather"][0]["astronomy"][0]["sunrise"])
CLOUD = (j["current_condition"][0]["cloudcover"])
CHS = (j["weather"][0]["hourly"][0]["chanceofsnow"])


def fact (DEFAUL):

    TEMPLATE ="{:17}".format("| Location: ") + "{:<17}".format("| " +  DEFAUL) + ("|")
    return TEMPLATE




#formatting
LOC_format = fact(LOC)
VIS_format = fact(VIS + " Miles")
SUN_format = fact(SUN + " AM")
CLOUD_format = fact(CLOUD + " %")
CHS_format = fact(CHS + " %")



#format lines
line ="-----------------------------------"

#Printing area

print(line)
print(LOC_format)
print(SUN_format)
print(VIS_format)
print(CLOUD_format)
print(CHS_format)
print(line)
