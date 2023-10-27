import tkinter as tk
from tkinter import *

window = tk.Tk()

fontName = "Arial"


def dimensions():
    for widget in window.winfo_children():
        widget.destroy()

    window.columnconfigure(0, weight=1)  # Center-align the first column
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)

    greeting = tk.Label(
        text="Hello to AreaAce!",
        width=50,
        height=3,
        font=(fontName, 25)
    )
    greeting.grid(column=0, columnspan=2, row=0, padx=5, pady=5)

    chooseDimensions = tk.Label(
        text="Choose with which dimensions you want to work with:",
        font=(fontName, 15)
    )
    chooseDimensions.grid(column=0, columnspan=2, row=1, padx=5, pady=5)

    twoDButton = tk.Button(
        text="2D",
        width=15,
        height=6,
        activebackground="#EEEEEE",
        bd=5,
        bg="#FFFFFF",
        font=(fontName, 25, "bold"),
        command=lambda: chooseShape(2)
    )
    threeDButton = tk.Button(
        text="3D",
        width=15,
        height=6,
        activebackground="#EEEEEE",
        bd=5,
        bg="#FFFFFF",
        font=(fontName, 25, "bold"),
        command=lambda:chooseShape(3)
    )
    twoDButton.grid(column=0, row=2, padx=5, pady=5)
    threeDButton.grid(column=1, row=2, padx=5, pady=5)


def chooseShape(n):
    if n==2:
        for widget in window.winfo_children():
            widget.destroy()

        window.columnconfigure(0, weight=1)  # Center-align the first column
        window.columnconfigure(1, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=3)
        window.rowconfigure(2, weight=3)

        chooseShape = tk.Label(
            text="Choose the shape:",
            font=(fontName, 25)
        )
        chooseShape.grid(column=0, columnspan=2, row=0, padx=5, pady=5)

        frameTriangles = Frame(window, width=500, height=300, bg='#DDDDDD')
        frameTriangles.grid(column=0, row=1, padx=5, pady=5)

        frameTriangles.columnconfigure(0, weight=1)  # Center-align the first column
        frameTriangles.columnconfigure(1, weight=1)
        frameTriangles.rowconfigure(0, weight=1)
        frameTriangles.rowconfigure(1, weight=1)

        triangleButton = tk.Button(frameTriangles,
            text="Triangle",
            activebackground="#EEEEEE",
            bd=5,
            bg="#FFFFFF",
            font=(fontName, 20, "bold"),

        )
        rightTriangleButton = tk.Button(frameTriangles,
            text="Right Triangle",
            activebackground="#EEEEEE",
            bd=5,
            bg="#FFFFFF",
            font=(fontName, 20, "bold"),

        )
        isoTriangleButton = tk.Button(frameTriangles,
            text="Isosceles Triangle",
            activebackground="#EEEEEE",
            bd=5,
            bg="#FFFFFF",
            font=(fontName, 20, "bold"),

        )
        equaTriangleButton = tk.Button(frameTriangles,
            text="Equilateral Triangle",
            activebackground="#EEEEEE",
            bd=5,
            bg="#FFFFFF",
            font=(fontName, 20, "bold"),

        )

        triangleButton.grid(column=0, row=0, padx=5, pady=5)
        rightTriangleButton.grid(column=1, row=0, padx=5, pady=5)
        isoTriangleButton.grid(column=0, row=1, padx=5, pady=5)
        equaTriangleButton.grid(column=1, row=1, padx=5, pady=5)



        frameQuad = Frame(window, width=500, height=600, bg='#DDDDDD')
        frameQuad.grid(column=1, row=1, rowspan=2, padx=5, pady=5)

        frameCircles = Frame(window, width=500, height=300, bg='#DDDDDD')
        frameCircles.grid(column=0, row=2, padx=5, pady=5)

    elif n==3:
        print (n)


dimensions()
window.mainloop()
