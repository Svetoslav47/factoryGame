import tkinter as tk


class MainMenu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Factory Game")
        self.window.geometry("400x400")

        self.is_fullscreen = False

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.window, text="Factory Game", font=("Arial", 20))
        title.pack()

        start_new_game = tk.Button(self.window, text="Start New Game", font=(
            "Arial", 10), command=self.open_start_new_game_window)
        start_new_game.pack()

        load_game = tk.Button(
            self.window, text="Load Game", font=("Arial", 10))
        load_game.pack()

        options_label = tk.Label(
            self.window, text="Options:", font=("Arial", 10))
        options_label.pack()

        screen_width_label = tk.Label(
            self.window, text="Screen Width:", font=("Arial", 10))
        screen_width_label.pack()

        self.screen_width_entry = tk.Entry(self.window)
        self.screen_width_entry.insert(0, "800")
        self.screen_width_entry.pack()

        screen_height_label = tk.Label(
            self.window, text="Screen Height:", font=("Arial", 10))
        screen_height_label.pack()

        self.screen_height_entry = tk.Entry(self.window)
        self.screen_height_entry.insert(0, "600")
        self.screen_height_entry.pack()

        fullscreen_label = tk.Label(
            self.window, text="Fullscreen:", font=("Arial", 10))
        fullscreen_label.pack()

        self.fullscreen_checkbutton = tk.Checkbutton(
            self.window, command=self.on_fullscreen_checkbutton_click)
        self.fullscreen_checkbutton.pack()

    def open_start_new_game_window(self):
        from menu.StartNewGame import StartNewGame
        screen_width = int(self.screen_width_entry.get())
        screen_height = int(self.screen_height_entry.get())

        if self.is_fullscreen:
            screen_width = self.window.winfo_screenwidth()
            screen_height = self.window.winfo_screenheight()

        self.window.destroy()

        start_new_game = StartNewGame(
            screen_width, screen_height)
        start_new_game.mainloop()

    def open_load_game_window(self):
        self.window.destroy()
        import menu.loadGame

    def on_fullscreen_checkbutton_click(self):
        self.is_fullscreen = not self.is_fullscreen
        print(self.is_fullscreen)

    def mainloop(self):
        self.window.mainloop()

    def destroy(self):
        self.window.destroy()
