import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time





def sptext():
    recognizer=sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("reccognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" NOt Understand ")

# sptext()


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)           # 1 for lady and 0 for man voice.
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(x)
    engine.runAndWait()

# speechtx(" Hello python")


if __name__ == '__main__':


    if  "hey peter" in sptext().lower():
        while True:
                data1 = sptext().lower()

                if "your name" in data1:
                    name = " my name is peter"
                    speechtx(name)

                elif "old are you" in data1:
                    age = " i am two years old"
                    speechtx(age)

                elif "time" in data1:
                    time = datetime.datetime.now().strftime("%I%M%p")
                    speechtx(time)

                elif "youtube" in data1:
                    webbrowser.open("https://www.youtube.com/")


                elif "web" in data1:
                    webbrowser.open("https://www.youtube.com/watch?v=N-iO1tDmP1A&t=3368s")

                elif "joke" in data1:
                    joke_1 = pyjokes.get_joke(language="en", category="neutral")
                    print(joke_1)
                    speechtx(joke_1)


                elif "exit" in data1:
                    speechtx("thank you")
                    break

                time.sleep(5)

    else:
        print("thanks")
