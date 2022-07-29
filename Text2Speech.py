#pyttsx3 package must be installed first in order for the programm to work
import pyttsx3  #this is the package which works on offline if you need online you can choose gts package

engine = pyttsx3.init() #creating a object
for voice in engine.getProperty("voices"): #getting voices which are available in our system
    print(voice)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) # choosing voice

def Speak(Audio): #function to change text to audio
    engine.say(Audio)
    engine.runAndWait()

text = input("Enter your text now: ") #input for text
Speak(text) #calling the function which coverts the text to speech.


