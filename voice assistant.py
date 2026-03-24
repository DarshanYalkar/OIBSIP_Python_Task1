import speech_recognition as sr
import datetime

recognizer = sr.Recognizer()

def listen_command():
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError:
        print("Network issue")
        return ""

def process_command(text):
    if "hello" in text:
        print("Hello! Nice to meet you")

    elif "time" in text:
        now = datetime.datetime.now()
        print("Time is:", now.strftime("%H:%M"))

    elif "date" in text:
        today = datetime.date.today()
        print("Date is:", today)

    elif "exit" in text:
        print("Exiting assistant...")
        return False

    else:
        print("Command not recognized")

    return True



running = True
while running:
    command = listen_command()
    if command:
        print("You said:", command)
        running = process_command(command)
