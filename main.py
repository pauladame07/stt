import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

"""TIME"""
current_time = datetime.now().strftime("%I:%M %p")

rate = engine.getProperty('rate')   # getting details of current speaking rate
print(rate)                         # printing current voice rate
engine.setProperty('rate', 150)     # setting up a new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')   # getting to know the current volume level (min=0 and max=1)
print(volume)                          # printing the current volume level
engine.setProperty('volume', 0.5)    # setting up the volume level between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       # getting details of the current voice
# engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 0 for male
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

# text = input("What do you want to say?: ")
text_to_speak = "The local time now is: " + current_time
print("TTS: "+text_to_speak)
engine.say(text_to_speak)
engine.runAndWait()
engine.stop()
