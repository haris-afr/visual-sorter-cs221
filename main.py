
#<<<<<<<<<<<< HEAD
import tkinter as tk
from tkinter import font #for fonts
import customtkinter as ctk #main GUI library
from PIL import Image #for image 
import re #regex for checking array
from image_gen import * #import functions from other file
from custom_sort import *
from ast import literal_eval #convert string array into actual array

#This project requires the user to download the following libraries from pip
# pillow (used for image display)
# customtkinter (used for GUI)
# numpy (used for storing arrays)
# matplotlib (used for image generation & saving)

#The project should be loaded in VS Code, with the visual-sroter-221 folder opened

#creating window for CTK
mainWindow = ctk.CTk()
mainWindow.title("DSA Visualizer")
mainWindow.geometry("600x400")

#creating list of algorithms
algorithm_array = ["Bubble Sort", "Insertion Sort", "Selection Sort", "BST", "Count Sort",
                    "Merge Sort", "Quick Sort", "Custom"]
selectedAlg = ctk.StringVar()
textA = ""

#variable declaration and initialization
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
def changeToScene2(): #called when the run button gets called without error
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

def changeToScene1(): #called when the back button is pressed
    imageLabel.pack_forget()
    backBtn.pack_forget()
    prevBtn.pack_forget()
    nextBtn.pack_forget()
    buttonsFrame.pack_forget()

    headingLabel.pack(pady="10px")
    algorithmSelectLabel.pack(side="left", padx="10px")
    algorithmList.pack(side="left", padx="10px")
    algorithmFrame.pack(pady="15px")
    arrayInputLabel.pack(side="left")
    arrayTextBox.pack()
    arrayFrame.pack(pady='15px')
    runButton.pack()

def getText(textbox: ctk.CTkTextbox, errorLabel:ctk.CTkLabel): #used for getting and checking array input
    global textA
    textA = textbox.get('0.0', 'end')
    textA = re.findall("^\[\d+(?:,\s*\d+)*\]$", textA) # type: ignore
    if (textA.__len__() == 0):
        errorLabel.pack()
    else:
        errorLabel.pack_forget()
        changeToScene2()
        return textA

def loadImage(): #used everytime an image is loaded
    global currentImageIndex
    global imageVar
    global imageTKVar
    global imageLabel
    imageVar = Image.open(f"saved_figures/fig_{currentImageIndex}.png")
    imageTKVar.configure(light_image=imageVar, dark_image=imageVar, size=(400,350))
    print(currentImageIndex)

def nextFrame(): #used when the next button is pressed
    global currentImageIndex
    global totalImages

    if (currentImageIndex == (totalImages-1)): return
    currentImageIndex += 1
    loadImage()

def prevFrame(): #take a wild guess
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
        case "Insertion Sort":
            totalImages = insertion_sort(textA)
        case "Selection Sort":
            totalImages = selection_sort(textA)
        case "BST":
            totalImages = bst_sort(textA)
        case "Count Sort":
            pass
        case "Quick Sort":
            pass
        case "Merge Sort":
            totalImages = mergeSort_front(textA)
            pass
        case "Custom":
            totalImages = custom_sort(textA)
        case "":
            pass


#creating elements
headingLabel = ctk.CTkLabel(mainWindow, text="DSA Visualizer", font=heading_font)

algorithmFrame = ctk.CTkFrame(mainWindow, fg_color="transparent", )
algorithmSelectLabel = ctk.CTkLabel(algorithmFrame, text="Select Algorithm", font=label_font)
algorithmList = ctk.CTkComboBox(algorithmFrame, values=algorithm_array, variable=selectedAlg)

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
algorithmSelectLabel.pack(side="left", padx="10px")
algorithmList.pack(side="left", padx="10px")
algorithmFrame.pack(pady="15px")
arrayInputLabel.pack(side="left")
arrayTextBox.pack()
arrayFrame.pack(pady='15px')
runButton.pack()


mainWindow.mainloop()