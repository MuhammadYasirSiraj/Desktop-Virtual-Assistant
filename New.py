# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 23:07:59 2022

@author: IT
"""


# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:00:24 2022

@author: IT
"""

import tkinter as tk
from tkinter import *
from tkinter import Tk,Label,Button,ttk,messagebox
from tkinter import PhotoImage
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import pyjokes
import smtplib
import requests
from bs4 import BeautifulSoup

screen = tk.Tk()
screen.geometry("1000x800")
screen.title("Virtual Assistant")
bg = PhotoImage(file = "Iron_Template_1.GIF")                   
lbl=Label(screen,image=bg)
lbl.pack()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
global flag
global lbl1
global lbl2
def End():
    flag =1
    screen.destroy()
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
         speak("Good Morning!")
         speak("Assalamu Alaikum, I am Jarvis Sir. Please tell me how may I help you")
    elif hour>=12 and hour<18:
         speak("Good Afternoon!")   
         speak("Assalamu Alaikum, I am Jarvis Sir. Please tell me how may I help you")
    else:
         speak("Good Evening!")  
        
         speak("Assalamu Alaikum, I am Jarvis Sir. Please tell me how may I help you")       
        
        
def listening():
            
            lbl1=Label(screen,text= "Listening...", fg ="white", bg="#000000")
            lbl1.pack()
            lbl1.place(x=150,y=150)
            
            messagebox.showinfo("Status","Listening...")
            #if lbl2.winfo_exists() ==1:
                #lbl2.config(text="")
def Recongnizing():   
            
            lbl2=Label(screen,text= "Recongnizing...", fg ="white", bg="#000000") 
            lbl2.pack()
            lbl2.place(x=700,y=150)
            #lbl1.config(text="")
            messagebox.showinfo("Status","Recongnizing...")
            
def takeCommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                
                listening()
                
                r.pause_threshold = 1
                audio = r.listen(source)
        
            try:
                Recongnizing()
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")
                speak(f"User said: {query}")
        
            except Exception as e:
                print(e)    
                print("Say that again please...")
                speak("Say that again please...")
                return "None"
            return query
        
def sendEmail(to, content):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('yasirsiraj04@gmail.com', 'Yasir_2001')
            server.sendmail('yasirsiraj04@gmail.com', to, content)
            server.close()
              
def YoutubeSearch(search):
            result = "https://www.youtube.com/results?search_query=" + search
            webbrowser.open(result)
            
def jokes():
            joke = pyjokes.get_joke('en', category = 'neutral')
            speak(joke)
                        
        
def tool():
               
        flag = 1
        wishMe()
        if flag == 1 :
        #while True:       
                query = takeCommand().lower()
                
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                    flag = 0    
                elif 'on google' in query:
                    speak('Searching...')
                    query = query.replace("on google", "")
                    results = webbrowser.open(query, "google.com")
                    print(results)
                    speak(results)
                    flag =0
                elif 'on youtube' in query:
                    speak('Searching...')
                    query = query.replace("on youtube", "")
                    results = YoutubeSearch(query)
                    speak(results)
                    flag =0    
                elif "temperature" in query:
                    speak("In which City Sir?")
                    city = takeCommand().lower()
                    search = f"temperature in {city} "
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_="BNeawe").text
                    speak(f"Current {search} is {temp}")
                    flag =0
                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
                    flag =0
                elif 'open google' in query:
                    webbrowser.open("google.com")
                    flag =0
                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")   
                    flag =0
                elif 'play music' in query:
                    music_dir = 'E:\\Non Critical\\songs\\Favorite Songs'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))
                    flag =0
                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")
                    flag =0
                elif 'joke' in query:
                    jokes()
                    flag =0
                elif 'send email' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "yasir.gameryt@gmail.com"    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                        flag =0
                    except Exception as e:
                        print(e)
                        speak("Sorry my friend yasir bhai. I am not able to send this email")
                        flag =0
                if 'stop' in query:
                  
                   screen.destroy()
                   #break



btn1=Button(screen, text="Run",bg="#000000",fg="white",width=15,height=3, relief= "raised", command = tool)
btn2=Button(screen, text="Exit",bg="#000000",fg="white",width=15,height=3, relief= "raised", command = End)
btn1.place(x=850,y=500)
btn2.place(x=850,y=600)



screen.mainloop()              
