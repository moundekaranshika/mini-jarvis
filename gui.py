import tkinter as tk

def launch_gui():
    root = tk.Tk()
    root.title("Jarvis AI")

    label = tk.Label(root, text="Jarvis is running...", font=("Arial", 16))
    label.pack(pady=20)

    root.mainloop()
