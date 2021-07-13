import pyttsx3
engine = pyttsx3.init()
speech = input("Say Something: \n")
engine.say(speech)
engine.runAndWait()
