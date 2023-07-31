# Importing necessary modules
import sys
from sys import exit
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import time
import instaloader
import pyautogui
import PyPDF2
from pywikihow import search_wikihow
import speedtest
from pytube import YouTube
import qrcode
import subprocess
import os
from Recordings import Record_Option
from PIL import ImageGrab
import pyaudio
import wave
import numpy as np 
from PhoneNumer import Phonenumber_location_tracker
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie, QImage
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisGUI import Ui_JarvisUi
from state import state
import cv2
import random
from requests import get
import smtplib
import psutil
from datetime import datetime as date


# Initializing text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Importing required libraries
import speech_recognition as sr
from PyQt5.QtCore import QThread

# Custom QThread class for running the main functionality in a separate thread
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    # Overridden run method to execute the thread
    def run(self):
        self.Intro()  # Call the Intro method when the thread starts

    # Method to listen and recognize user's speech command
    def take_Command(self):
        try:
            listener = sr.Recognizer()
            with sr.Microphone() as source:

                print('Listening....')
                listener.pause_threshold = 1  # Set pause threshold for speech recognition
                voice = listener.listen(source, timeout=4, phrase_time_limit=7)  # Listen for user's voice
                print("Recognizing...")
                command1 = listener.recognize_google(voice, language='en-in')  # Convert voice to text using Google's speech recognition
                command1 = command1.lower()  # Convert the recognized text to lowercase for easier processing

                if 'jarvis' in command1:  # Check if the command contains the word 'jarvis'
                    command1 = command1.replace('jarvis', '')  # Remove 'jarvis' from the command for better accuracy

            return command1  # Return the recognized command
        except:
            return 'None'  # Return 'None' if there was an error during speech recognition

    def run_jarvis(self):
        self.wish()
        self.talk('Hello boss I am jarvis your AI assistant. Please tell me how can I help you?')
        while True:
            self.command = self.take_Command() 
            print(self.command)
            if ('play a song' in self.command) or ('youtube' in self.command) or ("download a song" in self.command) or ("download song" in self.command) : 
                self.yt(self.command) 

            elif ('your age' in self.command) or ('are you single'in self.command) or ('are you there' in self.command) or ('tell me something' in self.command) or ('thank you' in self.command) or ('in your free time' in self.command) or ('I love you' in self.command) or ('can you hear me' in self.command) or ('do you ever get tired' in self.command):
                self.Fun(self.command)
            elif 'time' in self.command : 
                self.Clock_time(self.command)
            elif (('hi' in self.command) and len(self.command)==2) or ((('hai' in self.command) or ('hey' in self.command)) and len(self.command)==3) or (('hello' in self.command) and len(self.command)==5):
                self.comum(self.command)
            elif ('what can you do' in self.command) or ('your name' in self.command) or ('my name' in self.command) or ('university name' in self.command):
                self.Fun(self.command)
            elif ('joke'in self.command) or ('date' in self.command):
                self.Fun(self.command)

            elif ("college time table" in self.command) or ("schedule" in self.command):
                self.shedule() 

            elif ("today" in self.command):
                day = self.Cal_day()
                self.talk("Today is "+day)

            elif ("meeting" in self.command):
                self.talk("Ok sir opening meeet")
                webbrowser.open("https://meeting/")

            elif ('silence' in self.command) or ('silent' in self.command) or ('keep quiet' in self.command) or ('wait for' in self.command) :
                self.silenceTime(self.command)

            elif ('facebook' in self.command) or ('whatsapp' in self.command) or ('instagram' in self.command) or ('twitter' in self.command) or ('discord' in self.command) or ('social media' in self.command):
                self.social(self.command)

            elif ('hotstar' in self.command) or ('prime' in self.command) or ('netflix' in self.command):
                self.OTT(self.command)

            elif ('online classes'in self.command):
                self.OnlineClasses(self.command)

            elif ('open teams'in self.command) or ('open stream'in self.command) or ('open sharepoint'in self.command) or('open outlook'in self.command)or('open amrita portal'in self.command)or('open octave'in self.command):
                self.college(self.command)

            elif ('wikipedia' in self.command) or ('what is meant by' in self.command) or ('tell me about' in self.command) or ('who the heck is' in self.command):
                self.B_S(self.command)

            elif ('open google'in self.command) or ('open edge'in self.command) :
                self.brows(self.command)

            elif ('open gmail'in self.command) or('open maps'in self.command) or('open calender'in self.command) or('open documents'in self.command )or('open spredsheet'in self.command) or('open images'in self.command) or('open drive'in self.command) or('open news' in self.command):
                self.Google_Apps(self.command)

            elif ('open github'in self.command) or ('open gitlab'in self.command) :
                self.open_source(self.command)

            elif ('slides'in self.command) or ('canva'in self.command) :
                self.edit(self.command)

            elif ('open calculator'in self.command) or ('open notepad'in self.command) or ('open paint'in self.command) or ('open online classes'in self.command) or ('open discord'in self.command) or ('open ltspice'in self.command) or ('open editor'in self.command) or ('open spotify'in self.command) or ('open steam'in self.command) or ('open media player'in self.command):
                self.OpenApp(self.command)

            elif ('close calculator'in self.command) or ('close notepad'in self.command) or ('close paint'in self.command) or ('close discord'in self.command) or ('close ltspice'in self.command) or ('close editor'in self.command) or ('close spotify'in self.command) or ('close steam'in self.command) or ('close media player'in self.command):
                self.CloseApp(self.command)

            elif ('flipkart'in self.command) or ('amazon'in self.command) :
                self.shopping(self.command)

            elif ('where I am' in self.command) or ('where we are' in self.command):
                self.locaiton()

            elif ('command prompt'in self.command) :
                self.talk('Opening command prompt')
                os.system('start cmd')

            elif ('instagram profile' in self.command) or("profile on instagram" in self.command):
                self.Instagram_Pro()

            elif ('take screenshot' in self.command)or ('screenshot' in self.command) or("take a screenshot" in self.command):
                self.scshot()

            elif ("read pdf" in self.command) or ("pdf" in self.command):
                self.pdf_reader()

            elif "activate mod" in self.command:
                self.How()

            elif ("volume up" in self.command) or ("increase volume" in self.command):
                pyautogui.press("volumeup")
                self.talk('volume increased')

            elif ("volume down" in self.command) or ("decrease volume" in self.command):
                pyautogui.press("volumedown")
                self.talk('volume decreased')

            elif ("volume mute" in self.command) or ("mute the sound" in self.command) :
                pyautogui.press("volumemute")
                self.talk('volume muted')

            elif ("open mobile cam" in self.command):
                self.Mobilecamra()

            elif ('web cam'in self.command) :
                self.webCam()

            elif("create a new contact" in self.command):
                self.AddContact()

            elif("number in contacts" in self.command):
                self.NameIntheContDataBase(self.command)

            elif("display all the contacts" in self.command):
                self.Display()

            elif ("covid" in self.command) or  ("corona" in self.command) or  ("corona updates" in self.command):
                self.talk("Boss which state covid 19 status do you want to check?")
                s = self.take_Command()
                self.Covid(s)

            elif ("recording" in self.command) or ("screen recording" in self.command) or ("voice recording" in self.command):
                try:
                    self.talk("Boss press q key to stop recordings")
                    option = self.command
                    Record_Option(option=option)
                    self.talk("Boss recording is being saved")
                except:
                    self.talk("Boss an unexpected error occured couldn't start screen recording")

            elif ("track" in self.command) or ("track a mobile number" in self.command):
                self.talk("Boss please enter the mobile number with country code")
                try:
                    location,servise_prover,lat,lng=Phonenumber_location_tracker()
                    self.talk(f"Boss the mobile number is from {location} and the service provider for the mobile number is {servise_prover}")
                    self.talk(f"latitude of that mobile nuber is {lat} and longitude of that mobile number is {lng}")
                    print(location,servise_prover)
                    print(f"Latitude : {lat} and Longitude : {lng}")
                    self.talk("Boss location of the mobile number is saved in Maps")
                except:
                    self.talk("Boss an unexpected error occured couldn't track the mobile number")

            elif 'music' in self.command:
                try:
                    music_dir = 'E:\\music' 
                    songs = os.listdir(music_dir)
                    for song in songs:
                        if song.endswith('.mp3'):
                            os.startfile(os.path.join(music_dir, song))
                except:
                    self.talk("Boss an unexpected error occured")

            elif 'ip address' in self.command:
                ip = get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                self.talk(f"your IP address is {ip}")

            elif ('send a message' in self.command):
                self.whatsapp(self.command)

            elif 'send email' in self.command:
                self.verifyMail()

            elif "temperature" in self.command:
                self.temperature()

            elif "create a qr code" in self.command:
                self.qrCodeGenerator()

            elif "internet speed" in self.command:
                self.InternetSpeed()

            elif ("you can sleep" in self.command) or ("sleep now" in self.command):
                self.talk("Okay boss, I am going to sleep you can call me anytime.")
                break

            elif ("wake up" in self.command) or ("get up" in self.command):
                self.talk("boss, I am not sleeping, I am in online, what can I do for u")

            elif ("goodbye" in self.command) or ("get lost" in self.command):
                self.talk("Thanks for using me boss, have a good day.")
                sys.exit()

            elif ('system condition' in self.command) or ('condition of the system' in self.command):
                self.talk("checking the system condition")
                self.condition()

            elif ('tell me news' in self.command) or ("tell me today's news" in self.command) or ("the news" in self.command) or ("todays news" in self.command):
                self.talk("Please wait boss, featching the latest news")
                self.news()

            elif ('shutdown the system' in self.command) or ('down the system' in self.command):
                self.talk("Boss shutting down the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /s /t 5")

            elif 'restart the system' in self.command:
                self.talk("Boss restarting the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /r /t 5")

            elif 'sleep the system' in self.command:
                self.talk("Boss the system is going to sleep")
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")

    def Intro(self):
        while True:
            self.permission = self.take_Command()
            print(self.permission)
            if ("wake up" in self.permission) or ("get up" in self.permission):
                self.run_jarvis()
            elif ("goodbye" in self.permission) or ("get lost" in self.permission):
                self.talk("Thanks for using me boss, have a good day")
                sys.exit()

    def talk(self,text):
        engine.say(text)
        engine.runAndWait()

    def wish(self):
        hour = int(datetime.datetime.now().hour)
        t = time.strftime("%I:%M %p")
        day = self.Cal_day()
        print(t)
        if (hour>=0) and (hour <=12) and ('AM' in t):
            self.talk(f'Good morning boss, its {day} and the time is {t}')
        elif (hour >= 12) and (hour <= 16) and ('PM' in t):
            self.talk(f"good afternoon boss, its {day} and the time is {t}")
        else:
            self.talk(f"good evening boss, its {day} and the time is {t}")

    def temperature(self):
        IP_Address = get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        search = f"temperature in {city}"
        url_1 = f"https://www.google.com/search?q={search}"
        r = get(url_1)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        self.talk(f"current {search} is {temp}")

    def qrCodeGenerator(self):
        self.talk(f"Boss enter the text/link that you want to keep in the qr code")
        input_Text_link = input("Enter the Text/Link : ")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=4,
        )
        QRfile_name = (str(datetime.datetime.now())).replace(" ","-")
        QRfile_name = QRfile_name.replace(":","-")
        QRfile_name = QRfile_name.replace(".","-")
        QRfile_name = QRfile_name+"-QR.png"
        qr.add_data(input_Text_link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"QRCodes\{QRfile_name}")
        self.talk(f"Boss the qr code has been generated")

    def Mobilecamra(self):
        import urllib.request
        import numpy as np
        try:
            self.talk(f"Boss openinging mobile camera")
            URL = "http://_IP_Webcam_IP_address_/shot.jpg" 
            while True:
                imag_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img = cv2.imdecode(imag_arr,-1)
                cv2.imshow('IPWebcam',img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    self.talk(f"Boss closing mobile camera")
                    break
            cv2.destroyAllWindows()
        except Exception as e:
            print("Some error occured")

    def webCam(self):    
        self.talk('Opening camera')
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('web camera',img)
            k = cv2.waitKey(50)
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

    def Covid(self,s):
        try:
            from covid_india import states
            details = states.getdata()
            if "check in" in s:
                s = s.replace("check in","").strip()
                print(s)
            elif "check" in s:
                s = s.replace("check","").strip()
                print(s)
            elif "tech" in s:
                s = s.replace("tech","").strip()
            s = state[s]
            ss = details[s]
            Total = ss["Total"]
            Active = ss["Active"]
            Cured = ss["Cured"]
            Death = ss["Death"]
            print(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
            self.talk(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
            time.sleep(5)
            self.talk("Boss do you want any information of other states")
            I = self.take_Command()
            print(I)
            if ("check" in I):
                self.Covid(I)
            elif("no" in I):
                self.talk("Okay boss stay home stay safe")
            else:
                self.talk("Okay boss stay home stay safe")
        except:
            self.talk("Boss some error occured, please try again")
            self.talk("Boss do you want any information of other states")
            I = self.take_Command()
            if("yes" in I):
                self.talk("boss, Which state covid status do u want to check")
                Sta = self.take_Command()
                self.Covid(Sta)
            elif("no" in I):
                self.talk("Okay boss stay home stay safe")
            else:
                self.talk("Okay boss stay home stay safe")

    def whatsapp(self,command):
        try:
            command = command.replace('send a message to','')
            command = command.strip()
            name,numberID,F = self.SearchCont(command)
            if F:
                print(numberID)
                self.talk(f'Boss, what message do you want to send to {name}')
                message = self.take_Command()
                hour = int(datetime.datetime.now().hour)
                min = int(datetime.datetime.now().minute)
                print(hour,min)
                if "group" in command:
                    kit.sendwhatmsg_to_group(numberID,message,int(hour),int(min)+1)
                else:
                    kit.sendwhatmsg(numberID,message,int(hour),int(min)+1)
                self.talk("Boss message have been sent")
            if F==False:
                self.talk(f'Boss, the name not found in our data base, shall I add the contact')
                AddOrNot = self.take_Command()
                print(AddOrNot)
                if ("yes" in AddOrNot) or ("add" in AddOrNot) or ("yeah" in AddOrNot) or ("yah" in AddOrNot):
                    self.AddContact()
                elif("no" in AddOrNot):
                    self.talk('Ok Boss')
        except:
            print("Error occured, please try again")

    def AddContact(self):
        self.talk(f'Boss, Enter the contact details')
        name = input("Enter the name :").lower()
        number = input("Enter the number :")
        NumberFormat = f'"{name}":"+91{number}"'
        ContFile = open("Contacts.txt", "a") 
        ContFile.write(f"{NumberFormat}\n")
        ContFile.close()
        self.talk(f'Boss, Contact Saved Successfully')

    def SearchCont(self,name):
        with open("Contacts.txt","r") as ContactsFile:
            for line in ContactsFile:
                if name in line:
                    print("Name Match Found")
                    s = line.split("\"")
                    return s[1],s[3],True
        return 0,0,False

    def Display(self):
        ContactsFile = open("Contacts.txt","r")
        count=0
        for line in ContactsFile:
            count+=1
        ContactsFile.close()
        ContactsFile = open("Contacts.txt","r")
        self.talk(f"Boss displaying the {count} contacts stored in our data base")    
        for line in ContactsFile:
            s = line.split("\"")
            print("Name: "+s[1])
            print("Number: "+s[3])
        ContactsFile.close()

    def NameIntheContDataBase(self,command):
        line = command
        line = line.split("number in contacts")[0]
        if("tell me" in line):
            name = line.split("tell me")[1]
            name = name.strip()
        else:
            name= line.strip()
        name,number,bo = self.SearchCont(name)
        if bo:
            print(f"Contact Match Found in our data base with {name} and the mboile number is {number}")
            self.talk(f"Boss Contact Match Found in our data base with {name} and the mboile number is {number}")
        else:
            self.talk("Boss the name not found in our data base, shall I add the contact")
            AddOrNot = self.take_Command()
            print(AddOrNot)
            if ("yes add it" in AddOrNot)or ("yeah" in AddOrNot) or ("yah" in AddOrNot):
                self.AddContact()
                self.talk(f'Boss, Contact Saved Successfully')
            elif("no" in AddOrNot) or ("don't add" in AddOrNot):
                self.talk('Ok Boss')

    def InternetSpeed(self):
        self.talk("Wait a few seconds boss, checking your internet speed")
        st = speedtest.Speedtest()
        dl = st.download()
        dl = dl/(1000000) 
        up = st.upload()
        up = up/(1000000)
        print(dl,up)
        self.talk(f"Boss, we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")

    def How(self):
        self.talk("How to do mode is is activated")
        while True:
            self.talk("Please tell me what you want to know")
            how = self.take_Command()
            try:
                if ("exit" in how) or("close" in how):
                    self.talk("Ok sir how to mode is closed")
                    break
                else:
                    max_result=1
                    how_to = search_wikihow(how,max_result)
                    assert len(how_to) == 1
                    how_to[0].print()
                    self.talk(how_to[0].summary)
            except Exception as e:
                self.talk("Sorry sir, I am not able to find this")

    def comum(self,command):
        print(command)
        if ('hi'in command) or('hai'in command) or ('hey'in command) or ('hello' in command) :
            self.talk("Hello boss what can I help for u")
        else :
            self.No_result_found()

    def Fun(self,command):
        print(command)
        if 'your name' in command:
            self.talk("My name is jarvis")
        elif 'my name' in command:
            self.talk("your name is Harshit")
        elif 'university name' in command:
            self.talk("you are studing in VIT Bhopal, Btech Computer Science in gaming Technology") 
        elif 'what can you do' in command:
            self.talk("I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes")
        elif 'your age' in command:
            self.talk("I am good.")
        elif 'date' in command:
            self.talk(date.today().strftime("%b-%d-%Y"))
        elif 'are you single' in command:
            self.talk('No, I am in a relationship with wifi.')
        elif 'joke' in command:
            self.talk(pyjokes.get_joke())
        elif 'are you there' in command:
            self.talk('Yes boss I am here')
        elif 'tell me something' in command:
            self.talk('boss, I don\'t have much to say, you only tell me someting I will give you the company')
        elif 'thank you' in command:
            self.talk('boss, I am here to help you..., your welcome')
        elif 'in your free time' in self.command:
            self.talk('boss, I will be listening to all your words')
        elif 'I love you' in command:
            self.talk('I love you too boss')
        elif 'can you hear me' in command:
            self.talk('Yes Boss, I can hear you')
        elif 'do you ever get tired' in command:
            self.talk('It would be impossible for me to get tired')
        else :
            self.No_result_found()

    def social(self,command):
        print(command)
        if 'facebook' in command:
            self.talk('opening your facebook')
            webbrowser.open('https://www.facebook.com/')
        elif 'whatsapp' in command:
            self.talk('opening your whatsapp')
            webbrowser.open('https://web.whatsapp.com/')
        elif 'instagram' in command:
            self.talk('opening your instagram')
            webbrowser.open('https://www.instagram.com/')
        elif 'twitter' in command:
            self.talk('opening your twitter')
            webbrowser.open('https://twitter.com/Suj8_116')
        elif 'discord' in command:
            self.talk('opening your discord')
            webbrowser.open('https://discord.com/channels/@me')
        else :
            self.No_result_found()

    def Clock_time(self,command):
        print(command)
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        self.talk("Current time is "+time)

    def Cal_day(self):
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)

        return day_of_the_week

    def shedule(self):
        day = self.Cal_day().lower()
        self.talk("Boss today's shedule is")
        Week = {"monday" : "6:00 AM - Wake up, shower, and get dressed 7:00 AM - Breakfast 8:00 AM - Commute to work/school 9:00 AM - Work/school 12:00 PM - Lunch break 1:00 PM - Work/school 5:00 PM - Commute back home 6:00 PM - Exercise or other physical activity 7:00 PM - Dinner 8:00 PM - Spend time with family/friends or pursue hobbies 10:00 PM - Wind down and prepare for bed 11:00 PM - Sleep",
        "tuesday" : "6:00 AM - Wake up, shower, and get dressed 7:00 AM - Breakfast 8:00 AM - Work/school 12:00 PM - Lunch break 1:00 PM - Work/school 5:00 PM - Commute back home 6:00 PM - Volunteer work or community service 7:00 PM - Dinner 8:00 PM - Relaxation or pursue hobbies 10:00 PM - Wind down and prepare for bed 11:00 PM - Sleep",
        "wednesday" : "6:00 AM - Wake up, shower, and get dressed 7:00 AM - Breakfast 8:00 AM - Work/school 12:00 PM - Lunch break 1:00 PM - Work/school 5:00 PM - Commute back home 6:00 PM - Attend a class or take an online course 7:00 PM - Dinner 8:00 PM - Spend time with family/friends or pursue hobbies 10:00 PM - Wind down and prepare for bed 11:00 PM - Sleep",
        "thrusday" : "6:00 AM - Wake up, shower, and get dressed 7:00 AM - Breakfast 8:00 AM - Work/school 12:00 PM - Lunch break 1:00 PM - Work/school 5:00 PM - Commute back home 6:00 PM - Socialize with friends/family 8:00 PM - Dinner 9:00 PM - Watch a movie or go to a concert/show 11:00 PM - Wind down and prepare for bed 12:00 AM - Sleep",
        "friday" : "6:00 AM - Wake up, shower, and get dressed 7:00 AM - Breakfast 8:00 AM - Work/school 12:00 PM - Lunch break 1:00 PM - Work/school 5:00 PM - Commute back home 6:00 PM - Socialize with friends/family 8:00 PM - Dinner 9:00 PM - Watch a movie or go to a concert/show 11:00 PM - Wind down and prepare for bed 12:00 AM - Sleep",
        "saturday" : "8:00 AM - Wake up and have a leisurely breakfast 9:00 AM - Exercise or other physical activity 10:00 AM - Pursue hobbies or attend to personal projects 12:00 PM - Lunch 1:00 PM - Socialize with friends/family 6:00 PM - Dinner 7:00 PM - Attend a cultural event or go out with friends 11:00 PM - Wind down and prepare for bed 12:00 AM - Sleep",
        "sunday":"Boss today is holiday but we can't say anything when they will bomb you with any assisgnments."}
        if day in Week.keys():
            self.talk(Week[day])

    def college(self,command):
        print(command)
        if 'teams' in command:
            self.talk('opening your microsoft teams')
            webbrowser.open('https://teams.microsoft.com/')
        elif 'stream' in command:
            self.talk('opening your microsoft stream')
            webbrowser.open('https://web.microsoftstream.com/')
        elif 'outlook' in command:
            self.talk('opening your microsoft school outlook')
            webbrowser.open('https://outlook.office.com/mail/')
        elif 'vtop portal' in command:
            self.talk('opening your vit university management system')
            webbrowser.open('https://vtop.vitbhopal.ac.in/vtop/initialProcess/')
        elif 'octave' in command:
            self.talk('opening Octave online')
            webbrowser.open('https://octave-online.net/')
        else :
            self.No_result_found()

    def OnlineClasses(self,command):
        print(command)

        if("java" in command):
            self.talk('opening DSA class in teams')
            webbrowser.open("https://teams.microsoft.com/java")
        elif 'online classes' in command:
            self.talk('opening your microsoft teams')
            webbrowser.open('https://teams.microsoft.com/')

    def B_S(self,command):
        print(command)
        try:

            if ('wikipedia' in command):
                target1 = command.replace('search for','')
                target1 = target1.replace('in wikipedia','')
            elif('what is meant by' in command):
                target1 = command.replace("what is meant by"," ")
            elif('tell me about' in command):
                target1 = command.replace("tell me about"," ")
            elif('who the heck is' in command):
                target1 = command.replace("who the heck is"," ")
            print("searching....")
            info = wikipedia.summary(target1,5)
            print(info)
            self.talk("according to wikipedia "+info)
        except :
            self.No_result_found()

    def brows(self,command):
        print(command)
        if 'google' in command:
            self.talk("Boss, what should I search on google..")
            S = self.take_Command()
            webbrowser.open(f"{S}")
        elif 'edge' in command:
            self.talk('opening your Miscrosoft edge')
            os.startfile('..\\..\\MicrosoftEdge.exe')
        else :
            self.No_result_found()

    def Google_Apps(self,command):
        print(command)
        if 'gmail' in command:
            self.talk('opening your google gmail')
            webbrowser.open('https://mail.google.com/mail/')
        elif 'maps' in command:
            self.talk('opening google maps')
            webbrowser.open('https://www.google.co.in/maps/')
        elif 'news' in command:
            self.talk('opening google news')
            webbrowser.open('https://news.google.com/')
        elif 'calender' in command:
            self.talk('opening google calender')
            webbrowser.open('https://calendar.google.com/calendar/')
        elif 'photos' in command:
            self.talk('opening your google photos')
            webbrowser.open('https://photos.google.com/')
        elif 'documents' in command:
            self.talk('opening your google documents')
            webbrowser.open('https://docs.google.com/document/')
        elif 'spreadsheet' in command:
            self.talk('opening your google spreadsheet')
            webbrowser.open('https://docs.google.com/spreadsheets/')
        else :
            self.No_result_found()

    def yt(self,command):
        print(command)
        if 'play' in command:
            self.talk("Boss can you please say the name of the song")
            song = self.take_Command()
            if "play" in song:
                song = song.replace("play","")
            self.talk('playing '+song)
            print(f'playing {song}')
            pywhatkit.playonyt(song)
            print('playing')
        elif "download" in command:
            self.talk("Boss please enter the youtube video link which you want to download")
            link = input("Enter the YOUTUBE video link: ")
            yt=YouTube(link)
            yt.streams.get_highest_resolution().download()
            self.talk(f"Boss downloaded {yt.title} from the link you given into the main folder")
        elif 'youtube' in command:
            self.talk('opening your youtube')
            webbrowser.open('https://www.youtube.com/')
        else :
            self.No_result_found()

    def open_source(self,command):
        print(command)
        if 'github' in command:
            self.talk('opening your github')
            webbrowser.open('https://github.com/Harshit-Raj-14/JARVIS-Python-Voice-Assistant')
        elif 'gitlab' in command:
            self.talk('opening your gitlab')
            webbrowser.open('https://gitlab.com/-/profile')
        else :
            self.No_result_found()

    def edit(self,command):
        print(command)
        if 'slides' in command:
            self.talk('opening your google slides')
            webbrowser.open('https://docs.google.com/presentation/')
        elif 'canva' in command:
            self.talk('opening your canva')
            webbrowser.open('https://www.canva.com/')
        else :
            self.No_result_found()

    def OTT(self,command):
        print(command)
        if 'hotstar' in command:
            self.talk('opening your disney plus hotstar')
            webbrowser.open('https://www.hotstar.com/in')
        elif 'prime' in command:
            self.talk('opening your amazon prime videos')
            webbrowser.open('https://www.primevideo.com/')
        elif 'netflix' in command:
            self.talk('opening Netflix videos')
            webbrowser.open('https://www.netflix.com/')
        else :
            self.No_result_found()

    def OpenApp(self,command):
        print(command)
        if ('calculator'in command) :
            self.talk('Opening calculator')
            os.startfile('C:\\Windows\\System32\\calc.exe')
        elif ('paint'in command) :
            self.talk('Opening msPaint')
            os.startfile('c:\\Windows\\System32\\mspaint.exe')
        elif ('notepad'in command) :
            self.talk('Opening notepad')
            os.startfile('c:\\Windows\\System32\\notepad.exe')
        elif ('discord'in command) :
            self.talk('Opening discord')
            os.startfile('..\\..\\Discord.exe')
        elif ('editor'in command) :
            self.talk('Opening your Visual studio code')
            os.startfile('..\\..\\Code.exe')
        elif ('online classes'in command) :
            self.talk('Opening your Microsoft teams')
            webbrowser.open('https://teams.microsoft.com/')
        elif ('spotify'in command) :
            self.talk('Opening spotify')
            os.startfile('..\\..\\Spotify.exe')
        elif ('lt spice'in command) :
            self.talk('Opening lt spice')
            os.startfile("..\\..\\XVIIx64.exe")
        elif ('steam'in command) :
            self.talk('Opening steam')
            os.startfile("..\\..\\steam.exe")
        elif ('media player'in command) :
            self.talk('Opening VLC media player')
            os.startfile("C:\Program Files\VideoLAN\VLC\vlc.exe")
        else :
            self.No_result_found()

    def CloseApp(self,command):
        print(command)
        if ('calculator'in command) :
            self.talk("okay boss, closeing calculator")
            os.system("taskkill /f /im calc.exe")
        elif ('paint'in command) :
            self.talk("okay boss, closing mspaint")
            os.system("taskkill /f /im mspaint.exe")
        elif ('notepad'in command) :
            self.talk("okay boss, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif ('discord'in command) :
            self.talk("okay boss, closing discord")
            os.system("taskkill /f /im Discord.exe")
        elif ('editor'in command) :
            self.talk("okay boss, closing vs code")
            os.system("taskkill /f /im Code.exe")
        elif ('spotify'in command) :
            self.talk("okay boss, closing spotify")
            os.system("taskkill /f /im Spotify.exe")
        elif ('lt spice'in command) :
            self.talk("okay boss, closing lt spice")
            os.system("taskkill /f /im XVIIx64.exe")
        elif ('steam'in command) :
            self.talk("okay boss, closing steam")
            os.system("taskkill /f /im steam.exe")
        elif ('media player'in command) :
            self.talk("okay boss, closing media player")
            os.system("taskkill /f /im vlc.exe")
        else :
            self.No_result_found()

    def shopping(self,command):
        print(command)
        if 'flipkart' in command:
            self.talk('Opening flipkart online shopping website')
            webbrowser.open("https://www.flipkart.com/")
        elif 'amazon' in command:
            self.talk('Opening amazon online shopping website')
            webbrowser.open("https://www.amazon.in/")
        else :
            self.No_result_found()

    def pdf_reader(self):
        self.talk("Boss enter the name of the book which you want to read")
        n = input("Enter the book name: ")
        n = n.strip()+".pdf"
        book_n = open(n,'rb')
        pdfReader = PyPDF2.PdfFileReader(book_n)
        pages = pdfReader.numPages
        self.talk(f"Boss there are total of {pages} in this book")
        self.talk("please enter the page number which I nedd to read for you")
        num = int(input("Enter the page number: "))
        page = pdfReader.getPage(num)
        text = page.extractText()
        print(text)
        self.talk(text)

    def silenceTime(self,command):
        print(command)
        x=0

        if ('10' in command) or ('ten' in command):x=600
        elif '1' in command or ('one' in command):x=60
        elif '2' in command or ('two' in command):x=120
        elif '3' in command or ('three' in command):x=180
        elif '4' in command or ('four' in command):x=240
        elif '5' in command or ('five' in command):x=300
        elif '6' in command or ('six' in command):x=360
        elif '7' in command or ('seven' in command):x=420
        elif '8' in command or ('eight' in command):x=480
        elif '9' in command or ('nine' in command):x=540
        self.silence(x)

    def silence(self,k):
        t = k
        s = "Ok boss I will be silent for "+str(t/60)+" minutes"
        self.talk(s)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        self.talk("Boss "+str(k/60)+" minutes over")

    def verifyMail(self):
        try:
            self.talk("what should I say?")
            content = self.take_Command()
            self.talk("To whom do you want to send the email?")
            to = self.take_Command()
            self.SendEmail(to,content)
            self.talk("Email has been sent to "+str(to))
        except Exception as e:
            print(e)
            self.talk("Sorry sir I am not not able to send this email")

    def SendEmail(self,to,content):
        print(content)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login("YOUR_MAIL_ID","PASWORD")
        server.sendmail("YOUR_MAIL_ID",to,content)
        server.close()

    def locaiton(self):
        self.talk("Wait boss, let me check")
        try:
            IP_Address = get('https://api.ipify.org').text
            print(IP_Address)
            url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
            print(url)
            geo_reqeust = get(url)
            geo_data = geo_reqeust.json()
            city = geo_data['city']
            state = geo_data['region']
            country = geo_data['country']
            tZ = geo_data['timezone']
            longitude = geo_data['longitude']
            latidute = geo_data['latitude']
            org = geo_data['organization_name']
            print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
            self.talk(f"Boss we are in {city} city of {state} state of {country} country")
            self.talk(f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
        except Exception as e:
            self.talk("Sorry boss, due to network issue I am not able to find where we are.")
            pass

    def Instagram_Pro(self):
        self.talk("Boss please enter the user name of Instagram: ")
        name = input("Enter username here: ")
        webbrowser.open(f"www.instagram.com/{name}")
        time.sleep(5)
        self.talk("Boss would you like to download the profile picture of this account.")
        cond = self.take_Command()
        if('download' in cond):
            mod = instaloader.Instaloader()
            mod.download_profile(name,profile_pic_only=True)
            self.talk("I am done boss, profile picture is saved in your main folder. ")
        else:
            pass

    def scshot(self):
        self.talk("Boss, please tell me the name for this screenshot file")
        name = self.take_Command()
        self.talk("Please boss hold the screen for few seconds, I am taking screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        self.talk("I am done boss, the screenshot is saved in the main folder.")

    def news(self):
        MAIN_URL_= "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=7ca0f6d986024269b3392a430cc19314"
        MAIN_PAGE_ = get(MAIN_URL_).json()
        articles = MAIN_PAGE_["articles"]
        headings=[]
        seq = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth'] 
        for ar in articles:
            headings.append(ar['title'])
        for i in range(len(seq)):
            print(f"todays {seq[i]} news is: {headings[i]}")
            self.talk(f"todays {seq[i]} news is: {headings[i]}")
        self.talk("Boss I am done, I have read most of the latest news")

    def condition(self):
        usage = str(psutil.cpu_percent())
        self.talk("CPU is at"+usage+" percentage")
        battray = psutil.sensors_battery()
        percentage = battray.percent
        self.talk(f"Boss our system have {percentage} percentage Battery")
        if percentage >=75:
            self.talk(f"Boss we could have enough charging to continue our work")
        elif percentage >=40 and percentage <=75:
            self.talk(f"Boss we should connect out system to charging point to charge our battery")
        elif percentage >=15 and percentage <=30:
            self.talk(f"Boss we don't have enough power to work, please connect to charging")
        else:
            self.talk(f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon")

    def No_result_found(self):
        self.talk('Boss I couldn\'t understand, could you please say it again.')        

startExecution = MainThread()
class Main(QMainWindow):
    cpath =""   


######################    GUI    ########################################

    def __init__(self,path):
        self.cpath = path
        super().__init__()
        self.ui = Ui_JarvisUi()#(path=current_path)
        self.ui.setupUi(self)
        self.ui.pushButton_start.clicked.connect(self.startTask)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.ui.pushButton_chrome.clicked.connect(self.chrome_app)
        self.ui.pushButton_whatsapp.clicked.connect(self.whatsapp_app)
        self.ui.pushButton_youtube.clicked.connect(self.youtube_app)
    
    def chrome_app(self):
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    
    def youtube_app(self):
        webbrowser.open("https://www.youtube.com/")
    
    def whatsapp_app(self):
        webbrowser.open("https://web.whatsapp.com/")


    def startTask(self):

        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\bg\ironmanwoo.gif")
        self.ui.gif_1.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\extraGui\Hero_Template.gif")
        self.ui.gif_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\extraGui\Earth.gif")
        self.ui.gif_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\voiceReg\aqua.gif")
        self.ui.gif_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\bg\voicegrf.gif")
        self.ui.gif_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        IP_Address = get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        search = f"temperature in {city}"
        url_1 = f"https://www.google.com/search?q={search}"
        r = get(url_1)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        self.ui.Text_Temperature.setText(temp)
        self.ui.Text_Day.setText(date.today().strftime("%A"))
        

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()


    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.Text_Date.setText(label_date)
        self.ui.Text_Time.setText(label_time)
            

current_path = os.getcwd()
app = QApplication(sys.argv)

jarvis = Main(path=current_path)
jarvis.show()
exit(app.exec_())
        
