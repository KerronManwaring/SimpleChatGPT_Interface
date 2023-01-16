import creds
import os
import openai
from gtts import gTTS
from pygame import mixer
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from tkinter import *
window = Tk()
from tkinter import messagebox

openai.api_key = creds.OPENAI_API_KEY
engines = openai.Engine.list()
#print(engines.data[0].id)

window.title("Simple ChatGPT Interface")
window.geometry('300x100')

lbl = Label(window, text="request:")
lbl.grid(column=0, row=1)

txt = Entry(window,width=20)
txt.grid(column=1, row=1)


def speak(text):
    tts = gTTS(text, slow=False, pre_processor_funcs = [abbreviations, end_of_line]) 
    tts.save('chatGPT.mp3')
    
    mixer.init()
    mixer.music.load("chatGPT.mp3")
    mixer.music.play()

def request():
    text = txt.get()
    completion = openai.Completion.create(engine="text-davinci-003", prompt=text, max_tokens=1024)
    response = completion.choices[0].text

    speak(response)

    messagebox.showinfo('ChatGPT Response', response) 
        
btn1 = Button(window, text="Submit to chatGPT", command=request)
btn1.grid(column=1, row=2) #request


window.mainloop()

