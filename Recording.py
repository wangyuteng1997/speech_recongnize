# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 11:40
# @Author  : WANG Yuteng
# @FileName: Recording.py
import speech_recognition as sr
import nltk

def recording():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Say Camera to active the AI. And say 'red object', 'green object' or "
              "'xxx object' to know how many objects in the camera.")
        audio = r.listen(source)
        Reaudio = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + Reaudio)
    return Reaudio


