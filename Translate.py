from tkinter import* 
import tkinter as tk
from tkinter.font import BOLD
import deepl as d
import pyautogui as gui
import pygetwindow as pgw
import os as os
from PIL import ImageGrab
import pytesseract as cv


cv.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' 
os.putenv('TESSDATA_PREFIX', 'C:\Program Files\Tesseract-OCR\tessdata')

auth_key = "AUTHORIZATION_KEY"
translator = d.Translator(auth_key)

Active_Window = pgw.getActiveWindow()




isActive = True




def Get_text():

    img = ImageGrab.grab(bbox=(int(Active_Window.left), int(Active_Window.top),int(Active_Window.right), int(Active_Window.bottom)))
    text = cv.image_to_string(img, lang="jpn")

    return text

def output():

    while(isActive):
        try:
            newtext = Get_text()
            result = translator.translate_text(newtext, target_lang="EN-US")
        finally:
            return result


def defwindow():
    window = Tk()
    window.title("Translator")

    window.configure(width=800, height=600)
    window.configure(bg='lightgray')
    window.geometry("800x600")

    
    
    T = Text(window, height=500, width=500)
    L = Label(window, text = "Translation")

    L.config(font = ("Arial", 20, BOLD))

    L.pack()
    T.pack()


    T.insert(tk.END, output())

   
    

    window.mainloop()
    
defwindow()
