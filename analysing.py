# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 11:41
# @Author  : WANG Yuteng
# @FileName: analysing.py
import speech_recognition as sr
import nltk
def analysing(Reaudio):
    tokens = nltk.word_tokenize(Reaudio)
    print("result of the recording　：")
    print(tokens)
    print("___________________________")
    lens = len(tokens)
    for i in range(lens):
        if tokens[i] == "camera" or tokens[i] == "Camera": # use 'and' can also search the little dog or something
            for i in range(i+1,lens): # we can also search the action after the dog by setting i.
                if tokens[i] == "red": # or tokens[i] == "eat": # we can add more actions
                    result = 1
                    return result
                elif tokens[i] == "green":
                    result = 2
                    return result
                elif tokens[i] == "blue":
                    result = 3
                    return result
                else :
                    print("No color recognition request.")
                    print("_____________________________")
                    result = 0
                    return result
        else :
            print("the recognition is not active.")
            print("______________________________")