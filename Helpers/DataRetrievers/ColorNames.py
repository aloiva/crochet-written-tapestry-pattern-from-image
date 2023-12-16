import tkinter as tk
from tkinter import messagebox, ttk
import math

class ColorNameEditor:
    def __init__(self, root, color_data):
        self.root = root
        self.root.title("Color Name Editor")

        self.color_data = color_data
        self.keys = list(color_data.keys())

        self.info_label = ttk.Label(self.root, text="Edit Color Names", font=("Helvetica", 16, "bold"))
        self.info_label.pack(pady=10)

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.entries = []
        c = len(color_data)
        n = math.isqrt(c)  # Initial guess for n
        m = math.ceil(c / n)  # Initial guess for n
        while m * n < c:
            n += 1
            m = math.ceil(c / n)

        # print("m: ", m, "n: ", n)

        for i, hex_color in enumerate(self.keys):
            color_name = self.color_data[hex_color]
            entry = tk.Entry(self.frame, font=("Helvetica", 12), width=20)
            entry.placeholder = f"{color_name}"
            entry.insert(0, entry.placeholder)
            entry.bind("<FocusIn>", self.remove_placeholder_text)
            entry.bind("<FocusOut>", self.add_placeholder_text)
            self.entries.append(entry)

            color_box = tk.Canvas(self.frame, width=25, height=25)
            color_box.create_rectangle(0, 0, 50, 50, fill=hex_color)
            color_box.grid(row=i % m, column=i // m * 2, padx=10, pady=5)
            entry.grid(row=i % m, column=i // m * 2 + 1, padx=10, pady=5)

        self.submit_button = ttk.Button(self.root, text="Submit", command=self.submit_names)
        self.submit_button.pack(pady=10)

        self.root.bind("<Return>", self.submit_names)

        # Calculate the required window size based on the number of colors and columns
        column_width = 50 + (2 * 10 ) + (20 * 10)  # Color box width + padding + textbox width
        window_width = n * column_width + 40
        window_height = m * 60 + 160  # Height per color + padding

        # print("window_width: ", window_width)
        # print("window_height: ", window_height)
        self.root.geometry(f"{window_width}x{window_height}")

    def remove_placeholder_text(self, event):
        entry = event.widget
        if entry.get() == entry.placeholder:
            entry.delete(0, "end")

    def add_placeholder_text(self, event):
        entry = event.widget
        if not entry.get():
            entry.insert(0, entry.placeholder)

    def submit_names(self, event=None):
        for i, hex_color in enumerate(self.keys):
            new_name = self.entries[i].get()
            if new_name.lower() != self.entries[i].placeholder.lower():
                new_name = new_name.lower().replace("'", "").replace(",", "").replace(" ", "_")
                self.color_data[hex_color] = new_name
        self.show_confirmation()

    def show_confirmation(self):
        confirm = messagebox.askquestion("Confirmation", "Are you sure you want to save changes?", icon="warning")
        if confirm == "yes":
            self.root.destroy()
            print("Color data:", self.color_data)

def GetNewColorData(color_data):
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use("clam")
    app = ColorNameEditor(root, color_data)
    root.mainloop()
    return app.color_data

if __name__ == "__main__":
    color_data = {
        "#FF0000": "red",
        "#00FF00": "green",
        "#0000FF": "blue",
        "#FFFF00": "yellow",
        "#FF00FF": "magenta",
        "#00FFFF": "cyan",
        "#800080": "purple",
        "#FFA500": "orange",
        "#808080": "gray",
        "#800000": "maroon"
    }
    color_data = GetNewColorData(color_data)
    print(color_data)