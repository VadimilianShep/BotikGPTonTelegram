# -*- coding: cp1251 -*-
import pyttsx3
import openai

openai.api_key = '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'


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.7)
text = input("Введите текст:  ")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
)
    
engine.say(response.choices[0]['text'])
engine.runAndWait()
