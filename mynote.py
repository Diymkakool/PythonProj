import tkinter as tk
from tkinter import filedialog, messagebox
import argparse

# Global variable to store the currently open file path
current_file_path = None

def savefile():
    """Save the content of the text editor to a file."""
    global current_file_path
    if not current_file_path:
        current_file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All Files", "*.*")]
        )
    if current_file_path:
        try:
            with open(current_file_path, "w", encoding="utf-8") as file:
                file.write(text.get("1.0", tk.END))
                print(f"File saved: {current_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

def openfile():
    """Open a file and load its content into the text editor."""
    global current_file_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                text.delete("1.0", tk.END)  
                text.insert("1.0", content)  
                current_file_path = file_path
                print(f"File opened: {current_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while opening the file: {e}")

def load_file_from_argument(file_path):
    """Load a file specified by the --file argument."""
    global current_file_path
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text.delete("1.0", tk.END)  
            text.insert("1.0", content)  
            current_file_path = file_path
            print(f"File loaded from argument: {current_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open the file provided as an argument: {e}")

def info():
    """Show an information dialog."""
    messagebox.showinfo("About Notepad", "Notepad by Diymka, ver 0.1")

# Parse command-line arguments
parser = argparse.ArgumentParser(description="A script that processes a file.")
parser.add_argument(
    "--file",
    type=str,
    help="Path to the file to open (optional)"
)

# Add the --info argument
parser.add_argument(
    "--info",
    action="store_true",  # Corrected here
    help="Show information about the script"
)
args = parser.parse_args()

# Handle the --info argument
if args.info:
    info()

# Initialize the Tkinter GUI
root = tk.Tk()
root.title("Notepad")
root.geometry("500x400")

# Text editor widget
text = tk.Text(root, font=("Arial", 15), wrap="word")
text.pack(padx=10, pady=10, expand=True, fill="both")

# Menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save", command=savefile)
file_menu.add_command(label="Open", command=openfile)

menu_bar.add_cascade(label="File", menu=file_menu)

# Additional menu
additional_bar = tk.Menu(menu_bar, tearoff=0)
additional_bar.add_command(label="About", command=info)

menu_bar.add_cascade(label="Additional", menu=additional_bar)

root.config(menu=menu_bar)

# Load file from argument if provided
if args.file:
    load_file_from_argument(args.file)

# Run the GUI loop
root.mainloop()
