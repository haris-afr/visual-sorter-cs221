import tkinter as tk
from tkinter import font
import customtkinter as ctk

mainWindow = ctk.CTk()
mainWindow.title("DSA Visualizer")
mainWindow.geometry("600x400")

ctk.FontManager.load_font("fonts/Courier_Prime/CourierPrime.ttf")
if ("Courier Prime" in font.families()):
    heading_font = ctk.CTkFont(family="Courier Prime", size=38)
else: #Fall back font
    heading_font = ctk.CTkFont(family="Courier New Bold", size=42)


w = ctk.CTkLabel(mainWindow, text="DSA Visualizer", font=heading_font)
w.pack()

mainWindow.mainloop()