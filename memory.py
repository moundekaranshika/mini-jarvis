memory = []

def save_memory(text):
    memory.append(text)

def get_memory():
    return memory[-5:]  # last 5 interactions
