import pyttsx3 as px
import datetime

engine= px.init()
voice=engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
VoiceRate= 185
engine.setProperty('rate', VoiceRate)
def pronounce(_input):
    engine.say(_input)
    engine.runAndWait()
pronounce("Vivek")
def time():
    cur_time=datetime.datetime.now().strftime("%I,%M, %S")
    return cur_time
