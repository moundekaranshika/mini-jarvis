def listen_for_wake_word():
    while True:
        text = listen()
        if "jarvis" in text:
            return True
