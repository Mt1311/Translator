# Translator
Communication gaps are quite prevalent in our country because of the linguistic diversity. Through this project, we can reduce the communication issues faced by us in our day to day lives by utilising the technology of automatic language translation. This repository holds the code for the implementation of Speech to Speech Translation in python. With the help of this product, the user can translate from any language to any language as required by the user.
<br>

## Steps Involved
- Imported the required modules.

- Initialised the class variables.

- Audio input is taken and converted into a text.

- The text is translated to the required language.

- The translated text is converted back to facilitate an audio output.
<br>

## Languages and their codes supported by TextBlob
<img src = 'results/language_codes.png'>

## Installation and Usage Guidelines
To use the repo for speech to speech translation follow the guidelines given below-

- Cloning the Repository: 

        git clone https://github.com/Mt1311/Translator
        
- Setting up the Python Environment with dependencies:

        pip install -r requirements.txt

- Running the file for inference:

        python3 inference.py
 <br>
 
The inference file gives a choice of setting languages. To translate the input in Hindi, the user needs to specify the choice as 1.

```python
choice = int(input('Do you want the translated speech to be in Hindi or in any other language? Enter 1 if it is Hindi and enter 0 if it is any other language: '))
```
To translate it into any other language, the user needs to specify the choice as 0 and enter the required language to which the input is to be translated.

```python
choice = int(input('Do you want the translated speech to be in Hindi or in any other language? Enter 1 if it is Hindi and enter 0 if it is any other language: '))
lang = input('Enter the language to which the input needs to be translated: ')
```
 
 ## Results
 Samples of translated audio files can be found in the directory named <a href='results/'>results</a>
