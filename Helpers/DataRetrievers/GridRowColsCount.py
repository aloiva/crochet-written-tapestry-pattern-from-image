import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class GridDataGetterGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Grid Data Getter")

        # Set Clam theme
        style = ttk.Style()
        style.theme_use("clam")

        # Configure window size and background color
        self.root.geometry("600x400")
        self.root.configure(bg="#F9E0E2")  # Lighter shade background

        self.rows_entry = ttk.Entry(self.root, font=("Helvetica", 12), style="Placeholder.TEntry")
        self.rows_entry.insert(0, "Enter row count")
        self.rows_entry.pack(pady=(50, 10))

        self.cols_entry = ttk.Entry(self.root, font=("Helvetica", 12), style="Placeholder.TEntry")
        self.cols_entry.insert(0, "Enter column count")
        self.cols_entry.pack(pady=10)

        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.pack()

        self.submit_button = ttk.Button(self.root, text="Submit", command=self.get_values, style="Submit.TButton")
        self.submit_button.pack(pady=10)

        # Create a custom style for the submit button
        self.root.option_add("*TButton*padding", 10)
        self.root.option_add("*TButton*background", "#FFEB3B")  # Light yellow shade
        self.root.option_add("*TButton*foreground", "#333333")  # Dark color

        style.configure("Submit.TButton", font=("Helvetica", 14, "bold"))

        # Bindings for entry placeholders
        self.rows_entry.bind("<FocusIn>", lambda event: self.remove_placeholder_text(self.rows_entry, "Enter row count"))
        self.rows_entry.bind("<FocusOut>", lambda event: self.add_placeholder_text(self.rows_entry, "Enter row count"))
        self.cols_entry.bind("<FocusIn>", lambda event: self.remove_placeholder_text(self.cols_entry, "Enter column count"))
        self.cols_entry.bind("<FocusOut>", lambda event: self.add_placeholder_text(self.cols_entry, "Enter column count"))

        self.root.bind("<Return>", lambda event: self.submit_button.invoke())


    def remove_placeholder_text(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry["foreground"] = "black"

    def add_placeholder_text(self, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)
            entry["foreground"] = "#BDBDBD"  # Light color

    def show_error(self, message):
        self.error_label.config(text=message)

    def get_values(self):
        try:
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())
            self.root.destroy()
            self.result = [rows, cols]
        except ValueError:
            self.show_error("Please enter valid integer values.")

    def run(self):
        self.root.mainloop()

def GetRowColsCount():
    gui = GridDataGetterGUI()
    gui.run()
    return gui.result
