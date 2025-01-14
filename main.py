import tkinter as tk
import random
import string

def Create_Name ():
    
    result = ""
    key = ""

    uppercase_consonants = ''.join(c for c in string.ascii_uppercase if c not in 'AEIOU')
    uppercase_vowels = 'AEIOU'
    lowercase_consonants = ''.join(c for c in string.ascii_lowercase if c not in 'aeiou')
    lowercase_vowels = 'aeiou'

    pattern_mapping = {
    'C': uppercase_consonants,
    'V': uppercase_vowels,
    'c': lowercase_consonants,
    'v': lowercase_vowels
    }

    key = keyEntry.get()

    result = ''.join(random.choice(pattern_mapping[char]) for char in key)
    resultLabel.config(text= result)
    
root = tk.Tk()
root.title("Random Name Generator")
root.geometry("250x100")

keyLabel = tk.Label(root, text = "Name Key")
keyEntry = tk.Entry(root)

submitButton = tk.Button(root, text="Submit", command = Create_Name)

resultLabel = tk.Label(root, text="Name will appear here!")

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

keyLabel.grid(row=0, column=0, padx=10,pady=5, sticky="nesw")
keyEntry.grid(row=0, column=1, padx=10,pady=5, sticky="nesw")
submitButton.grid(row=1, column=0, columnspan=2, padx=10,pady=5, sticky="nesw")
resultLabel.grid(row=2, column=0,columnspan=2, padx=10,pady=5, sticky="nesw")

root.mainloop()