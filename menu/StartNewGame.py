import tkinter as tk


class StartNewGame:
    def __init__(self, screen_width, screen_height):
        self.window = tk.Tk()

        self.window.title("Factory Game")
        self.window.geometry("400x400")

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.create_widgets()

    def create_widgets(self):
        grid_width_label = tk.Label(
            self.window, text="Grid Width:", font=("Arial", 10))
        grid_width_label.pack()

        self.grid_width_entry = tk.Entry(self.window)
        self.grid_width_entry.insert(0, "20")
        self.grid_width_entry.pack()

        grid_height_label = tk.Label(
            self.window, text="Grid Height:", font=("Arial", 10))
        grid_height_label.pack()

        self.grid_height_entry = tk.Entry(self.window)
        self.grid_height_entry.insert(0, "20")
        self.grid_height_entry.pack()

        seed_label = tk.Label(
            self.window, text="Seed:", font=("Arial", 10))
        seed_label.pack()

        self.seed_entry = tk.Entry(self.window)
        self.seed_entry.insert(0, "igraPoScriptovi<3")
        self.seed_entry.pack()

        start_game = tk.Button(
            self.window, text="Start Game", font=("Arial", 10), command=self.start_game)
        start_game.pack()

    def start_game(self):
        from GameManager import GameManager
        grid_width = int(self.grid_width_entry.get())
        grid_height = int(self.grid_height_entry.get())
        seed = self.seed_entry.get()

        self.window.destroy()

        game_manager = GameManager(
            grid_width, grid_height, seed, self.screen_width, self.screen_height)
        game_manager.mainloop()

    def on_fullscreen_checkbutton_click(self):
        self.is_fullscreen = not self.is_fullscreen
        print(self.is_fullscreen)

    def mainloop(self):
        self.window.mainloop()
