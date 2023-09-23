import tkinter as tk
import sys
import logging
from logging import StreamHandler

MAX_LINES = 100  # Maximum number of lines to keep in the log window

class LogRedirector:
    def __init__(self, widget):
        self.widget = widget
        self.line_count = 0
        # Configure the text widget's colors
        self.widget.config(bg="black", fg="green")  # Set background to black and text to white


    def write(self, text):
        # Insert the text
        self.widget.insert(tk.END, text)
        # Count the number of lines in the widget
        self.line_count = int(self.widget.index(tk.END).split('.')[0])

        # Check if the line count exceeds the maximum
        if self.line_count > MAX_LINES:
            # Calculate how many lines to delete
            delete_count = self.line_count - MAX_LINES
            # Delete the extra lines from the beginning of the text
            self.widget.delete(1.0, f"{delete_count}.0")

        self.widget.see(tk.END)  # Scroll to the end to keep the latest messages visible

    def clear_log(self):
        self.log_text.delete(1.0, tk.END)

def log_to_window(message):
    # Redirect to the log Text widget
    sys.stdout.write(message + '\n')

def start_log_window():
    root = tk.Tk()
    root.title("Log Window")

    # Set the initial size of the log window (width x height)
    width = 200
    height = 300
    screen_size = str(width) + "x" + str(height)
    root.geometry(screen_size)  # Adjust the values as needed
    # Set the initial position of the log window (right-aligned)
    screen_width = root.winfo_screenwidth()
    window_width = width  # Adjust the window width as needed
    x_position = screen_width - window_width
    root.geometry(f"{window_width}x{str(height)}+{x_position}+0")

    log_text = tk.Text(root)
    log_text.pack(fill=tk.BOTH, expand=True)  # Fill the available space and expand with the window

    # Redirect stdout to your custom log redirector
    sys.stdout = LogRedirector(log_text)

    # Example usage (generating a lot of output)
    print("  --- Log Console ---  ")

    root.mainloop()