# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 10:21
# @Author  : WANG Yuteng
# @FileName: main.py
# import Os module to start the audio file
import os
import video
from gtts import gTTS
import speech_recognition as sr
import nltk
import Recording
import analysing
if __name__ == '__main__':
 result = 0

 #voice recognition system
 Reaudio = Recording.recording()

 #order recognition system
 result = analysing.analysing(Reaudio)

 ###real time image processing system
 num_green,num_red,num_blue = video.camera()

 ########text to speech system########
 if(result == 1):
     myText = "there is " + str(num_red) + "red objects"
 elif(result == 2):
     myText = "there is " + str(num_green) + " green objects "
 elif(result == 3):
     myText = "there is " + str(num_blue) + " blue objects "

 print(myText)

 # Language we want to use
 language = 'en'

 output = gTTS(text=myText, lang=language, slow=False)

 output.save("output.mp3")

 #  Play the converted file
 os.system("start output.mp3")