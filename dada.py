# -*- coding: cp1251 -*-
import pyttsx3
engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 0.7)
text = input("Введите текст:  ")
engine.say(text)
engine.runAndWait()
