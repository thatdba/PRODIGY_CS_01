import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                alpha = ord('a')
            else:
                alpha = ord('A')
            result += chr((ord(char) - alpha + shift * mode) % 26 + alpha)
        else:
            result += char
    return result

def process_message():
    message = message_entry.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    mode = 1 if mode_var.get() == "Encrypt" else -1

    if mode == 1:
        result = caesar_cipher(message, shift, mode)
    else:
        result = caesar_cipher(message, shift, mode)

    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", result)

# Create a Tkinter window
root = tk.Tk()
root.title("Caesar Cipher Example by Masego")
#provide size to window
root.geometry("450x350")

# Create a message entry field
message_label = tk.Label(root, text="Enter Message:")
message_label.grid(row=0, column=0)
message_entry = tk.Text(root, height=5, width=30)
message_entry.grid(row=0, column=1, padx=10, pady=5)

# Create a shift entry field
shift_label = tk.Label(root, text="Enter Shift (0-25):")
shift_label.grid(row=1, column=0)
shift_entry = tk.Entry(root)
shift_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a mode selection (Encrypt/Decrypt)
mode_var = tk.StringVar()
mode_var.set("Encrypt")
encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt")
encrypt_radio.grid(row=2, column=0)
decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt")
decrypt_radio.grid(row=2, column=1)

# Create a process button
process_button = tk.Button(root, text="Process", command=process_message)
process_button.grid(row=3, columnspan=2, pady=10)

# Create an output text field
output_label = tk.Label(root, text="Output:")
output_label.grid(row=4, column=0, pady=5)
output_text = tk.Text(root, height=5, width=30)
output_text.grid(row=4, column=1, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
