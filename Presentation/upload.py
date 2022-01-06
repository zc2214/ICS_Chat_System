
import os
import tkinter as tk
from tkinter import filedialog


def file_opener():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path