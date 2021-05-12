from datetime import datetime
from threading import Timer
import time
from tkinter.constants import COMMAND, END, FALSE
import urllib.request as urllib2
import tkinter as tk
from tkinter import ttk
import time as t
from tkinter import messagebox
import googlesearch
import webbrowser
from bs4 import BeautifulSoup
import re
from urllib.request import url2pathname
from urllib.request import url2pathname
import urllib
import urllib3
import pyautogui
import requests
from datetime import date







Current_Date = datetime.now()





window = tk.Tk(className= "dash")




buttonClicked = False



window.minsize(600,400) # window size

info = False

def allinfo(info):
    if info == True:
         getresult = name.get()

    the_word = "user_id"

    x1 = "https://forum.neverlose.cc/u/" + getresult +".json"
    r = requests.get(x1, allow_redirects=False)
    soup = BeautifulSoup(r.content, 'lxml')
    words = soup.find(text=lambda text: text and the_word in text)


    string = words
    print("--------------------------------")


    print(string)


 
def gui(buttonClicked):




   if(buttonClicked == True):
    getresult = name.get()

    the_word = "user_id"

    x1 = "https://forum.neverlose.cc/u/" + getresult +".json"
    r = requests.get(x1, allow_redirects=False)
    soup = BeautifulSoup(r.content, 'lxml')
    words = soup.find(text=lambda text: text and the_word in text)


    string = words

    if(getresult.lower() == "thaiti"):
        print(name.get() + " is a harmless bitch that cant do anything~!")

    if (name.get().lower() == "longknives"):
        print("I like longknives")




  





    location = string.find("user_id", 0)
    admin = string.find("admin", 0)
    granted = string.find("granted_at", 0)
    email = (string.find("email", 0 ))
    

    falseadmin = string[admin+7 : admin+12]

    falseemail = string[email+7:email+12]

    location1 = string[location+9:location + 15]

    locationgranted = string[granted+ 13: granted+23]

    acountcreation = string[granted+53: granted + 63]

   

    

    print("--------------------------------")

    print("UID: " + location1)

    if(falseadmin == "false"):
        print(name.get() + " is not an admin")
    if(falseadmin == "true"):
        print(name.get() + " is an admin")

    if(falseemail == "false"):
            print(name.get() + " no email is associated with the account")
    else:
        print(name.get() + " phone number is: " + string[falseemail : falseemail + 20])




    







  


    


 

    print("Granted at: " + locationgranted)

    print("Acount created at: " + acountcreation)

    

 


   









   

    






   

 
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name, background='blue')
nameEntered.grid(column = 10, row = 1) 


 


button = ttk.Button(window, text = "Enter", command=lambda buttonClicked = True: gui(buttonClicked))
             
button.grid(column= 15, row = 1) 









label = ttk.Label(window, text = "Check Console for other details: ") # text
label.grid(column = 10, row = 20) 


button = ttk.Button(window, text = "All Info", command=lambda info = True: allinfo(info))
             
button.grid(column= 20, row = 1) 


 





window.mainloop()


       





       

