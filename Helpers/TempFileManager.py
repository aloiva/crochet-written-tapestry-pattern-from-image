import tempfile
import os

class TempFileManager:
    def __init__(self):
        self.temp_file = None
        self.temp_file_path = None

    def create_temp_file(self):
        self.temp_file = tempfile.NamedTemporaryFile(suffix=".txt", delete=False)
        self.temp_file_path = self.temp_file.name
        return self.temp_file_path

    def open_temp_file(self):
        if self.temp_file_path:
            os.startfile(f'"{self.temp_file_path}"')

    def close_temp_file(self):
        if self.temp_file:
            self.temp_file.close()

def CreateTempFile():
    filemngr = TempFileManager()
    return filemngr.create_temp_file()

# Example usage
if __name__ == "__main__":
    temp_manager = TempFileManager()
    temp_file_path = temp_manager.create_temp_file()
    print(f"Temporary file created at: {temp_file_path}")

    temp_manager.open_temp_file()

    # Clean up
    temp_manager.close_temp_file()
