import tkinter as tk
from tkinter import filedialog
import typing

def Select_File():
    root = tk.Tk()
    root.withdraw()

    file_path: str = filedialog.askopenfilename()

    return file_path


def Select_Folder():
    root = tk.Tk()
    root.withdraw()

    folder_path: str = filedialog.askdirectory()
    return folder_path