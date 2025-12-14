import tkinter as tk
from tkinter import font
import customtkinter as ctk

mainWindow = ctk.CTk()
mainWindow.title("DSA Visualizer")
mainWindow.geometry("600x400")

ctk.FontManager.load_font("fonts/Courier_Prime/CourierPrime.ttf")
if ("Courier Prime" in font.families()):
    heading_font = ctk.CTkFont(family="Courier Prime", size=38)
    label_font = ctk.CTkFont(family="Courier Prime Bold", size=16)
else: #Fall back font
    heading_font = ctk.CTkFont(family="Courier New Bold", size=42)
    heading_font = ctk.CTkFont(family="Courier New Bold", size=20)


headingLabel = ctk.CTkLabel(mainWindow, text="DSA Visualizer", font=heading_font)

algorithmFrame = ctk.CTkFrame(mainWindow, fg_color="transparent")
selectAlgorithmLabel = ctk.CTkLabel(algorithmFrame, text="Select Algorithm", font=label_font)

arrayFrame = ctk.CTkFrame(mainWindow, fg_color="transparent")
inputArrayLabel = ctk.CTkLabel(arrayFrame, text="Input Array", font=label_font)

runButton = ctk.CTkButton(mainWindow, text='Run')

headingLabel.pack(pady="10px")
algorithmFrame.pack()
selectAlgorithmLabel.pack()
arrayFrame.pack()
inputArrayLabel.pack()
runButton.pack()

mainWindow.mainloop()