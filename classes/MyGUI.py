from tkinter import *
from tkinterhtml import HtmlFrame
from tkinter import messagebox
from tkinter import font #to be able to underline label
import math

from classes.RAE import *

class MyGUI:

    def __init__(self,mywindow,titulo,size='850x860',icon='',bg='#CCCCCC'):
        # This method create a Window
        self.mywindow=mywindow
        self.titulo=titulo
        self.bg=bg
        self.icon=icon
        self.size=size
        self.mywindow.title(self.titulo)
        self.mywindow.resizable(False,True)
        self.mywindow.iconbitmap(self.icon)
        #self.mywindow.geometry(self.size)
        self.mywindow.config(bg=self.bg)

        self.miFrameLeft=Frame(self.mywindow,padx=10,pady=10,bg=self.bg,width=100, height=100)
        self.miFrameLeft.grid(row=0, column=0, sticky="nw")
 
        self.miFrameRight=Frame(self.mywindow,padx=10,pady=10,bg=self.bg)
        self.miFrameRight.grid(row=0, column=1, sticky="nsw")      


        self.createFrameHtml()

        txtLabel="Introduce una palabra: "
        posRow=0
        posColumn=0
        self.createLabel(self.miFrameLeft,txtLabel,posRow,posColumn)

        self.createInput()

        txtBoton="Definición"
        posRow=2
        posColumn=0
        method = self.clickDefinition
        self.createButon(txtBoton,posRow,posColumn,method)

        txtBoton="Obtén palabras\nque empiezan por..."
        posRow=1
        posColumn=1
        method = self.clickWordsStart
        self.createButon(txtBoton,posRow,posColumn,method)
        
        txtBoton="Obtén palabras\nque terminan en..."
        posRow=2
        posColumn=1
        method = self.clickWordsEnd
        self.createButon(txtBoton,posRow,posColumn,method)

        txtBoton="Obtén palabras\nque cotinen..."
        posRow=3
        posColumn=1
        method = self.clickWordsContent
        self.createButon(txtBoton,posRow,posColumn,method)


    def createFrameHtml(self):
        # This method create a Frame Html
        self.frameHtml = HtmlFrame(self.mywindow, horizontal_scrollbar="auto")
        self.frameHtml.grid(column=0, row=1,columnspan=2,sticky="nesw")

        #self.frameHtml.pack(fill="x",expand=True,anchor="s")

    def createLabel(self,frame,txtLabel,posRow,posColumn,swMethod=False):
        # This method create a Label
        self.wordLabel=Label(frame,text=txtLabel,bg=self.bg)
        self.wordLabel.grid(row=posRow,column=posColumn,sticky="w",padx=10)
        if swMethod:
            self.wordLabel.config(fg="blue",cursor="hand2")
            f = font.Font(self.wordLabel, self.wordLabel.cget("font"))
            f.configure(underline=True)
            self.wordLabel.configure(font=f)

            self.wordLabel.bind('<Button>', lambda x: self.clickLabelResult(txtLabel))
        


    def createInput(self):
        # This method create a Input
        self.wordInput=Entry(self.miFrameLeft,borderwidth=10,relief="flat",highlightcolor="white")
        self.wordInput.grid(row=1,column=0)
        self.wordInput.config(fg="blue",justify="left")

    def createButon(self,txtBoton,posRow,posColumn,method):
        # This method create a Buton
        butDefinition = Button(self.miFrameLeft, text=txtBoton,command=method)
        butDefinition.grid(row=posRow,column=posColumn,sticky="nswe",padx=10,pady=5)
        butDefinition.config(cursor="hand2")


    def clickDefinition(self,word=''):
        # This method is launched with the button "Definición"
        if not word:
            word = self.wordInput.get()
        if word:
            rae = RAE(word)
            result = rae.getDefinition()
            self.frameHtml.set_content(f"<html>{result}</html>")
        else:
            messagebox.showinfo(message="Debe introducir una palabra", title="Mensaje de información")
        

    def clickWordsStart(self):
        # This method is launched with the button "Obtén palabras\nque empiezan por..."
        word = self.wordInput.get()
        if word:
            rae = RAE(word)
            result = rae.getWordsStart()
            self.displayListWords(result)
        else:
            messagebox.showinfo(message="Debe introducir una palabra", title="Mensaje de información")


    def clickWordsEnd(self):
        # This method is launched with the button "Obtén palabras\nque terminan en..."        
        word = self.wordInput.get()
        if word:
            rae = RAE(word)
            result = rae.getWordsEnd()
            self.displayListWords(result)
        else:
            messagebox.showinfo(message="Debe introducir una palabra", title="Mensaje de información")

    def clickWordsContent(self):
        # This method is launched with the button "Obtén palabras\nque cotinen..."        
        word = self.wordInput.get()
        if word:
            rae = RAE(word)
            result = rae.getWordsContent()
            self.displayListWords(result)
        else:
            messagebox.showinfo(message="Debe introducir una palabra", title="Mensaje de información")

    def clickLabelResult(self,word):                       
        self.clickDefinition(word)

    def displayListWords(self,result):
        # This method display the list Words in columns        
        numColumn = 5 #Number of columns to display
        n=len(result) #Number of words found 
        if n>0:
            self.removeDisplayResult()
            numItemColumn=math.ceil(n/numColumn) #Number of item / column to display the result
            i=0
            posColumn=0
            for item in result:
                #print (str(item).decode('utf-8','ignore'))                 
                if(i>=numItemColumn):
                    posColumn+=1
                    i=0
                txtLabel=item
                posRow=i                
                nameMethod=True
                self.createLabel(self.miFrameRight,txtLabel,posRow,posColumn,nameMethod)            
                i+=1
        else:
            messagebox.showinfo(message="No hay resultados", title="Mensaje de información")

    def removeDisplayResult(self):
        # This method delete the displayed results
        list = self.miFrameRight.grid_slaves()
        for l in list:
            l.destroy()