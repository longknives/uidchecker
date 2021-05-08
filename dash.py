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



window = tk.Tk()

buttonClicked = False


window.title("dash(BETA)") # title
window.minsize(600,400) # window size


 
def gui(buttonClicked):


   if(buttonClicked == True):
    getresult = name.get()

    the_word = "user_id"

    x1 = "https://forum.neverlose.cc/u/" + getresult +".json"
    r = requests.get(x1, allow_redirects=False)
    soup = BeautifulSoup(r.content, 'lxml')
    words = soup.find(text=lambda text: text and the_word in text)


    string = words
    print("Important information" + string[0:1000])
    print(" ")
    print(" ")
    print(" ")
    print("ALL INFORMATION")
    print(string)


    






   

 
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name)# box
nameEntered.grid(column = 10, row = 1) # location


 


button = ttk.Button(window, text = "Enter", command=lambda buttonClicked = True: gui(buttonClicked))
             
button.grid(column= 15, row = 1) # button





label = ttk.Label(window, text = "user_id shows uid~!") # text
label.grid(column = 10, row = 20) 




 

window.mainloop()


       

