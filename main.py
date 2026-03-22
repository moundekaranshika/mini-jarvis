from voice import speak, listen, listen_for_wake_word
from vision import start_camera
from brain import ask_ai
from memory import save_memory

import datetime

speak("Jarvis ready.")

while True:
    listen_for_wake_word()
    speak("Yes?")

    command = listen()

    save_memory(command)

    if "camera" in command:
        start_camera()

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif "who are you" in command:
        speak("I am your personal AI assistant.")

    else:
        answer = ask_ai(command)
        speak(answer)
