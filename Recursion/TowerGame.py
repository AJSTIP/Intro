# TowerGame.py
import tkinter as tk
import time

class TowerOfHanoiGUI:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.window = tk.Tk()
        self.window.title("Towers of Hanoi")
        self.canvas = tk.Canvas(self.window, width=600, height=400, bg="white")
        self.canvas.pack()

        # Rod positions
        self.rod_positions = [150, 300, 450]
        self.rods = [[], [], []]

        # Create rods and disks
        self.create_rods()
        self.create_disks()

        # Add reset button
        reset_button = tk.Button(self.window, text="Reset", command=self.reset_game)
        reset_button.pack()

        # Add move label
        self.move_label = tk.Label(self.window, text="Move: 0", bg="white", font=("Arial", 14))
        self.move_label.pack()

    def create_rods(self):
        for i, x in enumerate(self.rod_positions):
            self.canvas.create_line(x, 100, x, 300, width=5, fill="black")
            self.canvas.create_text(x, 320, text=f"Rod {i+1}", fill="black", font=("Arial", 12))

    def create_disks(self):
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        for i in range(self.num_disks, 0, -1):
            width = i * 20
            color = colors[(i - 1) % len(colors)]
            disk = self.canvas.create_rectangle(
                self.rod_positions[0] - width // 2,
                300 - len(self.rods[0]) * 20,
                self.rod_positions[0] + width // 2,
                320 - len(self.rods[0]) * 20,
                fill=color,
                outline="black"
            )
            self.rods[0].append(disk)

    def move_disk(self, from_rod, to_rod):
        disk = self.rods[from_rod].pop()
        self.rods[to_rod].append(disk)

        # Calculate new position
        x_start, _, x_end, _ = self.canvas.coords(disk)
        disk_width = x_end - x_start
        new_x_start = self.rod_positions[to_rod] - disk_width // 2
        new_y_start = 300 - len(self.rods[to_rod]) * 20

        # Animate the movement
        while True:
            current_x_start, current_y_start, _, _ = self.canvas.coords(disk)
            if abs(current_x_start - new_x_start) < 1 and abs(current_y_start - new_y_start) < 1:
                break
            dx = (new_x_start - current_x_start) * 0.2
            dy = (new_y_start - current_y_start) * 0.2
            self.canvas.move(disk, dx, dy)
            self.canvas.update()
            time.sleep(0.005)

    def reset_game(self):
        self.canvas.delete("all")
        self.rods = [[], [], []]
        self.create_rods()
        self.create_disks()

    def update_move_label(self, move_number):
        self.move_label.config(text=f"Move: {move_number}")
        self.window.update()

def towers_of_hanoi(gui, n, source, target, auxiliary, move_number=None):
    if move_number is None:
        move_number = [0]
    if n == 1:
        tracking(move_number, gui, source, target)
        return
    towers_of_hanoi(gui, n - 1, source, auxiliary, target, move_number)
    tracking(move_number, gui, source, target)
    towers_of_hanoi(gui, n - 1, auxiliary, target, source, move_number)

def tracking(move_number, gui, source, target):
    move_number[0] += 1
    gui.update_move_label(move_number[0])
    gui.move_disk(source, target)

if __name__ == "__main__":
    num_disks = 6  # You can change the number of disks here
    gui = TowerOfHanoiGUI(num_disks)
    towers_of_hanoi(gui, num_disks, 0, 2, 1)
    gui.window.mainloop()