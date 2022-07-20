import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while 1:

    try:
        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio = r.listen(source2)
            # Using google to recognize audio
            speech = r.recognize_google(audio, language="ar-SA")
            print(speech)


    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")

    break
