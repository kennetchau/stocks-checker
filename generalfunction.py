import speech_recognition as sr
import datetime

def sR():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        print("Speak anything: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            print("Sorry could not recognize you voice")
            return ""



def getnumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Please input an integer!")
            continue
        else:
            return userInput
            break

def changestringtodate(input):
    format_str = '%Y/%m/%d'
    datetime_obj = datetime.datetime.strptime(input,format_str)
    return datetime_obj

