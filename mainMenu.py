import tkinter as tk


class MainMenu():
    def __init__(self):
        window = tk.Tk()
        window.title("Factory Game")
        window.geometry("500x500")
        window.resizable(False, False)
        lable = tk.Label(window, text="Factory Game Main Menu")
        lable.pack()
        window.mainloop()


mainMenu = MainMenu()
