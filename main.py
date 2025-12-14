import tkinter as tk
from tkinter import font
import customtkinter as ctk

#creating window
mainWindow = ctk.CTk()
mainWindow.title("DSA Visualizer")
mainWindow.geometry("600x400")

#creating list of algorithms
algorithm_array = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Count Sort", "Merge Sort", "Quick Sort", "Custom"]
log_array = ["n2", "n2", "n2", "n + m", "n log n", "n log n", "?"]
info_array = ["Simplest algorithm, swaps adjacent elements", "creates sorted list and sorts elements into their correct position", "selects smallest element and swaps with first unsorted element",
              "counts frequency of each element and sorts, only works with ints", "uses recursion and merging", "uses recursion and pivots", "create a custom function and test"]
selectedAlg = algorithm_array[0]
selectedLog = log_array[0]
selectedInfo= info_array[0]

def updateLogInfo():
    print("hi")
    index = algorithm_array.index(selectedAlg)
    global selectedInfo
    global selectedLog
    selectedLog = log_array[index]
    selectedInfo= info_array[index]
    print(selectedLog)

#loading fonts
ctk.FontManager.load_font("fonts/Courier_Prime/CourierPrime.ttf")
if ("Courier Prime" in font.families()):
    heading_font = ctk.CTkFont(family="Courier Prime", size=38)
    label_font = ctk.CTkFont(family="Courier Prime Bold", size=16)
    info_font = ctk.CTkFont(family="Courier Prime Bold", size=12)
else: #Fall back font
    heading_font = ctk.CTkFont(family="Courier New Bold", size=42)
    label_font = ctk.CTkFont(family="Courier New Bold", size=20)
    info_font = ctk.CTkFont(family="Courier New Bold", size=14)


#creating elements
headingLabel = ctk.CTkLabel(mainWindow, text="DSA Visualizer", font=heading_font)

algorithmFrame = ctk.CTkFrame(mainWindow, fg_color="transparent", )
algorithmLogLable = ctk.CTkLabel(algorithmFrame, text=f"Log of O({selectedLog})", font=info_font)
algorithmSelectLabel = ctk.CTkLabel(algorithmFrame, text="Select Algorithm", font=label_font)
algorithmList = ctk.CTkComboBox(algorithmFrame, values=algorithm_array, variable=selectedAlg, command=updateLogInfo())
algorithmInfoLabel = ctk.CTkLabel(algorithmFrame, text=selectedInfo, font=info_font)

arrayFrame = ctk.CTkFrame(mainWindow, fg_color="transparent")
arrayInputLabel = ctk.CTkLabel(arrayFrame, text="Input Array", font=label_font)

runButton = ctk.CTkButton(mainWindow, text='Run')

#displaying all of the elements
headingLabel.pack(pady="10px")

elementPadding = 10
algorithmLogLable.pack(side="left", padx=f"{elementPadding}px")
algorithmSelectLabel.pack(side="left", padx=f"{elementPadding}px")
algorithmList.pack(side="left", padx=f"{elementPadding}px")
algorithmInfoLabel.pack(side="right", padx=f"{elementPadding}px", expand=True)
algorithmFrame.pack(pady="15px")

arrayInputLabel.pack(side="left")
arrayFrame.pack()


runButton.pack()

mainWindow.mainloop()