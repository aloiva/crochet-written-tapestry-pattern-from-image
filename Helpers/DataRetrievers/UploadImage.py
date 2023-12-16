import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab
import io
import requests
from tkinter import ttk

class ImageUploadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Upload")

        self.selected_image = None

        # Set the background color to a light blueish shade
        self.root.configure(bg="#E6F0F3")

        self.style = tk.ttk.Style()
        self.style.theme_use("clam")  # Set the theme to "clam"

        self.instructions_label = tk.Label(self.root, text="Upload an image or paste from clipboard or provide a URL:", font=("Helvetica", 14, "bold"), bg="#E6F0F3")
        self.instructions_label.pack(pady=10)

        # Create a frame for the "Choose Image" and "Paste Image" buttons
        button_frame = tk.Frame(self.root, bg="#E6F0F3")
        button_frame.pack()

        # "Choose Image" button with lighter lime green shade and contrasting text
        self.upload_button = tk.Button(button_frame, text="Choose Image", command=self.upload_image, bg="#B2FF99", fg="#333333")
        self.upload_button.pack(side="left", padx=5)

        # "Or" text
        or_label = tk.Label(button_frame, text="Or", font=("Helvetica", 12, "bold"), bg="#E6F0F3")
        or_label.pack(side="left", padx=5)

        # "Paste Image" button with lighter lavender-purplish shade and contrasting text
        self.paste_button = tk.Button(button_frame, text="Paste Image (from clipboard)", command=self.paste_image, bg="#D8BFD8", fg="#333333")
        self.paste_button.pack(side="left", padx=5)

        # Add a small gap between buttons and the URL entry
        tk.Label(self.root, text="", bg="#E6F0F3").pack()

        # "Submit URL" button with lighter reddish-pink shade and contrasting text
        self.download_button = tk.Button(self.root, text="Submit URL", command=self.download_image, bg="#FFCCCC", fg="#333333", font=("Helvetica", 12, "bold"))
        
        # URL Entry with placeholder text
        self.url_entry = tk.Entry(self.root, font=("Helvetica", 12), width=40, fg="#333333", borderwidth=2, relief="solid")
        self.url_entry.insert(0, "Enter Image URL")  # Placeholder text
        self.url_entry.bind("<FocusIn>", self.remove_placeholder_text)
        self.url_entry.bind("<FocusOut>", self.add_placeholder_text)

        # Pack URL Entry and Submit URL button
        self.url_entry.pack(pady=5)
        self.download_button.pack(pady=10)

        # Bind Ctrl+V to the paste_image() function
        self.root.bind("<Control-v>", self.paste_image_event)
    
    def remove_placeholder_text(self, event):
        if self.url_entry.get() == "Enter Image URL":
            self.url_entry.delete(0, tk.END)
            self.url_entry.config(fg="#333333")  # Set text color to contrast

    def add_placeholder_text(self, event):
        if not self.url_entry.get():
            self.url_entry.insert(0, "Enter Image URL")
            self.url_entry.config(fg="#999999")  # Set placeholder text color

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.selected_image = Image.open(file_path)
            self.root.destroy()

    def paste_image(self):
        clipboard_image = self.get_image_from_clipboard()
        if clipboard_image:
            self.selected_image = clipboard_image
            self.root.destroy()

    def get_image_from_clipboard(self):
        try:
            clipboard_image = ImageGrab.grabclipboard()
            if clipboard_image:
                return clipboard_image
            else:
                print("No image found in clipboard.")
                return None
        except Exception as e:
            print("Error:", e)
            return None
        
    def paste_image_event(self, event):
        self.paste_image()

    def download_image(self):
        url = self.url_entry.get()
        if url:
            response = requests.get(url)
            if response.status_code == 200:
                img_stream = io.BytesIO(response.content)
                img = Image.open(img_stream)
                self.selected_image = img
                self.root.destroy()
        else:
            print("Please enter a url")

def GetImage():
    root = tk.Tk()
    app = ImageUploadApp(root)
    root.geometry("600x400")
    root.mainloop()
    return app.selected_image

if __name__ == "__main__":
    uploaded_image = GetImage()
    if uploaded_image:
        uploaded_image.show()  # Display the selected image (PIL Image object)
    else:
        print("No image selected.")
