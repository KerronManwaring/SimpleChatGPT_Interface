import creds
import os
import openai

from tkinter import *
window = Tk()
from tkinter import messagebox


window.title("Simple ChatGPT Interface")
window.geometry('300x100')

lbl = Label(window, text="request:")
lbl.grid(column=0, row=1)
txt = Entry(window,width=20)
txt.grid(column=1, row=1)

openai.api_key = creds.OPENAI_API_KEY
engines = openai.Engine.list()
print(engines.data[0].id)


def request():
    text = txt.get()
    completion = openai.Completion.create(engine="text-davinci-003", prompt=text, max_tokens=1024)
    #print(text)
    #print(completion.choices[0].text)
    messagebox.showinfo('ChatGPT Response', completion.choices[0].text)

        
btn1 = Button(window, text="Submit to chatGPT", command=request)
btn1.grid(column=1, row=2) #request

window.mainloop()
