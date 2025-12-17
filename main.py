import tkinter as tk
from tkinter import font
<<<<<<< HEAD
import customtkinter as ctk
from PIL import Image
import re #regex
from image_gen import *
from custom_sort import *
from ast import literal_eval
=======
import customtkinter as ctk #main GUI library
from PIL import Image #for image 
from image_gen import * #import functions from other file
import re #regex for checking array
from ast import literal_eval #convert string array into actual array
>>>>>>> 62115fc9273deea5fa232cf573e72656446d9fb0

#creating window
mainWindow = ctk.CTk()
mainWindow.title("DSA Visualizer")
mainWindow.geometry("600x400")

#creating list of algorithms
algorithm_array = ["Bubble Sort", "Insertion Sort", "Selection Sort", "BST", "Count Sort",
                    "Merge Sort", "Quick Sort", "Custom"]
selectedAlg = ctk.StringVar()
textA = ""

global currentImageIndex
global totalImages
global imageVar
global imageTKVar
currentImageIndex = 0
totalImages = 10
imageVar = Image.open(f"saved_figures/fig_eg.png")
imageTKVar = ctk.CTkImage(light_image=imageVar, dark_image=imageVar, size=(400,350))
imageLabel = ctk.CTkLabel(mainWindow, image=imageTKVar, text="")

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

    chooseAlgorithm()
    loadImage()

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
    textA = re.findall("^\[\d+(?:,\s*\d+)*\]$", textA) # type: ignore
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

    if (currentImageIndex == (totalImages-1)): return
    currentImageIndex += 1
    loadImage()

def prevFrame():
    global currentImageIndex
    if (currentImageIndex <= 0): return
    currentImageIndex -= 1
    loadImage()

def chooseAlgorithm():
    global textA
    global totalImages
    textA = textA[0]
    textA = literal_eval(textA)
    match(selectedAlg.get()):
        case "Bubble Sort":
            totalImages = bubble_sort(textA)
            print(totalImages)
        case "Insertion Sort":
            totalImages = insertion_sort(textA)
            print(totalImages)
        case "Selection Sort":
            totalImages = selection_sort(textA)
            print(totalImages)
        case "BST":
            totalImages = bst_sort(textA)
            print(totalImages)
        case "Count Sort":
            pass
        case "Quick Sort":
            pass
        case "Merge Sort":
            totalImages = mergeSort_front(textA)
            print(totalImages)
            pass
        case "Custom":
            totalImages = custom_sort(textA)
            pass
        case "":
            pass


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

buttonsFrame = ctk.CTkFrame(mainWindow, fg_color="transparent")
prevBtn = ctk.CTkButton(buttonsFrame, text="<", command=lambda: prevFrame())
nextBtn = ctk.CTkButton(buttonsFrame, text=">", command=lambda: nextFrame())
backBtn = ctk.CTkButton(buttonsFrame, text="Go Back", command=lambda: changeToScene1())


#displaying all of the elements
headingLabel.pack(pady="10px")

elementPadding = 10
algorithmSelectLabel.pack(side="left", padx=f"{elementPadding}px")
algorithmList.pack(side="left", padx=f"{elementPadding}px")
algorithmFrame.pack(pady="15px")

arrayInputLabel.pack(side="left")
arrayTextBox.pack()
arrayFrame.pack(pady='15px')

runButton.pack()


mainWindow.mainloop()