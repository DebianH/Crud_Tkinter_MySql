from tkinter import *
from window import Ventana

def main():
    root = Tk()
    root.wm_title("Productos App MySql")
    app = Ventana(root)
    app.mainloop()


if __name__ == '__main__':
    main()