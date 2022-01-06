import os
import tkinter as tk
from tkinter import filedialog


def file_opener():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


def file_info(file_path):
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)
    file_name = "name" + file_name
    file_dic = {"file_name": file_name, "file_size": file_size}
    return file_dic


def file_self(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return data


def file():
    file_path = file_opener()
    file_dic = file_info(file_path)
    data = file_self(file_path)
    return file_dic, data
