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
    greeting.grid(column=0, columnspan=2, row=0, padx=15, pady=15)

    chooseDimensions = tk.Label(
        text="Choose with which dimensions you want to work with:",
        font=(fontName, 15)
    )
    chooseDimensions.grid(column=0, columnspan=2, row=1, padx=15, pady=15)

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
        command=lambda: chooseShape(3)
    )
    twoDButton.grid(column=0, row=2, padx=15, pady=15)
    threeDButton.grid(column=1, row=2, padx=15, pady=15)


def chooseShape(n):
    if n == 2:
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
        chooseShape.grid(column=0, columnspan=2, row=0, padx=15, pady=15)

        frameTriangles = Frame(window, width=500, height=300, bg='#DDDDDD')
        frameTriangles.grid(column=0, row=1, padx=15, pady=15)

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
                                   command=lambda: calcShape("triangle")
                                   )
        rightTriangleButton = tk.Button(frameTriangles,
                                        text="Right\nTriangle",
                                        activebackground="#EEEEEE",
                                        bd=5,
                                        bg="#FFFFFF",
                                        font=(fontName, 20, "bold"),

                                        )
        isoTriangleButton = tk.Button(frameTriangles,
                                      text="Isosceles\nTriangle",
                                      activebackground="#EEEEEE",
                                      bd=5,
                                      bg="#FFFFFF",
                                      font=(fontName, 20, "bold"),

                                      )
        equaTriangleButton = tk.Button(frameTriangles,
                                       text="Equilateral\nTriangle",
                                       activebackground="#EEEEEE",
                                       bd=5,
                                       bg="#FFFFFF",
                                       font=(fontName, 20, "bold"),

                                       )

        triangleButton.grid(column=0, row=0, padx=15, pady=15)
        rightTriangleButton.grid(column=1, row=0, padx=15, pady=15)
        isoTriangleButton.grid(column=0, row=1, padx=15, pady=15)
        equaTriangleButton.grid(column=1, row=1, padx=15, pady=15)

        frameQuad = Frame(window, width=500, height=600, bg='#DDDDDD')
        frameQuad.grid(column=1, row=1, rowspan=2, padx=15, pady=15)

        frameQuad.columnconfigure(0, weight=1)  # Center-align the first column
        frameQuad.columnconfigure(1, weight=1)
        frameQuad.rowconfigure(0, weight=1)
        frameQuad.rowconfigure(1, weight=1)
        frameQuad.rowconfigure(2, weight=1)
        frameQuad.rowconfigure(3, weight=1)

        photo = PhotoImage(file=r"C:\Users\Atrur\Desktop\AreaAce\tri.png")
        photoimage = photo.subsample(10, 10)

        squareButton = tk.Button(frameQuad,
                                 text="Square",
                                 image=photoimage,
                                 compound=BOTTOM,
                                 anchor=NW,
                                 activebackground="#EEEEEE",
                                 bd=5,
                                 bg="#FFFFFF",
                                 font=(fontName, 20, "bold"),
                                 )
        squareButton.image = photoimage
        rectangleButton = tk.Button(frameQuad,
                                    text="Rectangle",
                                    activebackground="#EEEEEE",
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 20, "bold"),
                                    )
        rhombusButton = tk.Button(frameQuad,
                                  text="Rhombus",
                                  activebackground="#EEEEEE",
                                  bd=5,
                                  bg="#FFFFFF",
                                  font=(fontName, 20, "bold"),
                                  )
        parallelogramButton = tk.Button(frameQuad,
                                        text="Parallelogram",
                                        activebackground="#EEEEEE",
                                        bd=5,
                                        bg="#FFFFFF",
                                        font=(fontName, 20, "bold"),
                                        )
        trapezoidButton = tk.Button(frameQuad,
                                    text="Trapezoid",
                                    activebackground="#EEEEEE",
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 20, "bold"),
                                    )
        rightTrapezoidButton = tk.Button(frameQuad,
                                         text="Right\nTrapezoid",
                                         activebackground="#EEEEEE",
                                         bd=5,
                                         bg="#FFFFFF",
                                         font=(fontName, 20, "bold"),
                                         )
        isoTrapezoidButton = tk.Button(frameQuad,
                                       text="Isosceles\nTrapezoid",
                                       activebackground="#EEEEEE",
                                       bd=5,
                                       bg="#FFFFFF",
                                       font=(fontName, 20, "bold"),
                                       )
        kiteButton = tk.Button(frameQuad,
                               text="Kite",
                               activebackground="#EEEEEE",
                               bd=5,
                               bg="#FFFFFF",
                               font=(fontName, 20, "bold"),
                               )

        squareButton.grid(column=0, row=0, padx=15, pady=15)
        rectangleButton.grid(column=1, row=0, padx=15, pady=15)
        rhombusButton.grid(column=0, row=1, padx=15, pady=15)
        parallelogramButton.grid(column=1, row=1, padx=15, pady=15)
        trapezoidButton.grid(column=0, row=2, padx=15, pady=15)
        rightTrapezoidButton.grid(column=1, row=2, padx=15, pady=15)
        isoTrapezoidButton.grid(column=0, row=3, padx=15, pady=15)
        kiteButton.grid(column=1, row=3, padx=15, pady=15)

        frameCircles = Frame(window, width=500, height=300, bg='#DDDDDD')
        frameCircles.grid(column=0, row=2, padx=15, pady=15)

        frameCircles.columnconfigure(0, weight=1)
        frameCircles.rowconfigure(0, weight=1)
        frameCircles.rowconfigure(1, weight=1)

        circleButton = tk.Button(frameCircles,
                                 text="Circle",
                                 activebackground="#EEEEEE",
                                 bd=5,
                                 bg="#FFFFFF",
                                 font=(fontName, 20, "bold"),
                                 )
        elipseButton = tk.Button(frameCircles,
                                 text="Elipse",
                                 activebackground="#EEEEEE",
                                 bd=5,
                                 bg="#FFFFFF",
                                 font=(fontName, 20, "bold"),
                                 )

        circleButton.grid(column=0, row=0, padx=15, pady=15)
        elipseButton.grid(column=0, row=1, padx=15, pady=15)

    elif n == 3:
        print(n)


def calcShape(shape):
    for widget in window.winfo_children():
        widget.destroy()
    if shape == "triangle":
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=1)

        frameTriangleDiagram = Frame(window, width=500, height=300, bg='#DDDDDD')
        frameSides = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameSides.columnconfigure(0, weight=1)
        frameSides.columnconfigure(1, weight=1)
        frameSides.rowconfigure(0, weight=1)
        frameSides.rowconfigure(1, weight=1)
        frameSides.rowconfigure(2, weight=1)

        frameHeight = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameHeight.columnconfigure(0, weight=1)
        frameHeight.columnconfigure(1, weight=1)
        frameHeight.rowconfigure(0, weight=1)
        frameHeight.rowconfigure(1, weight=1)
        frameHeight.rowconfigure(2, weight=1)

        frameAreas = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAreas.columnconfigure(0, weight=1)
        frameAreas.columnconfigure(1, weight=1)
        frameAreas.rowconfigure(0, weight=1)
        frameAreas.rowconfigure(1, weight=1)

        frameAngles = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameTriangleDiagram.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
        frameSides.grid(column=0, row=1, padx=15, pady=15)
        frameHeight.grid(column=1, row=1, padx=15, pady=15)
        frameAreas.grid(column=0, row=2, padx=15, pady=15)
        frameAngles.grid(column=1, row=2, padx=15, pady=15)

        def calculatetest():
            print(int(firstSideInput.get())*int(firstHeightInput.get())/2)

        buttonTest = tk.Button (frameTriangleDiagram,
            text="Calculate the area",
            font=(fontName, 15),
            command=lambda:calculatetest()

        )
        buttonTest.grid()

        firstSideLabel = tk.Label(frameSides,
                                  text="Side a: ",
                                  bd=5,
                                  bg='#DDDDDD',
                                  font=(fontName, 15),
                                  )
        firstSideInput = tk.Entry(frameSides,
                                  bd=5,
                                  bg="#FFFFFF",
                                  font=(fontName, 15),
                                  )

        secondSideLabel = tk.Label(frameSides,
                                   text="Side b: ",
                                   bd=5,
                                   bg='#DDDDDD',
                                   font=(fontName, 15),
                                   )
        secondSideInput = tk.Entry(frameSides,
                                   bd=5,
                                   bg="#FFFFFF",
                                   font=(fontName, 15),
                                   )

        thirdSideLabel = tk.Label(frameSides,
                                  text="Side c: ",
                                  bd=5,
                                  bg='#DDDDDD',
                                  font=(fontName, 15),
                                  )
        thirdSideInput = tk.Entry(frameSides,
                                  bd=5,
                                  bg="#FFFFFF",
                                  font=(fontName, 15),
                                  )

        firstSideLabel.grid(column=0, row=0, pady=15)
        firstSideInput.grid(column=1, row=0, padx=5, pady=15)
        secondSideLabel.grid(column=0, row=1, pady=15)
        secondSideInput.grid(column=1, row=1, padx=5, pady=15)
        thirdSideLabel.grid(column=0, row=2, pady=15)
        thirdSideInput.grid(column=1, row=2, padx=5, pady=15)

        firstHeightLabel = tk.Label(frameHeight,
                                  text="Height a: ",
                                  bd=5,
                                  bg='#DDDDDD',
                                  font=(fontName, 15),
                                  )
        firstHeightInput = tk.Entry(frameHeight,
                                  bd=5,
                                  bg="#FFFFFF",
                                  font=(fontName, 15),
                                  )

        secondHeightLabel = tk.Label(frameHeight,
                                   text="Height b: ",
                                   bd=5,
                                   bg='#DDDDDD',
                                   font=(fontName, 15),
                                   )
        secondHeightInput = tk.Entry(frameHeight,
                                   bd=5,
                                   bg="#FFFFFF",
                                   font=(fontName, 15),
                                   )

        thirdHeightLabel = tk.Label(frameHeight,
                                  text="Height c: ",
                                  bd=5,
                                  bg='#DDDDDD',
                                  font=(fontName, 15),
                                  )
        thirdHeightInput = tk.Entry(frameHeight,
                                  bd=5,
                                  bg="#FFFFFF",
                                  font=(fontName, 15),
                                  )

        firstHeightLabel.grid(column=0, row=0, pady=15)
        firstHeightInput.grid(column=1, row=0, padx=5, pady=15)
        secondHeightLabel.grid(column=0, row=1, pady=15)
        secondHeightInput.grid(column=1, row=1, padx=5, pady=15)
        thirdHeightLabel.grid(column=0, row=2, pady=15)
        thirdHeightInput.grid(column=1, row=2, padx=5, pady=15)

        areaLabel = tk.Label(frameAreas,
                                   text="Area: ",
                                   bd=5,
                                   bg='#DDDDDD',
                                   font=(fontName, 15),
                                   )
        areaInput = tk.Entry(frameAreas,
                                   bd=5,
                                   bg="#FFFFFF",
                                   font=(fontName, 15),
                                   )

        perimeterLabel = tk.Label(frameAreas,
                                  text="Perimeter: ",
                                  bd=5,
                                  bg='#DDDDDD',
                                  font=(fontName, 15),
                                  )
        perimeterInput = tk.Entry(frameAreas,
                                  bd=5,
                                  bg="#FFFFFF",
                                  font=(fontName, 15),
                                  )

        areaLabel.grid(column=0, row=0, pady=15)
        areaInput.grid(column=1, row=0, padx=5, pady=15)
        perimeterLabel.grid(column=0, row=1, pady=15)
        perimeterInput.grid(column=1, row=1, padx=5, pady=15)





dimensions()
window.mainloop()
