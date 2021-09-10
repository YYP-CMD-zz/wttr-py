from tkinter import *
from tkinter import messagebox
import urllib.request
import json
from urllib.request import urlopen, Request
import urllib.request
from tkinter import *




def buttonBerechnenClick():
   # try:
        #data
        city = City.get()
        
        
        
   

        city = city.replace("ü", "ue")

        city = city.replace("ä", "ae")

        city = city.replace("ö", "oe")


        
   



        urlData = "https://wttr.in/" + city + "?format=j1"
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


        def fact (DEFAUL, NAME):

            TEMPLATE ="{:17}".format("| " + NAME) + "{:<17}".format("| " +  DEFAUL) + ("|")
            return TEMPLATE




        #formatting
        LOC_format = fact(LOC, "Location:")
        VIS_format = fact(VIS + " Miles" , "Visibility:")
        SUN_format = fact(SUN + " AM", "Sunrise:")
        CLOUD_format = fact(CLOUD + " %", "Cloudly:")
        CHS_format = fact(CHS + " %", "Chance of Snow:")



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

   # except:
      #  messagebox.showerror('Error', 'Invalid Input')



# Fenster
tkFenster = Tk()
tkFenster.title('wttr')
tkFenster.geometry('258x195')
# Label mit Aufschrift Gewicht
labelGewicht = Label(master=tkFenster, bg='#FFCFC9', text='Enter you Location:')
labelGewicht.place(x=54, y=24, width=100, height=27)
# Entry für das Gewicht
City = Entry(master=tkFenster, bg='white')
City.place(x=164, y=24, width=40, height=27)

buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='Start',
                         command=buttonBerechnenClick)
buttonBerechnen.place(x=54, y=104, width=100, height=27)

# Aktivierung des Fensters
tkFenster.mainloop()
