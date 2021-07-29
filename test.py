
from textblob import TextBlob
from gtts import gTTS
import os
from playsound import playsound  
import speech_recognition as sr

def translate(line, lang="hi" ):
    blob = TextBlob(line)
    translated_sentence = blob.translate(to = lang)
    translated_sentence = str(translated_sentence)
    return translated_sentence
 
recognizer = sr.Recognizer()
with sr.Microphone() as inputs:
    print("Please speak now")
    listening = recognizer.listen(inputs)
    print("Analysing...")

    try:
         b=recognizer.recognize_google(listening)
         b=str(b) 
    except:
         print("please speak again")

output = translate(b) 

obj = gTTS(text=output, slow=False)
obj.save("translation.mp3")
playsound('translation.mp3')


         

