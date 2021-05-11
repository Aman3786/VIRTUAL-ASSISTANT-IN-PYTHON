# from __future__ import unicode_literals
import pyttsx3                      # pyttsx3 is a text-to-speech conversion library in Python.It works offline.
import datetime                     # The datetime module supplies classes for manipulating dates and times.
import speech_recognition as sr     # It is a Library for performing speech recognition, with support for several engines and APIs.
import wikipedia
import webbrowser
import os
import subprocess
import random
import requests
import gsearch
import pytesseract
from PIL import Image
from googletrans import Translator
import img2pdf
import youtube_dl
import smtplib
from email.message import EmailMessage
import imghdr
import config     #user defined module to get the email_address and password of sender

# There are 3 text-to-specch(TTs) engine viz. sapi5,nsss and espeak

engine = pyttsx3.init('sapi5')         # object creation. Wrapping the sapi5 TTs with pyttsx3
voice =engine.getProperty('voices')    #getting details of current voice
print(voice)
engine.setProperty('voice',voice[0].id)  #There is two voice in system i.e. male(0) and female(1). Changing index, changes voices. 0 for male.

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    time = int(datetime.datetime.now().hour)

    if time>=0 and time<4:
        print("hello sir")
        print("sir,Still you are awake...\nHave some rest sir.")
        speak("hello sir")
        speak("sir,Still you are awake Have some rest sir.")
    elif time>=4 and time<12:
        print("Good Morning Sir.")
        speak("Good Morning Sir.")   
    elif time>=12 and time<17:
        print("Good Afternoon Sir")
        speak("Good Afternoon Sir")
    else:
        print("Good Evening Sir")
        speak("Good Evening Sir")
  
    speak("Hello sir, I am your assistant")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir : {query}\n")
    except Exception as e: 
        print("Say that again please...")
        speak("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()

    i=1
    while True:
        query = takeCommand().lower()
      

        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                print("can't understand,please say it again")
                speak("can't understand,please say it again")

        elif "open google" in query:
            try:
                webbrowser.get(using='google-chrome').open("google.com",new=2)
            except:
                print("can't understand,please say it again")
                speak("can't understand,please say it again")

        elif "open youtube" in query:
            try:
                webbrowser.get(using='google-chrome').open("youtube.com",new=2)
            except:
                print("sorry,I am not able to understand. please say it again")
                speak("sorry,I am not able to understand. please say it again")

        elif "time" in query:
            try:
                # time = datetime.datetime.now().strftime('%H:%M:%S')
                # print(time)
                # speak(time)
                subprocess.call("Rundll32.exe shell32.dll,Control_RunDLL timedate.cpl")
            except:
                print("sorry,I am not able to understand. please say it again")
                speak("sorry,I am not able to understand. please say it again")
                

        elif 'code' in query:
            try:
                path = 'C:\\Users\\Amaan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                os.startfile(path)
            except:
                print("sorry,can't open code. please say it again")
                speak("sorry,can't open code. please say it again")

        elif "notepad" in query or "notepads" in query:
            try:
                path = "C:\\Windows\\notepad.exe"
                os.startfile(path)
            except:
                print("sorry,can't open notepad. please say it again")
                speak("sorry,can't open notepad. please say it again")

        elif "sublime" in query or "sublimes" in query:
            try:
                path = "C:\\Program Files (x86)\\Sublime Text 3\\subl.exe"
                os.startfile(path)
            except:
                print("sorry,can't open sublime. please say it again")
                speak("sorry,can't open sublime. please say it again")

        elif "hello" in query or "hii" in query or "hey" in query or "hi" in query:
            try:
                if 'hello' in query:
                    print("Hello")
                    speak("Hello")
                elif "hii" in query:
                    print("hii")
                    speak("hii")
                elif "hi" in query:
                    print("hi")
                    speak("hi")
                else:
                    print("Hey")
                    speak("Hey")
            except:
                print("sorry,please say it again")
                speak("sorry,please say it again")

        elif "clear" in query:
            try:
                os.system("cls")
            except:
                print("sorry,please say it again")
                speak("sorry,please say it again")


        elif "terminate" in query or 'good bye' in query or 'goodbye' in query or 'exit' in query:
            speak('Good bye sir, see you soon')
            print("Good bye sir, see you soon")
            exit()

        elif "how are you" in query or "whatsupp" in query or "whatsup" in query:
            print("I'm good")
            speak("I'm good")


        elif "saver" in query:
            try:
                os.chdir("C:\\Users\\Amaan\\Desktop\\screenshot")
                os.system(f"nircmd.exe savescreenshotfull {i}.png")
                speak("Screenshot taken")
                os.chdir("C:\\Users\\Amaan\\Desktop\\Amaan\\Amaan_all\\Amaan")
                i+=1
            except:
                print("can't save your screen shot.please say it again")
                speak("can't save your screen shot.please say it again")

        elif 'next song' in query or 'next songs' in query or "play songs" in query or "play song" in query or "songs" in query or "song" in query:
            try:
                a=str(random.choice(os.listdir("C:\\Users\\Amaan\\Desktop\\screenshot")))
                path = "C:\\Users\\Amaan\\Desktop\\screenshot"+'\\'+a
                os.system(path)
            except:
                print("sorry,not able to play the song.please say it again")
                speak("sorry,not able to play the song.please say it again")
                
        elif 'stop music'in query:
            try:
                os.system('nircmd.exe killprocess Groove.exe')
            except:
                print("please say it again..")
                speak("please say it again..")

        elif 'minimise all' in query:
            try:
                os.system('nircmd sendkeypress rwin+"d"')  
            except:
                print("please say it again..")
                speak("please say it again..")

        elif 'maximise all' in query:
            try:
                os.system('nircmd sendkeypress rwin+shift+"m"')  
            except:
                print("please say it again..")
                speak("please say it again..")

        elif "lock" in query:
            try:
                subprocess.call('rundll32.exe user32.dll,LockWorkStation')
            except:
                print("please say it again..")
                speak("please say it again..")

        elif "manager" in query:
            try:
                subprocess.call("Rundll32.exe devmgr.dll DeviceManager_Execute")
            except:
                print("please say it again..")
                speak("please say it again..")

        elif "variables" in query or "environment" in query or "variable" in query or "environments":
            try:
                subprocess.call("Rundll32.exe sysdm.cpl,EditEnvironmentVariables")
            except:
                print("please say it again..")
                speak("please say it again..")

        elif "display" in query:
            try:
                subprocess.call("Rundll32.exe shell32.dll,Control_RunDLL desk.cpl")
            except:
                print("please say it again..")
                speak("please say it again..")

        elif "explorer" in query or "manager" in query:
            try:
                subprocess.call("Rundll32.exe shell32.dll,Options_RunDLL 0")
            except:
                print("please say it again..")
                speak("please say it again..")

        elif "control panel" in query or "panel" in query:
            try:
                subprocess.call("Rundll32.exe shell32.dll,Control_RunDLL")
            except:
                print("please say it again..")
                speak("please say it again..")

        elif "clock" in query or "display clock" in query:
            try:
                subprocess.call("Rundll32.exe shell32.dll,Control_RunDLL timedate.cpl,,1")
            except:
                print("please say it again..")
                speak("please say it again..")

        elif "about windows" in query or "about window" in query:
            try:
                subprocess.call("Rundll32.exe shell32.dll,ShellAbout")
            except:
                print("please say it again..")
                speak("please say it again..")

        elif "sleep" in query:
            try:
                subprocess.call("Rundll32.exe powrprof.dll,SetSuspendState")
            except:
                print("please say it again..")
                speak("please say it again..")

        elif "background" in query or "backgrounds" in query:
            try:
                subprocess.call("Rundll32.exe shell32.dll,Control_RunDLL desk.cpl,,2")
            except:
                print("please say it again..")
                speak("please say it again..")

        elif "settings" in query or "setting" in query:
            try:
                subprocess.call("Rundll32.exe shell32.dll,Options_RunDLL 3")
            except:
                print("please say it again..")
                speak("please say it again..")

        elif 'cmd' in query or "prompt" in query:
            try:
                os.system('start "" "C:\\WINDOWS\\system32\\cmd.exe"')
            except:
                print("please say it again..")
                speak("please say it again..")

        elif "new folder" in query:
            try:
                speak("Name of a folder")
                folder = str(takeCommand())
                if "none" in query:
                    print("Nothing is recognize")
                    speak("Nothing is recognize")
                else:
                    os.mkdir(f"C:\\Users\\Amaan\\Desktop\\{folder}") 
                    print("Folder created")          
                    speak("Folder created")
            except:
                print("sorry,can't able to create folder.say it again")
                speak("sorry,can't able to create folder.say it again")

        elif "new file" in query or "create file" in query or "file" in query:
            try:
                os.chdir("C:\\Users\\Amaan\\Desktop\\Amaan")
                speak("Name of the file")
                file =str(takeCommand())
                print(file)
                if ".py" in file:
                    with open(file,"w") as f:
                        pass
                    print("file created..\n")
                    speak("file created..")
                    os.chdir("C:\\Users\\Amaan\\Desktop\\Amaan\\Amaan_all\\Amaan")
                elif ".java" in file:
                    with open(file,"w") as f:
                        pass
                    print("file created..\n")
                    speak("file created..")
                    os.chdir("C:\\Users\\Amaan\\Desktop\\Amaan\\Amaan_all\\Amaan")
                elif ".c" in file:
                    with open(file,"w") as f:
                        pass
                    print("file created..\n")
                    speak("file created..")
                    os.chdir("C:\\Users\\Amaan\\Desktop\\Amaan\\Amaan_all\\Amaan")
                elif ".txt" in file:
                    with open(file,"w") as f:
                        pass
                    print("file created..\n")
                    speak("file created..")
                    os.chdir("C:\\Users\\Amaan\\Desktop\\Amaan\\Amaan_all\\Amaan")
                else:
                    pass
            except:
                print("sorry,can't able to create file.say it again")
                speak("sorry,can't able to create file.say it again")


        elif "calculate" in query or "solve" in query:
            try:
                query = query.replace('calculate','')
                query = query.replace('solve','')
                query = query.replace('plus','+')
                query = query.replace('minus','-')
                query = query.replace('multiplies','*')
                query = query.replace('multiplication','*')
                query = query.replace('multiply','*')            
                query = query.replace('multiplied','*')
                query = query.replace('divide','/')
                query = query.replace('divides','/')
                query = query.replace('divided','/')
                query = query.replace('division','/')
                query = query.replace('modulo','%')
                query = query.replace('modulus','%')

                result = eval(query)
                print(f"The answer is {result}")
                speak(f"The answer is {result}")
            except:
                print("can't understand,please say it again")
                speak("can't understand,please say it again")
        
        elif "android" in query or "studio" in query:
            try:
                path = 'C:\\Program Files\\Android\\Android Studio\\bin\\studio.exe'
                os.startfile(path)
            except:
                print("sorry,can't open studio. please say it again")
                speak("sorry,can't open studio. please say it again")

        elif "download" in query or "downloaded" in query or "download youtube" in query:
            try:  
                ydl_opts = {} 
                
                def vid(): 
                    link = input("Enter the video link: ")
                    speak("Enter the video link") 
                    z = link.strip() 
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
                        ydl.download([z])
                        
                    channel = 1
                    while channel == int(1):
                        vid()
                        channel = int(input("Enter '1' if you want to download more videos or '0' if you are done ")) 
                        speak("Enter '1' if you want to download more videos or '0' if you are done")
            except:
                print("sorry,can't download video. please say it again")
                speak("sorry,can't download video. please say it again")

        elif "chrome" in query:
            try:
                path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(path)
            except:
                print("sorry,can't open it.please say it again")
                speak("sorry,can't open it.please say it again")

        elif "temperature" in query or "temperature of" in query or "weather" in query or "weather of" in query or "climate" in query or "climate of" in query:    
            try:
                query = query.replace('temperture','')
                query = query.replace('temperture of','')
                query = query.replace('weather','')
                query = query.replace('weather of','')
                query = query.replace('climate','')
                query = query.replace('climate of','')

                url = f'http://api.openweathermap.org/data/2.5/weather?q={query}&appid=a3c4b1ad728ab081c6984b4de0e722e3&units=metric'
                r = requests.get(url)
                data = r.json()
                
                temp = data['main']['temp']
                wind_speed = data['wind']['speed']
                pressure_temp = data['main']['pressure']
                humidity_temp = data['main']['humidity']
                longitude = data['coord']['lon']
                latitude = data['coord']['lat']
                desc = data['weather'][0]['description']

                print(f"Temperature : {temp} degree celcius")
                print(f"wind speed : {wind_speed} m\s")
                print(f"pressure : {pressure_temp}")
                print(f"humidity : {humidity_temp}")
                print(f"description : {desc}")
                print(f"longitude : {longitude}")
                print(f"latitude : {latitude}")        
                speak(f"Temperature : {temp} degree celcius")
                speak(f"wind speed : {wind_speed} m\s")
                speak(f"pressure : {pressure_temp}")
                speak(f"humidity : {humidity_temp}")
                speak(f"description : {desc}")
                speak(f"longitude : {longitude}")
                speak(f"latitude : {latitude}")
            except:
                query = query.replace('temperture','')
                query = query.replace('temperture of','')
                query = query.replace('weather','')
                query = query.replace('weather of','')
                query = query.replace('climate','')
                query = query.replace('climate of','')
                print(f"sorry,can't show you the weather of {query},please say it again")
                speak(f"sorry,can't show you the weather of {query},please say it again")

        elif "shutdown" in query or "power off" in query:
            try:
                print("Good bye, see you soon")
                speak("Good bye, see you soon")
                os.system('shutdown -l -t 00')
            except:
                print("sorry,please say it again")
                speak("sorry,please say it again")

        elif "volume" in query or "noise" in query or "sound" in query:
            try:
                if "max" in query or "full" in query or "high" in query:
                    os.system("nircmd.exe setsysvolume 65535")
                elif "increase" in query or "up" in query:
                    os.system("nircmd.exe changesysvolume 5000")
                elif "decrease" in query or "down" in query:
                    os.system("nircmd.exe changesysvolume -5000")
                elif "mute" in query or "silent" in query:
                    os.system("nircmd.exe mutesysvolume 1")
                elif "unmute" in query:
                    os.system("nircmd.exe mutesysvolume 0")
            except:
                print("sorry,can't understand. please say it again")
                speak("sorry,can't understand. please say it again")

        elif "search" in query or "images of" in query or "image of" in query or "google" in query:
            try:
                if "images" in query or "image" in query:
                    query = query.replace("images of","")
                    query = query.replace("image of","")
                    url = f"https://www.google.com/search?tbm=isch&q={query}"
                    webbrowser.get(using='google-chrome').open(url,new=2)
                elif "map" in query:
                    query = query.replace("google map","")
                    query = query.replace("google map of","")
                    query = query.replace("map","")
                    query = query.replace("map of","")
                    url = f"https://www.google.co.in/maps/place/{query}"
                    webbrowser.get(using='google-chrome').open(url,new=2)
                else:
                    query = query.replace("search","")
                    query = query.replace("google","")
                    gsearch(query)
            except:
                print("sorry,not able to understand.please say it again")
                speak("sorry,not able to understand.please say it again")

        elif "image to text" in query or "images to texts" in query or "image to txt" in query or "images to txt" in query:
            try:
                path= input("Please enter the path of the image: ")
                speak("Please enter the path of the image: ")
                img = Image.open(path) 
                pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
                result = pytesseract.image_to_string(img)
                print(result)
                speak(result)
                user = input("Want to write the content inside the file (Press 'Y' for Yes and 'N' for No) : ")
                speak("Want to write the content inside the file. Press 'Y' for Yes and 'N' for No")
                if user == "Y" or user == "y":
                    print("Name of the file")
                    speak("Name of the file")
                    file_name = str(takeCommand())
                    file = open(f"C:\\Users\\Amaan\\Documents\\{file_name}","w")
                    file.write(result)
                    print("successfully written.")
                    speak("successfully written.")
                elif user == "N" or user == "n":
                    print("Ok")
                    speak("Ok")
                    break
                else:
                    print("invalid choice!!")
                    speak("invalid choice!!")
            
        # j = 1
        elif "image to pdf" in query or "images to pdfs" in query or "image to pdfs" in query or "image to pdf" in query:
            j =1
            try:
                a = input("Want to convert single image or multiple image.(Press 'A' for single image OR 'B' for multiple image) : ")
                speak("Want to convert single image or multiple image. Press 'A' for single image OR 'B' for multiple image")
                if a == "A":
                    user = input("Enter the path of the image: ")
                    speak("Enter the path of the image")
                    img = Image.open(user)
                    pdf_bytes = img2pdf.convert(img.filename)
                    pdf = open(f"C:\\Users\\Amaan\\Documents\\{j}.pdf","wb")
                    pdf.write(pdf_bytes)
                    img.close()
                    pdf.close()
                    j+=1
                    print("successfully created pdf file")
                    speak("successfully created pdf file")
                elif a == "B":
                    li = []
                    n = int(input("Enter the total number of image you want to convert: "))
                    speak("Enter the total number of image you want to convert:")
                    for i in range(1,n+1):
                        k =1
                        li.append(input(f"Enter {k} path: "))
                        k+=1
                    for i in li:
                        img = Image.open(i)
                        pdf_bytes = img2pdf.convert(img.filename)
                        pdf = open(f"C:\\Users\\Amaan\\Documents\\{j}.pdf","wb")
                        pdf.write(pdf_bytes)
                        img.close()
                        pdf.close()
                        j+=1
                    print("successfully created pdf file")
                    speak("successfully created pdf file")
                else:
                    print("INVALID CHOICE!!")
                    speak("INVALID CHOICE!!")
            except:
                print("sorry,not able to convert it into pdf.please say it again")
                speak("sorry,not able to convert it into pdf.please say it again")
                
        elif "translate" in query:
            try:
                user= input("Want to paste text for translation OR Want to speak.(Press 'A' for to paste text and 'B' for to speak): ")
                print("Want to paste text for translation OR Want to speak.Press 'A' for to paste text and 'B' for to speak")
                if user == "A":
                    txt = input("Enter the text to translate: ")
                    lang = input("Enter the language in which you want to translate: ")
                    p = Translator()
                    res = p.translate(txt,dest=lang)
                    print(res)
                    speak(res)
                elif user == "B":
                    print("Speak the text")
                    speak("Speak the text")
                    txt = str(takeCommand())
                    print("Tell the language in which you want to convert")
                    speak("Tell the language in which you want to convert")
                    lang = str(takeCommand())
                    p = Translator()
                    res = p.translate(txt,dest=lang)
                    print(res)
                    speak(res)
                else:
                    print("INVALID CHOICE!!")
                    speak("INVALID CHOICE!!")
            except:
                print("sorry,not able to translate it.please say it again")
                speak("sorry,not able to translate it.please say it again")

        elif "mp3 extract" in query or "youtube mp3 extract" in query or "extract" in query:
            try:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'extractaudio':True,
                    'audioformat':'wav',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'wav',
                        'preferredquality': '192'
                    }],
                    'postprocessor_args': [
                        '-ar', '16000'
                    ],
                    'prefer_ffmpeg': True,
                    'keepvideo': False
                    }

                link =input("Enter the link: ")

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
            except:
                print("sorry,not able to extract mp3.Please say it again.")
                speak("sorry,not able to extract mp3.Please say it again.")
        
        elif "mail" in query or "gmail" in query:
            try:
                li = []
                print("Want to send plain text or attachment with email.(speak 'A' for plain text or 'B' for Attachment)")
                speak("Want to send plain text or attachment with email.speak 'A' for plain text or 'B' for Attachment")
                user = str(takeCommand())
                if user == 'A' or user == 'a':
                    print("Want to write text or want to speak the text.(speak 'T' to write or 'S' to speak)")
                    speak("Want to write text or want to speak the text.(speak 'T' to write or 'S' to speak)")
                    text = str(takeCommand())
                    if text == "S" or text == "s":
                        try:
                            print("Speak the no. of receiver email address")
                            speak("Speak the number of receiver email address")
                            a = int(takeCommand())
                            for i in range(1,a+1):
                                print(f"speak the {i} Email address of the receiver")
                                speak(f"speak the {i} Email address of the receiver")
                                li.append(input())
                            print("Speak the subject to send")
                            speak("Speak the subject to send")
                            sub = str(takeCommand())
                            print("Speak the mssg to send")
                            speak("Speak the message to send")
                            msg = str(takeCommand())

                            mssg = EmailMessage()
                            mssg['Subject'] = sub
                            mssg['From'] = config.Email
                            mssg['To'] = ','.join(li)
                            mssg.set_content(msg)   

                            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                smtp.login(config.Email,config.Password)
                                smtp.send_message(mssg)

                            print("Email sent successfully..")
                            print("Email sent successfully..") 
                        except:
                            print("sorry,Not able to send email")
                            speak("sorry,Not able to send email")

                    elif text == "T" or text == "t":
                        try:
                            rec = int(input("Enter the no. of receiver: "))
                            speak('Enter the number of receiver')
                            for i in range(1,rec+1):
                                print(f"Enter {i} email address of the receiver")
                                speak(f"Enter {i} email address of the receiver")
                                li.append(input())
                            sub = input("Enter the subject: ")
                            speak("Enter the subject")
                            msg = input("Enter the mssg: ")
                            speak("Enter the message")
                            
                            mssg = EmailMessage()
                            mssg['Subject'] = sub
                            mssg['From'] = config.Email
                            mssg['To'] = ','.join(li)
                            mssg.set_content(msg)   

                            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                smtp.login(config.Email,config.Password)
                                smtp.send_message(mssg) 

                            print("Email sent successfully..")
                            print("Email sent successfully..")
                        except:
                            print("sorry,Not able to send email")
                            speak("sorry,Not able to send email")

                    else:
                        print("Invalid choice!!")
                        speak("Invalid choice!!")
                elif user == "B" or user == 'b':
                    print('Want to send image or document.(speak "I" for image or "D" for document)')
                    speak('Want to send image or document.speak "I" for image or "D" for document')
                    user1 = str(takeCommand())

                    if user1 == "I" or user1 == "i":
                        try:
                            img = []
                            rece = int(input("Enter the no of receiver email address: "))
                            speak("Enter the number of receiver email address")
                            for i in range(1,rece+1):
                                print(f"Enter {i} email address of the receiver")
                                speak(f"Enter {i} email address of the receiver")
                                li.append(input())
                            sub = input("Enter the subject: ")
                            speak("Enter the subject")
                            msg = input("Enter the mssg: ")
                            speak("Enter the message")

                            image = int(input("Enter the no. of image to be send: "))
                            speak("Enter the no. of image to be send")
                            for j in range(1,image+1):
                                print(f"Enter {i} image")
                                speak(f"Enter {i} image")
                                img.append(input())

                            mssg = EmailMessage()
                            mssg['Subject'] = sub
                            mssg['From'] = config.Email
                            mssg['To'] = ','.join(li)
                            mssg.set_content(msg)     
                            
                            for file in img:
                                with open(f'C:\\Users\\Amaan\\Pictures\\Saved Pictures\\{file}','rb') as f:
                                    f_data = f.read()
                                    f_type =  imghdr.what(f.name)
                                    f_name = f.name

                                mssg.add_attachement(f_data,maintype="image",subtype=f_type,filename=f_name)      

                            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                smtp.login(config.Email,config.Password)
                                smtp.send_message(mssg) 

                            print("Email sent successfully..")
                            print("Email sent successfully..")
                        except:
                            print("sorry,Not able to send email")
                            speak("sorry,Not able to send email")

                    elif user1 == "D" or user1 == "d":
                        try:
                            doc = []
                            re = int(input("Enter the no of receiver email address: "))
                            speak("Enter the number of receiver email address")
                            for i in range(1,re+1):
                                print(f"Enter {i} email address of the receiver")
                                speak(f"Enter {i} email address of the receiver")
                                li.append(input())
                            sub = input("Enter the subject: ")
                            speak("Enter the subject")
                            msg = input("Enter the mssg: ")
                            speak("Enter the message")

                            docum = int(input("Enter the no. of file to be send: "))
                            speak("Enter the number of file to be send")
                            for j in range(1,docum+1):
                                print(f"Enter {i} file")
                                speak(f"Enter {i} file")
                                doc.append(input())

                            mssg = EmailMessage()
                            mssg['Subject'] = sub
                            mssg['From'] = config.Email
                            mssg['To'] = ','.join(li)
                            mssg.set_content(msg)

                            for d in doc:
                                with open(f"C:\\Users\\Amaan\\Documents\\{d}","rb") as f:
                                    fdata = f.read()
                                    fname = f.name

                                mssg.add_attachement(fdata,maintype="application",subtype='octet-stream',filename=fname)

                            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                                smtp.login(config.Email,config.Password)
                                smtp.send_message(mssg)

                            print("Email sent successfully..")
                            print("Email sent successfully..")
                        except:
                            print("sorry,Not able to send email")
                            speak("sorry,Not able to send email")
                else:
                    print("INVALID CHOICE !!")
                    print("INVALID CHOICE !!")
            except:
                print("sorry,Not able to understand.Please try again")
                print("sorry,Not able to understand.Please try again")
