
 
import speech_recognition as sr
import pyttsx3
 
r = sr.Recognizer()
 
def SpeakText(command):
     
    # Initialize the engine
    eng = pyttsx3.init()
    eng.say(command)
    eng.runAndWait()
     
     
# Loop infinitely for user to
# speak
 
while(1):   
     
    try:
        with sr.Microphone() as source2:
             
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            audio2 = r.listen(source2)
             
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
 
            print("Did you say ",MyText)
            SpeakText(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")