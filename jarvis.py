# from twilio.rest import TwilioRestClient
import pyttsx3                   # Package to convert text to speech
import speech_recognition as sr  # Google api for speech recognition or voice recognition
import datetime                  # Package in python to perform operations accroding to the time 
import wikipedia                 # Package in python to access wikipedia page directly
import webbrowser                # To access web operations
import os                        # Functions to operate with the operating system functions
import bs4
from GoogleNews import GoogleNews
from PyDictionary import PyDictionary
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import smtplib                   # It helps in dealing with emails
from selenium import webdriver   # Another to operate webbrowser operations
from pycricbuzz import Cricbuzz

engine = pyttsx3.init('sapi5')
# We can get any property using get for manipulation of voices
dictionary = PyDictionary()
voices = engine.getProperty('voices')    
# There are generally two voices in windows Mike and Zara.We can access Mike by accessing at 0th index and Zara at 1st index
engine.setProperty('voice', voices[0].id)
# driver = webdriver.Chrome('C:/Users/welcome/Downloads/chromedriver_win32')
list_activities =["Wikipedia Search","Open Youtube","Open Instagram","Open Facebook","Shutdown Or Restart your system",
                        "Make calls","Sent Emails","Open Google","News"]

inbuilt_applications={"notepad":'notepad.exe',"calculator":'calc.exe'}
sites={"youtube":"youtube.com","google":"google.com","stack Overflow":"stackoverflow.com"}
questions_answered=[]
questions_unanswered=[]
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def news():
    news_url = "https://news.google.com/news/rss"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()
    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    # Print news title, url and publish date
    c_news=0
    for news in news_list:
        print(news.title.text)
        print(news.pubDate.text)
        speak(news.title.text)
        print()
        if c_news==10:
            break
        else:
            c_news=c_news+1

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")
    print("What you want me to do")
    speak("What you want me to do")
    co=1
    for i in list_activities:
        print(str(co)+"."+i)
        speak(i)
        co=co+1

def whatsapp():
    driver = webdriver.chrome()
    driver.get('https://web.whatsapp.com/')
    print("Whom you want to sent message")
    speak("Whom you want to sent message")
    target_whatsapp=takeCommand()
    print("Message you want to sent")
    speak("Message you want to sent")
    message_whatsapp=takeCommand()
    user_whatsapp=driver.find_element__by_xpath('//span[@title="{}"]'.format(target_whatsapp))
    user_whatsapp.click()
    message_box_whatsapp=driver.find_element_by_class_name('input-container')
    message_box_whatsapp.send_keys(message_whatsapp)
    button_whatsapp=driver.find_element_by_class_name('compose-btn-send')
    button_whatsapp.send()



def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please")
        return "None"
    return query

def shutdown():
    os.system("shutdown /s /t 1")

def restart():
    os.system("shutdown /r /t 1")

def introduction():
    s ="Hi, My name is Jarvis.I am working on Desktop-GS36IBC.  Windows 10 64 bit on dell system.  Model number: Inspiron 3521.  Processor Intel Core i3-3217U CPU 1.80GHz and memory of 4096mb Ram"
    speak(s)

def sendEmail():
    try:
        s_Email = smtplib.SMTP('smtp.gmail.com', 587)
        # For security and authentication, you need to pass your Gmail account credentials in the login instance.Transport layer Security
        s_Email.starttls()
        s_Email.login("madhavsinghal899@gmail.com","ritikgarg27012000")
        print("Receivers Email")
        speak("Receiver email")
        k=input()
        print("Message you want to sent")
        mess = takeCommand()

        message = "My name is madhav"
        s_Email.sendmail("madhavsinghal899@gmail.com",
                                 k, mess)
        speak("Email suceessfully sent")
        s_Email.quit()
    except Exception as e:
        speak("Sorrry!!! Email not sent")

def dial_numbers():
        TWILIO_PHONE_NUMBER = "+12563339219"

        # list of one or more phone numbers to dial, in "+19732644210" format
        DIAL_NUMBERS = ["+917302075068"]

        # URL location of TwiML instructions for how to handle the phone call
        TWIML_INSTRUCTIONS_URL = \
            "http://static.fullstackpython.com/phone-calls-python.xml"
        # replace the placeholder values with your Account SID and Auth Token
        # found on the Twilio Console: https://www.twilio.com/console
        client = TwilioRestClient(
            "AC676df48e4b2e461a95621405463dab12", "394dcfdab04686a276ca94ac4b212060")
        """Dials one or more phone numbers from a Twilio phone number."""
        for number in DIAL_NUMBERS:
            print("Dialing " + number)
            # set the method to "GET" from default POST because Amazon S3 only
            # serves GET requests on files. Typically POST would be used for apps
            client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
        if query in inbuilt_applications.keys():
        # Logic for executing tasks based on query
            for i in inbuilt_applications.keys():
                if i in query:
                    os.system(inbuilt_applications[i])
                    break
    
        elif "whatsapp" in query or "Whatsapp" in query or "WhatsApp" in query:
            whatsapp()
        elif "news" in query:
            news()
        elif "youtube" in query:
            webbrowser.open('youtube.com')
            questions_answered.append(query)
        elif "google" in query:
            webbrowser.open('google.com')
            questions_answered.append(query)
        elif "stack overflow" in query:
            webbrowser.open('stackoverflow.com')
            questions_answered.append(query)
        elif 'wikipedia' in query or "what" in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3,auto_suggest=True,redirect=True)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print("Unable to find answer")
            questions_answered.append(query)
        elif "introduction" in query:
            introduction()
            questions_answered.append(query)
        elif 'shutdown' in query:
            shutdown()
            questions_answered.append(query)
        elif 'restart' in query:
            restart()
            questions_answered.append(query)
        elif 'play music' in query:
            music_dir = 'C:\\Users\\welcome\\Desktop\\Songs\\unplugged-cover-vicky-singh-salman-khan-tere-naam-humne-kiya-hai'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            questions_answered.append(query)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            questions_answered.append(query)
        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            questions_answered.append(query)
        elif 'email' in query:
            sendEmail()
        elif "call" in query:
            dial_numbers()
        elif "questions" in query:
            print("Questions answered are:")
            for i in range(len(questions_answered)):
                print(questions_answered[i])
            print("Questions unanswered are")
            for i in range(len(questions_unanswered)):
                print(questions_unanswered[i])   
        
        elif "relax" in query:
            exit(1)         
        else:        
            questions_unanswered.append(query)






    
