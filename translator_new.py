from textblob import TextBlob
from gtts import gTTS
import os
from playsound import playsound  
import speech_recognition as sr
 
class Translator(object):
    def __init__(self, lang='hi'):
   
        ''' lang : The language to which the speech needs to be translated (default : Hindi) '''
        ''' output : The translated text '''
        self.lang = lang
        self.output = None
    
    ''' function for translating the speech '''
    def translate(self, lang='hi'):
        
        ''' function for text to text translation '''
        def text_translate(line):
            blob = TextBlob(line)
            translated_sentence = blob.translate(to = lang)
            translated_sentence = str(translated_sentence)
            return translated_sentence
           
        ''' user input through microphone '''
        recognizer = sr.Recognizer()
        with sr.Microphone() as inputs:
            print("Please speak now")
            listening = recognizer.listen(inputs)
            print("Analysing...")
            
            ''' language recognization and speech to text conversion '''
            try:
                b=recognizer.recognize_google(listening)
                b=str(b) 
            except:
                print("please speak again")
        
        self.output = text_translate(b)
        
        ''' text to speech conversion '''
        obj = gTTS(text=self.output, lang="hi", slow=False)
        obj.save("translation.mp3")
        playsound('translation.mp3')
