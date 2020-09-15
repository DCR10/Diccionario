from classes.MyGUI import *

def main():
    MyWindow=Tk()
    titleWindow='Mi Diccionario'
    size='850x860'
    myWindow = MyGUI(MyWindow,titleWindow,size)
    MyWindow.mainloop() 


main()