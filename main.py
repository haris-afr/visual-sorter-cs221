import tkinter as tk
from tkinter import font
import customtkinter as ctk

#creating window
mainWindow = ctk.CTk()
mainWindow.title("DSA Visualizer")
mainWindow.geometry("600x400")

#creating list of algorithms
algorithm_array = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Count Sort", "Merge Sort", "Quick Sort", "Custom"]
info_array = ["Simplest algorithm, swaps adjacent elements", "Creates sorted list and sorts elements into their correct position", "Selects smallest element and swaps with first unsorted element",
              "Counts frequency of each element and sorts, only works with ints", "Uses recursion and merging", "Uses recursion and pivots", "create a custom function and test"]
selectedAlg = ctk.StringVar(value=algorithm_array[0])
global selectedInfo
selectedInfo= ctk.StringVar(value=info_array[0])


def updateInfo():
    print("hi")
    index = algorithm_array.index(selectedAlg.get())
    print(index)
    selectedInfo = ctk.StringVar(value=info_array[index])
    print(selectedInfo.get())

#loading fonts
ctk.FontManager.load_font("fonts/Courier_Prime/CourierPrime.ttf")
if ("Courier Prime" in font.families()):
    heading_font = ctk.CTkFont(family="Courier Prime", size=38)
    label_font = ctk.CTkFont(family="Courier Prime Bold", size=16)
    info_font = ctk.CTkFont(family="Courier Prime Bold", size=8)
else: #Fall back font
    heading_font = ctk.CTkFont(family="Courier New Bold", size=42)
    label_font = ctk.CTkFont(family="Courier New Bold", size=20)
    info_font = ctk.CTkFont(family="Courier New Bold", size=14)


#creating elements
headingLabel = ctk.CTkLabel(mainWindow, text="DSA Visualizer", font=heading_font)

algorithmFrame = ctk.CTkFrame(mainWindow, fg_color="transparent", )
algorithmSelectLabel = ctk.CTkLabel(algorithmFrame, text="Select Algorithm", font=label_font)

algorithmList = ctk.CTkComboBox(algorithmFrame, values=algorithm_array, variable=selectedAlg)
algorithmList.bind("<<ComboBoxSelected>>", updateInfo())

algorithmInfoLabel = ctk.CTkLabel(algorithmFrame, text=selectedInfo.get(), font=info_font)

arrayFrame = ctk.CTkFrame(mainWindow, fg_color="transparent")
arrayInputLabel = ctk.CTkLabel(arrayFrame, text="Input Array", font=label_font)

runButton = ctk.CTkButton(mainWindow, text='Run', command=updateInfo)

#displaying all of the elements
headingLabel.pack(pady="10px")

elementPadding = 10
algorithmSelectLabel.pack(side="left", padx=f"{elementPadding}px")
algorithmList.pack(side="left", padx=f"{elementPadding}px")
algorithmInfoLabel.pack(side="right", padx=f"{elementPadding}px", expand=True)
algorithmFrame.pack(pady="15px")

arrayInputLabel.pack(side="left")
arrayFrame.pack()


runButton.pack()


mainWindow.mainloop()