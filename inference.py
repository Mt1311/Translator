from translator_new import Translator

choice = int(input('Do you want the translated speech to be in Hindi or in any other language? Enter 1 if it is Hindi and enter 0 if it is any other language: '))
               
if choice == 1:
  Translator.translate(Translator, lang='hi')
else:
  lang = input('Enter the language to which the input needs to be translated: ')
  Translator.translate(Translator, lang=lang)
