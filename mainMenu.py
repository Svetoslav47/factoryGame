import tkinter as tk


window = tk.Tk()

window.title("Factory Game")
window.geometry("400x400")

title = tk.Label(text="Factory Game", font=("Arial", 20))
title.pack()

start_new_game = tk.Button(text="Start New Game", font=("Arial", 10))
start_new_game.pack()

load_game = tk.Button(text="Load Game", font=("Arial", 10))
load_game.pack()

optionsLabel = tk.Label(text="Options:", font=("Arial", 10))
optionsLabel.pack()

screen_width_label = tk.Label(text="Screen Width:", font=("Arial", 10))
screen_width_label.pack()

screen_width_entry = tk.Entry()
screen_width_entry.pack()

screen_height_label = tk.Label(text="Screen Height:", font=("Arial", 10))
screen_height_label.pack()

screen_height_entry = tk.Entry()
screen_height_entry.pack()

fullscreen_label = tk.Label(text="Fullscreen:", font=("Arial", 10))
fullscreen_label.pack()

# select true or false
fullscreen_true = tk.Button(text="True", font=("Arial", 10))
fullscreen_true.pack()

fullscreen_false = tk.Button(text="False", font=("Arial", 10))
fullscreen_false.pack()

window.mainloop()
