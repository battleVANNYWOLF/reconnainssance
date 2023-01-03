import speech_recognition
import pyttsx3

rec_vocale = speech_recognition.Recognizer()
while True:
    try:
        
        with speech_recognition.Microphone() as mic:

                rec_vocale.adjust_for_ambient_noise(mic, duration="0.2")
                audio = rec_vocale.listen(mic)
                text = rec_vocale.recognize_google(audio)
                text = text.lower()

                print(f"Recognized {text}")

    except speech_recognition.UnknownValueError():

     rec_vocale = speech_recognition.Recognizer()
     continue  

