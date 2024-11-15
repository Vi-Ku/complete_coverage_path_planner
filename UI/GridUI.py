import tkinter as tk
from tkinter import messagebox

class GridApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Grid Creator")
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        tk.Label(self.frame, text="Rows:").grid(row=0, column=0)
        self.rows_entry = tk.Entry(self.frame)
        self.rows_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Columns:").grid(row=1, column=0)
        self.cols_entry = tk.Entry(self.frame)
        self.cols_entry.grid(row=1, column=1)

        self.create_button = tk.Button(self.frame, text="Create Grid", command=self.create_grid)
        self.create_button.grid(row=2, column=0, columnspan=2, pady=10)

    def create_grid(self):
        try:
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())
            if rows > 0 and cols > 0:
                self.master.destroy()  # Close the current window
                ObstacleSelectionApp(rows, cols)  # Open the new window
            else:
                messagebox.showerror("Invalid Input", "Rows and columns must be positive integers.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for rows and columns.")

class ObstacleSelectionApp:
    def __init__(self, rows, cols):
        self.root = tk.Tk()
        self.root.title("Obstacle Selection")
        self.rows = rows
        self.cols = cols
        self.cell_size = 30
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.create_grid()

    def create_grid(self):
        self.canvas = tk.Canvas(self.root, width=self.cols*self.cell_size, height=self.rows*self.cell_size)
        self.canvas.pack()

        for i in range(self.rows):
            for j in range(self.cols):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        x1 = col * self.cell_size
        y1 = row * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size

        if self.grid[row][col] == 0:
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            self.grid[row][col] = 1
        else:
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            self.grid[row][col] = 0

def main():
    root = tk.Tk()
    app = GridApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()