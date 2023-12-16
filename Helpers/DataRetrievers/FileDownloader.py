import tkinter as tk
from tkinter import filedialog, simpledialog
import os
import shutil
import tkinter.ttk as ttk

class FileDownloadApp:
    def __init__(self, root, temp_file_path):
        self.root = root
        self.root.title("File Download App")

        style = ttk.Style()
        style.theme_use("clam")

        self.temp_file_path = temp_file_path

        self.save_button = ttk.Button(self.root, text="Save Pattern", command=self.save_pattern)
        self.save_button.pack(pady=10)

        self.view_button = ttk.Button(self.root, text="View Pattern", command=self.view_pattern)
        self.view_button.pack(pady=10)

        self.root.configure(bg="#f0f0f0")  # Set background color

        self.root.geometry(f"{300}x{200}")

    def save_pattern(self):
        file_name = simpledialog.askstring("Save Pattern", "Enter file name:", parent=self.root)
        if file_name:
            self.selected_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=file_name)
            if self.selected_path:
                self.move_file()
            self.root.destroy()  # Destroy the GUI after saving

    def move_file(self):
        new_file_path = self.selected_path
        shutil.copy(self.temp_file_path, new_file_path)

    def view_pattern(self):
        os.startfile(self.temp_file_path)
        self.root.destroy()  # Destroy the GUI after viewing

def DownloadOrViewFile(temp_file_path):
    root = tk.Tk()
    app = FileDownloadApp(root, temp_file_path)
    root.mainloop()

if __name__ == "__main__":
    DownloadOrViewFile("C:/Users/Pranava Vedagnya/Documents/projects/tapestry-pattern-from-image/pattern-python/tmp/tmpmkb274d4.txt")
