import random
import string
import tkinter as tk

def passGen():
    try:
        passlen = int(entry.get())
        if passlen < 1:
            label.config(text="Please enter a positive number")
            return
    except ValueError:
        label.config(text="Please enter a valid number")
        return

    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    password = "".join(s[:passlen])

    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, password)
    label.config(text="Generated Password:")

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_label = tk.Label(frame, text="Enter password length:")
entry_label.pack()

entry = tk.Entry(frame)
entry.pack(pady=5)

button = tk.Button(frame, text="Generate Password", command=passGen)
button.pack(pady=5)

label = tk.Label(frame, text="Generated Password: ")
label.pack(pady=5)

text_box = tk.Text(frame, height=1, width=30)
text_box.pack(pady=5)

quit_button = tk.Button(frame, text="Quit", command=root.quit)
quit_button.pack(pady=5)

root.mainloop()
