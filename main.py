import tkinter as tk
from tkinter import font
import customtkinter as ctk
from PIL import Image, ImageTk
import re #regex

#creating window
mainWindow = ctk.CTk()
mainWindow.title("DSA Visualizer")
mainWindow.geometry("600x400")

#creating list of algorithms
algorithm_array = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Count Sort",
                    "Merge Sort", "Quick Sort", "Custom"]
selectedAlg = ctk.StringVar()
textA = ""

global currentImageIndex
global totalImages
global imageVar
global imageTKVar
currentImageIndex = 0
totalImages = 19 # CHANGE
imageVar = Image.open(f"saved_figures/fig_{currentImageIndex}.png")
imageTKVar = ctk.CTkImage(light_image=imageVar, dark_image=imageVar, size=(400,350))

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

#declaring functions
def changeToScene2():
    headingLabel.pack_forget()
    algorithmSelectLabel.pack_forget()
    algorithmList.pack_forget()
    algorithmFrame.pack_forget()
    arrayInputLabel.pack_forget()
    arrayTextBox.pack_forget()
    arrayFrame.pack_forget()
    runButton.pack_forget()

    imageLabel.pack()
    backBtn.pack(side="left")
    prevBtn.pack(side="left")
    nextBtn.pack(side="left")
    buttonsFrame.pack()

def changeToScene1():
    imageLabel.pack_forget()
    backBtn.pack_forget()
    prevBtn.pack_forget()
    nextBtn.pack_forget()
    buttonsFrame.pack_forget()

    headingLabel.pack(pady="10px")
    elementPadding = 10
    algorithmSelectLabel.pack(side="left", padx=f"{elementPadding}px")
    algorithmList.pack(side="left", padx=f"{elementPadding}px")
    algorithmFrame.pack(pady="15px")
    arrayInputLabel.pack(side="left")
    arrayTextBox.pack()
    arrayFrame.pack(pady='15px')
    runButton.pack()

def getText(textbox: ctk.CTkTextbox, errorLabel:ctk.CTkLabel):
    global textA
    textA = textbox.get('0.0', 'end')
    textA = re.findall("^\[\d+(?:,\s*\d+)*\]$", textA)
    if (textA.__len__() == 0):
        errorLabel.pack()
    else:
        errorLabel.pack_forget()
        changeToScene2()
        return textA

def loadImage():
    global currentImageIndex
    global imageVar
    global imageTKVar
    global imageLabel
    imageVar = Image.open(f"saved_figures/fig_{currentImageIndex}.png")
    imageTKVar.configure(light_image=imageVar, dark_image=imageVar, size=(400,350))
    print(currentImageIndex)


def nextFrame():
    global currentImageIndex
    global totalImages

    if (currentImageIndex == totalImages): return
    currentImageIndex += 1
    loadImage()

def prevFrame():
    global currentImageIndex
    if (currentImageIndex <= 0): return
    currentImageIndex -= 1
    loadImage()

#creating elements
headingLabel = ctk.CTkLabel(mainWindow, text="DSA Visualizer", font=heading_font)

algorithmFrame = ctk.CTkFrame(mainWindow, fg_color="transparent", )
algorithmSelectLabel = ctk.CTkLabel(algorithmFrame, text="Select Algorithm", font=label_font)
algorithmList = ctk.CTkComboBox(algorithmFrame, values=algorithm_array, variable=selectedAlg, 
                                command=lambda event: print(selectedAlg.get()))

arrayFrame = ctk.CTkFrame(mainWindow, fg_color="transparent")
arrayInputLabel = ctk.CTkLabel(arrayFrame, text="Input Array", font=label_font)
arrayTextBox = ctk.CTkTextbox(arrayFrame, height = 100)

errorLabel = ctk.CTkLabel(mainWindow, text="Error! Incorrect Array!", font=label_font)

runButton = ctk.CTkButton(mainWindow, text='Run', command=lambda: getText(arrayTextBox, errorLabel))

#creating elements for scene 2
#image
imageLabel = ctk.CTkLabel(mainWindow, image=imageTKVar, text="")
buttonsFrame = ctk.CTkFrame(mainWindow, fg_color="transparent")
prevBtn = ctk.CTkButton(buttonsFrame, text="<", command=lambda: prevFrame())
nextBtn = ctk.CTkButton(buttonsFrame, text=">", command=lambda: nextFrame())
backBtn = ctk.CTkButton(buttonsFrame, text="Go Back", command=lambda: changeToScene1())


#displaying all of the elements
imageLabel.pack()
backBtn.pack(side="left")
prevBtn.pack(side="left")
nextBtn.pack(side="left")
buttonsFrame.pack()

# headingLabel.pack(pady="10px")

# elementPadding = 10
# algorithmSelectLabel.pack(side="left", padx=f"{elementPadding}px")
# algorithmList.pack(side="left", padx=f"{elementPadding}px")
# algorithmFrame.pack(pady="15px")

# arrayInputLabel.pack(side="left")
# arrayTextBox.pack()
# arrayFrame.pack(pady='15px')

# runButton.pack()




#Sorting Algorithms 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            #Add screenshot here
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            #Add screenshot here
    #Final screenshot here


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=-1 and key < arr[j]:
            arr[j+1] = arr[j]
            #Add screenshot here
            j-=1
        arr[j+1] = key
        #Add screenshot here
    #Final screenshot here
   

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            #Add screenshot here
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
        #Add screenshot here
    #Final screenshot here
   
def start_Algo():
    inputArr = [int(x) for x in arrayInputLabel.get().split(',')]
    algorithm = selectedAlg.get()

    if algorithm == "Bubble Sort":
        bubble_sort(inputArr)

    elif algorithm == "Insertion Sort":
        insertion_sort(inputArr)

    elif algorithm == "Selection Sort":
        selection_sort(inputArr)


mainWindow.mainloop()