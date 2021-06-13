import pyttsx3 as px
import datetime

engine= px.init()
voice=engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
VoiceRate= 170
engine.setProperty('rate', VoiceRate)
def pronounce(_input):
    engine.say(_input)
    engine.runAndWait()
pronounce("Hello. This is dodo. How may I help you?")
def time():
    cur_time=datetime.datetime.now().strftime("%I,%M, %S") 
    pronounce(cur_time)
def date():
    year=datetime.datetime.now().year
    month= datetime.datetime.now().month
    day=datetime.datetime.now().day
    pronounce("Today's date is ")
    date_tod="{}, {}, {}".format(day, month, year)
    pronounce(date_tod)

