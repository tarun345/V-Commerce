import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib

from .models import *

# required codes for speak function
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speak function will pronounce string passed in argument
def speak(text):
    engine.say(text)
    engine.runAndWait()

# takeCommand function is used to take the command from user by microhone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("listning...")
        # speak("listning...")
        r.pause_threshold= 2
        audio = r.listen(source)   
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f" said :{query}\n")
    except Exception as e:
        print("did not get it, say that again")
        query = ""

    return query

#--------- to search a product from the database -------------------------------        
def search(query):
    results = Product.objects.filter(name__icontains=query).distinct()
    return results

    
  
