from textblob import TextBlob
from gtts import gTTS
import os
from playsound import playsound  
import speech_recognition as sr
 
class Translator(object):
    def __init__(self, lang='hi'):
        self.lang = lang
        self.recognizer = sr.Recognizer()
        self.output = None

    def translate(self, lang):

        def text_translate(line):
            blob = TextBlob(line)
            translated_sentence = blob.translate(to = self.lang)
            translated_sentence = str(translated_sentence)
            return translated_sentence

        with sr.Microphone() as inputs:
            print("Please speak now")
            listening = self.recognizer.listen(inputs)
            print("Analysing...")

            try:
                b=self.recognizer.recognize_google(listening)
                b=str(b) 
            except:
                print("please speak again")

        self.output = self.text_translate(b)

        obj = gTTS(text=self.output, lang="hi", slow=False)
        obj.save("translation.mp3")
        playsound('translation.mp3')