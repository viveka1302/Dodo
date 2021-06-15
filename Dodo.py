import pyttsx3 as px
import datetime
import speech_recognition as sr
import tkinter as tk
import wikipedia as wk
import webbrowser as wb

engine= px.init()
voice=engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
VoiceRate= 170
engine.setProperty('rate', VoiceRate)
def pronounce(_input):
    engine.say(_input)
    engine.runAndWait()
def time():
    cur_time=datetime.datetime.now().strftime("%I,%M, %S") 
    pronounce("The time is ")
    pronounce(cur_time)
def date():
    year=datetime.datetime.now().year
    month= datetime.datetime.now().month
    day=datetime.datetime.now().day
    pronounce("Today's date is ")
    date_tod="{}, {}, {}".format(day, month, year)
    pronounce(date_tod)
def get_command():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio= r.listen(source)
    try:
        print('recognizing...')
        query = r.recognize_google(audio, language='en-US')
        print(query)
        return query
    except Exception as e:
        print(e)
        pronounce("Say that again please...")
        return None
    return query
def OnClick():
    x=str(get_command()).lower()
    inp.config(text=x)
    if "time" in x:
        time()
    if "date" in x:
        date()
    elif "open" in x:
        q=x.replace("open",'').lower()
        wb.open(q+".com")
    elif ("wikipedia" or "wiki" or "look up" or "search") in x:
        q=x.replace("wikipedia" or "wiki" or "look up" or "search", " ")
        try:
            result=str(wk.summary(q, sentences=2))
            result=result.replace(". ",".\n")
            reply.config(text=result)
            pronounce("Here's what I found on wikipedia:")
            pronounce(result)
        except Exception as e:
            print(e)
            reply.config(text='Whoops! No matching results found')
            pronounce("No results found")
    elif "do you remember" in x:
        pronounce("This is what you asked me to remember that")
        remem=open("remem.txt", "r")
        pronounce(remem.read())
    elif "remember" in x:
        pronounce("What should I remember?")
        q=str(get_command()).lower()
        remember=open("remem.txt", "w")
        remember.write(q)
        pronounce("I shall remember that {}".format(q))
        remember.close()
    
window=tk.Tk()
window.title('Dodo: The smart voice assistant')
window.geometry('720x360')
but=tk.Button(window, text="Mic On", fg='blue', command=OnClick)
but.pack()
inp=tk.Label(window, text=' ')
inp.pack()
reply=tk.Label(window, text='')
reply.pack()
pronounce("Hello. This is dodo. How may I help you?")
window.mainloop()
