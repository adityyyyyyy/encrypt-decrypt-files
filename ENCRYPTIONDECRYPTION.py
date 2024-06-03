import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
import os

# Encryption function for images, databases, Excel files, and videos
def operate(file_type,key, operation):
    file_types = {
        "Image": [("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")],
        "Excel": [("Excel files", "*.xls;*.xlsx")],
        "Video": [("Video files", "*.mp4;*.avi;*.mkv")],
        "PDF": [("PDF files", "*.pdf")]
    }

    file_path = filedialog.askopenfilename(filetypes=file_types[file_type])
    if not file_path:
        messagebox.showerror("Error", "No file selected")
        return

    try:
        # Read the file
        with open(file_path, 'rb') as file:
            data = bytearray(file.read())  # read file data into a bytearray for mutable operations

        # XOR operation
        for i in range(len(data)):
            data[i] ^= key

        # Write the modified data back to the same file
        with open(file_path, 'wb') as file:
            file.write(data)

        messagebox.showinfo("Success", f"{operation} operation completed successfully on the {file_type}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    root.title("encrypt/decrypt")
    root.geometry("500x300")
    root.resizable(False, False)
    root.configure(bg="#ececec")

    # Label setup
    label = tk.Label(root, text="Select File Type to Encrypt/Decrypt", font=('Arial', 16), bg="#ececec")
    label.pack(pady=10)

    # Dropdown menu setup
    file_types = ["Image", "Excel", "Video", "PDF"]
    selected_file_type = tk.StringVar(value=file_types[0])

    dropdown = ttk.Combobox(root, values=file_types, textvariable=selected_file_type, font=('Arial', 14))
    dropdown.pack(pady=10)

    # Buttons setup
    encrypt_button = tk.Button(root, text="Encrypt", command=lambda: get_key_and_operate(selected_file_type.get(), "Encrypt"), font=('Arial', 14), bg="#4caf50", fg="white")
    encrypt_button.pack(pady=10, fill=tk.X, padx=20)

    decrypt_button = tk.Button(root, text="Decrypt", command=lambda: get_key_and_operate(selected_file_type.get(), "Decrypt"), font=('Arial', 14), bg="#f44336", fg="white")
    decrypt_button.pack(pady=10, fill=tk.X, padx=20)

    # Progress bar
    progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
    progress.pack(pady=20)

    # Get key from user and perform operation
    def get_key_and_operate(file_type, operation):
        key = simpledialog.askinteger("Input", f"Enter the key (integer between 0 and 255) for {operation}:", minvalue=0, maxvalue=255)
        if key is not None:
            operate(file_type, key, operation)

    root.mainloop()

if __name__ == "__main__":
    main()


