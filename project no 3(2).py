import speech_recognition as sr
import webbrowser
import pyttsx3

recogniner = sr .Recognizer()
engine = pyttsx3.init()
import musicLibrary 
def speak(text):
    engine.say(text)
    engine.runAndWait()
def ProcessCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open games" in c.lower():
        webbrowser.open("https://poki.com/en/g/level-devil")       
    elif c.lower().startswith("play"):

     parts = c.lower().split(" ", 1)
    if len(parts) > 1:
        song = parts[1].strip()       
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"{song} not found in music library.")
    else:
        speak("Please say the song name after 'play'.")
   # else:

    pass    
     
if __name__=="__main__":
    speak(" My Liege, I am for your service , my name is Beru..")
    while True:
     #Listen for the wake word "arise"
     #obtain audio from the microphone
     r = sr.Recognizer()
      
        #recognize speech using Google Speech Recognition
     print("Roger that ")
     try:
            with sr.Microphone() as source:
              print("Roger")
              audio = r.listen(source,timeout=2,phrase_time_limit=1)
              word = r.recognize_google(audio)
            if(word.lower() == "arise"):
                speak("Ya")
                #listen for the  command
                with sr.Microphone( ) as source:
                     print("command me my liege")
                     audio = r.listen(source)
                     command = r.recognize_google(audio)
                
                     ProcessCommand(command)
     except Exception as e:
            print("Error;{0}".format(e))    
            

    
