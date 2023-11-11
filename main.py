import tkinter as tk
from tkinter import *
from tkinter import messagebox
import math

from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

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
                                        command=lambda: calcShape("rightTriangle")
                                        )
        isoTriangleButton = tk.Button(frameTriangles,
                                      text="Isosceles\nTriangle",
                                      activebackground="#EEEEEE",
                                      bd=5,
                                      bg="#FFFFFF",
                                      font=(fontName, 20, "bold"),
                                      command=lambda: calcShape("isoTriangle")
                                      )
        equaTriangleButton = tk.Button(frameTriangles,
                                       text="Equilateral\nTriangle",
                                       activebackground="#EEEEEE",
                                       bd=5,
                                       bg="#FFFFFF",
                                       font=(fontName, 20, "bold"),
                                       command=lambda: calcShape("equTriangle")
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
                                 command=lambda: calcShape("square")
                                 )
        squareButton.image = photoimage
        rectangleButton = tk.Button(frameQuad,
                                    text="Rectangle",
                                    activebackground="#EEEEEE",
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 20, "bold"),
                                    command=lambda: calcShape("rectangle")
                                    )
        rhombusButton = tk.Button(frameQuad,
                                  text="Rhombus",
                                  activebackground="#EEEEEE",
                                  bd=5,
                                  bg="#FFFFFF",
                                  font=(fontName, 20, "bold"),
                                  command=lambda: calcShape("rhombus")
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

        squareButton.grid(column=0, row=0, padx=15, pady=15)
        rectangleButton.grid(column=1, row=0, padx=15, pady=15)
        rhombusButton.grid(column=0, row=1, padx=15, pady=15)
        rightTrapezoidButton.grid(column=1, row=1, padx=15, pady=15)
        isoTrapezoidButton.grid(column=0, columnspan = 2, row=2, padx=15, pady=15)

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
        return 0


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

        frameTriangleDiagram.columnconfigure(0, weight=1)
        frameTriangleDiagram.columnconfigure(1, weight=1)
        frameTriangleDiagram.rowconfigure(0, weight=1)
        frameTriangleDiagram.rowconfigure(1, weight=1)

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

        frameAngles.columnconfigure(0, weight=1)
        frameAngles.columnconfigure(1, weight=1)
        frameAngles.rowconfigure(0, weight=1)
        frameAngles.rowconfigure(1, weight=1)
        frameAngles.rowconfigure(2, weight=1)

        frameTriangleDiagram.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
        frameSides.grid(column=0, row=1, padx=15, pady=15)
        frameHeight.grid(column=1, row=1, padx=15, pady=15)
        frameAreas.grid(column=0, row=2, padx=15, pady=15)
        frameAngles.grid(column=1, row=2, padx=15, pady=15)

        def warningWithDelete(a = "There couldn't exist a triangle with dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        def diagramWindow(a, b, h2):
            top = Toplevel()
            top.title('Shape diagram')

            xPlot = math.sqrt(a ** 2 - h2 ** 2)
            polygon1 = Polygon([(0, 0), (b, 0), (xPlot, h2)])

            fig, ax = plt.subplots(1, 1)

            ax.add_patch(polygon1)

            plt.ylim(0, h2)
            plt.xlim(0, b)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)  # Use grid manager for the canvas

        def threeSidesCalc(a, b, c):
            if a + b > c and a + c > b and b + c > a:
                p = a + b + c
                halfP = p / 2

                firstSideInput.delete(0, tk.END)
                secondSideInput.delete(0, tk.END)
                thirdSideInput.delete(0, tk.END)

                firstSideInput.insert(0, str(a))
                secondSideInput.insert(0, str(b))
                thirdSideInput.insert(0, str(c))

                perimeterInput.delete(0, tk.END)
                perimeterInput.insert(0, str(p))

                s = math.sqrt(halfP * (halfP - a) * (halfP - b) * (halfP - c))
                areaInput.delete(0, tk.END)
                areaInput.insert(0, str(s))

                h1 = s * 2 / a
                h2 = s * 2 / b
                h3 = s * 2 / c

                firstHeightInput.delete(0, tk.END)
                secondHeightInput.delete(0, tk.END)
                thirdHeightInput.delete(0, tk.END)

                firstHeightInput.insert(0, str(h1))
                secondHeightInput.insert(0, str(h2))
                thirdHeightInput.insert(0, str(h3))

                alphaInput.configure(state="normal")
                betaInput.configure(state="normal")
                gammaInput.configure(state="normal")

                alphaInput.delete(0, tk.END)
                betaInput.delete(0, tk.END)
                gammaInput.delete(0, tk.END)

                alpha = math.acos(((b ** 2) + (c ** 2) - (a ** 2)) / (2 * b * c)) * (180.0 / math.pi)
                beta = math.acos(((a ** 2) + (c ** 2) - (b ** 2)) / (2 * a * c)) * (180.0 / math.pi)
                gamma = math.acos(((a ** 2) + (b ** 2) - (c ** 2)) / (2 * b * a)) * (180.0 / math.pi)

                alphaInput.insert(0, str(alpha))
                betaInput.insert(0, str(beta))
                gammaInput.insert(0, str(gamma))

                alphaInput.configure(state="disabled")
                betaInput.configure(state="disabled")
                gammaInput.configure(state="disabled")
                diagramWindow(a, b, h2)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateTriangle():
            value = checkEnoughInformation()
            aVal = firstSideInput.get()
            if aVal != "":
                a = float(firstSideInput.get())
            bVal = secondSideInput.get()
            if bVal != "":
                b = float(secondSideInput.get())
            cVal = thirdSideInput.get()
            if cVal != "":
                c = float(thirdSideInput.get())
            h1Val = firstHeightInput.get()
            if h1Val != "":
                h1 = float(firstHeightInput.get())
            h2Val = secondHeightInput.get()
            if h2Val != "":
                h2 = float(secondHeightInput.get())
            h3Val = thirdHeightInput.get()
            if h3Val != "":
                h3 = float(thirdHeightInput.get())
            sVal = areaInput.get()
            if sVal != "":
                s = float(areaInput.get())
            pVal = perimeterInput.get()
            if pVal != "":
                p = float(perimeterInput.get())

            if value == 1:
                try:
                    threeSidesCalc(a, b, c)
                except:
                    perimeterInput.delete(0, tk.END)
                    areaInput.delete(0, tk.END)
                    firstHeightInput.delete(0, tk.END)
                    secondHeightInput.delete(0, tk.END)
                    thirdHeightInput.delete(0, tk.END)

                    alphaInput.configure(state="normal")
                    betaInput.configure(state="normal")
                    gammaInput.configure(state="normal")
                    alphaInput.delete(0, tk.END)
                    betaInput.delete(0, tk.END)
                    gammaInput.delete(0, tk.END)
                    alphaInput.configure(state="disabled")
                    betaInput.configure(state="disabled")
                    gammaInput.configure(state="disabled")

                    messagebox.showwarning("Error with calculations",
                                           "There couldn't exist a triangle with such side lengths")
            elif value == 2:
                # numberOfSides >= 2 and (numberOfHeights >= 1 or s != "" or p != "")
                if h1Val != "" or h2Val != "" or h3Val != "":
                    return 0
                elif sVal != "":
                    try:
                        if aVal == "":
                            h3 = (2 * s) / c
                            alpha = math.asin(h3 / b)
                            a = math.sqrt((b ** 2) + (c ** 2) - 2 * b * c * math.cos(alpha))
                            threeSidesCalc(a, b, c)
                        elif bVal == "":
                            h3 = (2 * s) / c
                            beta = math.asin(h3 / a)
                            b = math.sqrt((a ** 2) + (c ** 2) - 2 * a * c * math.cos(beta))
                            threeSidesCalc(a, b, c)
                        elif cVal == "":
                            h2 = (2 * s) / b
                            gamma = math.asin(h2 / a)
                            c = math.sqrt((a ** 2) + (b ** 2) - 2 * a * b * math.cos(gamma))
                            threeSidesCalc(a, b, c)
                    except:
                        deleteAllValues()
                        messagebox.showwarning("Error with calculations",
                                               "There couldn't exist a triangle with dimensions")
                else:
                    try:
                        if aVal == "":
                            a = p - b - c
                        elif bVal == "":
                            b = p - a - c
                        elif cVal == "":
                            c = p - a - b
                        threeSidesCalc(a, b, c)
                    except:
                        deleteAllValues()
                        messagebox.showwarning("Error with calculations",
                                               "There couldn't exist a triangle with dimensions")
            elif value == 3:

                if aVal != "":
                    '''halfP = p / 2
                    pMinusA = halfP-a
                    print(pMinusA)
                    print("a = ", p*pMinusA)
                    print("b = ", -(p*(pMinusA**2)+(p**2)*pMinusA))
                    print("c = ", (p**2)*(pMinusA**2) - s**2)
                    discriminant = ((p*(pMinusA**2)+(p**2)*pMinusA)**2)-4*(p*pMinusA)*((p**2)*(pMinusA**2) - s**2)
                    print(discriminant)
                    b = ((p*(pMinusA**2)+(p**2)*pMinusA)+math.sqrt((discriminant)))/(2*p*pMinusA)
                    c = ((p*(pMinusA**2)-(p**2)*pMinusA)+math.sqrt((discriminant)))/(2*p*pMinusA)
                    print (b,c)
                    threeSidesCalc(a,b,c)'''


                elif bVal != "":
                    b = p - a - c
                elif cVal != "":
                    c = p - a - b

        def checkEnoughInformation():
            a = firstSideInput.get()
            b = secondSideInput.get()
            c = thirdSideInput.get()

            numberOfSides = 0
            if a != "":
                numberOfSides += 1
            if b != "":
                numberOfSides += 1
            if c != "":
                numberOfSides += 1

            h1 = firstHeightInput.get()
            h2 = secondHeightInput.get()
            h3 = thirdHeightInput.get()

            numberOfHeights = 0
            if h1 != "":
                numberOfHeights += 1
            if h2 != "":
                numberOfHeights += 1
            if h3 != "":
                numberOfHeights += 1

            s = areaInput.get()
            p = perimeterInput.get()

            if numberOfSides >= 3:
                return 1
            elif numberOfSides >= 2 and (s != "" or p != ""):
                return 2
            elif numberOfSides >= 1 and (s != "") and (p != ""):
                return 3
            else:
                if numberOfSides == 1 and s != "":
                    return 4
                else:
                    return 0

        def deleteAllValues():
            firstSideInput.delete(0, tk.END)
            secondSideInput.delete(0, tk.END)
            thirdSideInput.delete(0, tk.END)
            perimeterInput.delete(0, tk.END)
            areaInput.delete(0, tk.END)
            firstHeightInput.delete(0, tk.END)
            secondHeightInput.delete(0, tk.END)
            thirdHeightInput.delete(0, tk.END)

            alphaInput.configure(state="normal")
            betaInput.configure(state="normal")
            gammaInput.configure(state="normal")
            alphaInput.delete(0, tk.END)
            betaInput.delete(0, tk.END)
            gammaInput.delete(0, tk.END)
            alphaInput.configure(state="disabled")
            betaInput.configure(state="disabled")
            gammaInput.configure(state="disabled")

        buttonBack = tk.Button(frameTriangleDiagram,
                               text="Go back",
                               font=(fontName, 15),
                               command=lambda: chooseShape(2)
                               )
        buttonCalc = tk.Button(frameTriangleDiagram,
                               text="Calculate",
                               font=(fontName, 15),
                               command=lambda: calculateTriangle()
                               )
        buttonTrash = tk.Button(frameTriangleDiagram,
                                text="Delete all values",
                                font=(fontName, 15),
                                command=lambda: deleteAllValues()
                                )
        buttonBack.grid(column=0, row=0, padx=5, pady=5)
        buttonCalc.grid(column=1, row=0, padx=5, pady=5)
        buttonTrash.grid(column=2, row=0, padx=5, pady=5)

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
                                    text="Height on a: ",
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
                                     text="Height on b: ",
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
                                    text="Height on c: ",
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

        alphaLabel = tk.Label(frameAngles,
                              text="Alpha angle: ",
                              bd=5,
                              bg='#DDDDDD',
                              font=(fontName, 15),
                              )
        alphaInput = tk.Entry(frameAngles,
                              name="alphaInput",
                              bd=5,
                              bg="#FFFFFF",
                              font=(fontName, 15),
                              state="disabled"
                              )

        betaLabel = tk.Label(frameAngles,
                             text="Beta angle: ",
                             bd=5,
                             bg='#DDDDDD',
                             font=(fontName, 15),
                             )
        betaInput = tk.Entry(frameAngles,
                             bd=5,
                             bg="#FFFFFF",
                             font=(fontName, 15),
                             state="disabled"
                             )
        gammaLabel = tk.Label(frameAngles,
                              text="Gamma angle: ",
                              bd=5,
                              bg='#DDDDDD',
                              font=(fontName, 15),
                              )
        gammaInput = tk.Entry(frameAngles,
                              bd=5,
                              bg="#FFFFFF",
                              font=(fontName, 15),
                              state="disabled"
                              )

        alphaLabel.grid(column=0, row=0, pady=15)
        alphaInput.grid(column=1, row=0, padx=5, pady=15)
        betaLabel.grid(column=0, row=1, pady=15)
        betaInput.grid(column=1, row=1, padx=5, pady=15)
        gammaLabel.grid(column=0, row=2, pady=15)
        gammaInput.grid(column=1, row=2, padx=5, pady=15)


    elif shape == "rightTriangle":
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=1)

        frameTriangleDiagram = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameTriangleDiagram.columnconfigure(0, weight=1)
        frameTriangleDiagram.columnconfigure(1, weight=1)
        frameTriangleDiagram.rowconfigure(0, weight=1)
        frameTriangleDiagram.rowconfigure(1, weight=1)

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

        frameAngles.columnconfigure(0, weight=1)
        frameAngles.columnconfigure(1, weight=1)
        frameAngles.rowconfigure(0, weight=1)
        frameAngles.rowconfigure(1, weight=1)
        frameAngles.rowconfigure(2, weight=1)

        frameTriangleDiagram.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
        frameSides.grid(column=0, row=1, padx=15, pady=15)
        frameHeight.grid(column=1, row=1, padx=15, pady=15)
        frameAreas.grid(column=0, row=2, padx=15, pady=15)
        frameAngles.grid(column=1, row=2, padx=15, pady=15)

        def warningWithDelete(a = "There couldn't exist a triangle with dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        def diagramWindow(a, b):
            top = Toplevel()
            top.title('Shape diagram')

            polygon1 = Polygon([(0, a), (b, 0), (0, 0)])

            fig, ax = plt.subplots(1, 1)

            ax.add_patch(polygon1)

            plt.ylim(0, a)
            plt.xlim(0, b)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)

        def threeSidesCalc(a, b, c):
            if a == "" or b == "":
                if a == "":
                    b = float(b)
                    c = float(c)
                    print(b<0, c)

                    if b<0 or c<0:
                        warningWithDelete()
                        return 0
                    elif (b > c):
                        warningWithDelete("C must be greater than b.")
                        return 0
                    a = math.sqrt(c ** 2 - b ** 2)

                    s = a * b / 2
                    p = a + b + c
                    h = 2 * s / c

                    alpha = math.atan(a / b) * (180 / math.pi)
                    beta = 90 - alpha

                elif b == "":
                    a = float(a)
                    c = float(c)
                    if a < 0 or c < 0:
                        warningWithDelete()
                        return 0
                    elif (a > c):
                        warningWithDelete("C must be greater than b.")
                        return 0

                    b = math.sqrt(c ** 2 - a ** 2)

                    s = a * b / 2
                    p = a + b + c
                    h = 2 * s / c

                    alpha = math.atan(a / b) * (180 / math.pi)
                    beta = 90 - alpha
            elif c == "":
                a = float(a)
                b = float(b)

                if a < 0 or b < 0:
                    warningWithDelete()
                    return 0

                s = a * b / 2
                c = math.sqrt(a ** 2 + b ** 2)
                p = a + b + c
                h = 2 * s / c

                alpha = math.atan(a / b) * (180 / math.pi)
                beta = 90 - alpha


            else:
                a = float(a)
                b = float(b)
                c = float(c)

                if a<0 or b < 0 or c < 0:
                    warningWithDelete()
                    return 0
                elif (b > c) or (a>c):
                    warningWithDelete("C must be greater than b.")
                    return 0

                if (a ** 2 + b ** 2 != c ** 2):
                    perimeterInput.delete(0, tk.END)
                    areaInput.delete(0, tk.END)
                    heightInput.delete(0, tk.END)

                    alphaInput.configure(state="normal")
                    betaInput.configure(state="normal")
                    alphaInput.delete(0, tk.END)
                    betaInput.delete(0, tk.END)
                    alphaInput.configure(state="disabled")
                    betaInput.configure(state="disabled")

                    messagebox.showwarning("Error with calculations",
                                           "There couldn't exist a triangle with such side lengths")
                    return 0

                s = a * b / 2
                p = a + b + c
                h = 2 * s / c

                alpha = math.atan(a / b) * (180 / math.pi)
                beta = 90 - alpha

            firstSideInput.delete(0, tk.END)
            secondSideInput.delete(0, tk.END)
            thirdSideInput.delete(0, tk.END)

            firstSideInput.insert(0, str(a))
            secondSideInput.insert(0, str(b))
            thirdSideInput.insert(0, str(c))

            perimeterInput.delete(0, tk.END)
            perimeterInput.insert(0, str(p))

            areaInput.delete(0, tk.END)
            areaInput.insert(0, str(s))

            heightInput.delete(0, tk.END)
            heightInput.insert(0, str(h))

            alphaInput.configure(state="normal")
            betaInput.configure(state="normal")

            alphaInput.delete(0, tk.END)
            betaInput.delete(0, tk.END)

            alphaInput.insert(0, str(alpha))
            betaInput.insert(0, str(beta))

            alphaInput.configure(state="disabled")
            betaInput.configure(state="disabled")

            diagramWindow(a, b)

        def calculateTriangle():
            value = checkEnoughInformation()
            aVal = firstSideInput.get()
            if aVal != "":
                a = float(firstSideInput.get())
            bVal = secondSideInput.get()
            if bVal != "":
                b = float(secondSideInput.get())
            cVal = thirdSideInput.get()
            if cVal != "":
                c = float(thirdSideInput.get())
            hVal = heightInput.get()
            if hVal != "":
                h = float(heightInput.get())
            sVal = areaInput.get()
            if sVal != "":
                s = float(areaInput.get())
            pVal = perimeterInput.get()
            if pVal != "":
                p = float(perimeterInput.get())
            try:
                if value == 1 or value == 2 or value == 3:
                    try:
                        threeSidesCalc(aVal, bVal, cVal)
                    except:
                        perimeterInput.delete(0, tk.END)
                        areaInput.delete(0, tk.END)
                        heightInput.delete(0, tk.END)

                        alphaInput.configure(state="normal")
                        betaInput.configure(state="normal")
                        gammaInput.configure(state="normal")
                        alphaInput.delete(0, tk.END)
                        betaInput.delete(0, tk.END)
                        gammaInput.delete(0, tk.END)
                        alphaInput.configure(state="disabled")
                        betaInput.configure(state="disabled")
                        gammaInput.configure(state="disabled")

                        messagebox.showwarning("Error with calculations",
                                               "There couldn't exist a triangle with such dimensions")
                elif value == 4:
                    if (aVal != "" or bVal != ""):
                        if sVal != "":
                            if aVal != "":
                                b = 2 * s / a
                                c = ""
                                threeSidesCalc(a, b, c)
                            else:
                                a = 2 * s / b
                                c = ""
                                threeSidesCalc(a, b, c)
                        elif hVal != "":
                            if aVal != "":
                                c1 = math.sqrt(a ** 2 - h ** 2)
                                c2 = h ** 2 / c1
                                c = c1 + c2

                                b = math.sqrt(c ** 2 - a ** 2)
                                threeSidesCalc(a, b, c)
                            else:
                                c = math.sqrt(b ** 2 - h ** 2)
                                a = math.sqrt(c ** 2 - b ** 2)
                                threeSidesCalc(a, b, c)
                else:
                    print(0)
                    if hVal == "":
                        r = 2 * s / p
                        rR = (s - r ** 2) / (2 * r)

                        c = rR * 2

                        a = 0.5 * (c + 2 * r + math.sqrt(c ** 2 - 4 * c * r - 4 * r ** 2))
                        b = math.sqrt(c ** 2 - a ** 2)

                        threeSidesCalc(a, b, c)
            except:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "Please provide correct and/or more information")

        def checkEnoughInformation():
            a = firstSideInput.get()
            b = secondSideInput.get()
            c = thirdSideInput.get()

            numberOfSides = 0
            if a != "":
                numberOfSides += 1
            if b != "":
                numberOfSides += 1
            if c != "":
                numberOfSides += 1

            h = heightInput.get()

            s = areaInput.get()
            p = perimeterInput.get()

            if numberOfSides >= 2:
                if a == "" or b == "":
                    return 1
                elif c == "":
                    return 2
                else:
                    return 3
            elif numberOfSides >= 1 and (s != "" or h != ""):
                return 4
            else:
                print(1)
                return 0

        def deleteAllValues():
            firstSideInput.delete(0, tk.END)
            secondSideInput.delete(0, tk.END)
            thirdSideInput.delete(0, tk.END)
            perimeterInput.delete(0, tk.END)
            areaInput.delete(0, tk.END)
            heightInput.delete(0, tk.END)

            alphaInput.configure(state="normal")
            betaInput.configure(state="normal")
            alphaInput.delete(0, tk.END)
            betaInput.delete(0, tk.END)
            alphaInput.configure(state="disabled")
            betaInput.configure(state="disabled")

        buttonBack = tk.Button(frameTriangleDiagram,
                               text="Go back",
                               font=(fontName, 15),
                               command=lambda: chooseShape(2)
                               )
        buttonCalc = tk.Button(frameTriangleDiagram,
                               text="Calculate",
                               font=(fontName, 15),
                               command=lambda: calculateTriangle()
                               )
        buttonTrash = tk.Button(frameTriangleDiagram,
                                text="Delete all values",
                                font=(fontName, 15),
                                command=lambda: deleteAllValues()
                                )
        buttonBack.grid(column=0, row=0, padx=5, pady=5)
        buttonCalc.grid(column=1, row=0, padx=5, pady=5)
        buttonTrash.grid(column=2, row=0, padx=5, pady=5)

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
                                    text="Height on c: ",
                                    bd=5,
                                    bg='#DDDDDD',
                                    font=(fontName, 15),
                                    )
        heightInput = tk.Entry(frameHeight,
                               bd=5,
                               bg="#FFFFFF",
                               font=(fontName, 15),
                               )

        firstHeightLabel.grid(column=0, row=0, pady=15)
        heightInput.grid(column=1, row=0, padx=5, pady=15)

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

        alphaLabel = tk.Label(frameAngles,
                              text="Alpha angle: ",
                              bd=5,
                              bg='#DDDDDD',
                              font=(fontName, 15),
                              )
        alphaInput = tk.Entry(frameAngles,
                              name="alphaInput",
                              bd=5,
                              bg="#FFFFFF",
                              font=(fontName, 15),
                              state="disabled"
                              )

        betaLabel = tk.Label(frameAngles,
                             text="Beta angle: ",
                             bd=5,
                             bg='#DDDDDD',
                             font=(fontName, 15),
                             )
        betaInput = tk.Entry(frameAngles,
                             bd=5,
                             bg="#FFFFFF",
                             font=(fontName, 15),
                             state="disabled"
                             )
        gammaLabel = tk.Label(frameAngles,
                              text="Gamma angle: ",
                              bd=5,
                              bg='#DDDDDD',
                              font=(fontName, 15),
                              )
        gammaInput = tk.Entry(frameAngles,
                              bd=5,
                              bg="#FFFFFF",
                              font=(fontName, 15),
                              state="disabled"
                              )
        gammaInput.configure(state="normal")
        gammaInput.insert(0, str(90))
        gammaInput.configure(state="disabled")

        alphaLabel.grid(column=0, row=0, pady=15)
        alphaInput.grid(column=1, row=0, padx=5, pady=15)
        betaLabel.grid(column=0, row=1, pady=15)
        betaInput.grid(column=1, row=1, padx=5, pady=15)
        gammaLabel.grid(column=0, row=2, pady=15)
        gammaInput.grid(column=1, row=2, padx=5, pady=15)


    elif shape == "isoTriangle":
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=1)

        frameTriangleDiagram = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameTriangleDiagram.columnconfigure(0, weight=1)
        frameTriangleDiagram.columnconfigure(1, weight=1)
        frameTriangleDiagram.rowconfigure(0, weight=1)
        frameTriangleDiagram.rowconfigure(1, weight=1)

        frameSides = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameSides.columnconfigure(0, weight=1)
        frameSides.columnconfigure(1, weight=1)
        frameSides.rowconfigure(0, weight=1)
        frameSides.rowconfigure(1, weight=1)

        frameHeight = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameHeight.columnconfigure(0, weight=1)
        frameHeight.columnconfigure(1, weight=1)
        frameHeight.rowconfigure(0, weight=1)
        frameHeight.rowconfigure(1, weight=1)

        frameAreas = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAreas.columnconfigure(0, weight=1)
        frameAreas.columnconfigure(1, weight=1)
        frameAreas.rowconfigure(0, weight=1)
        frameAreas.rowconfigure(1, weight=1)

        frameAngles = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAngles.columnconfigure(0, weight=1)
        frameAngles.columnconfigure(1, weight=1)
        frameAngles.rowconfigure(0, weight=1)
        frameAngles.rowconfigure(1, weight=1)

        frameTriangleDiagram.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
        frameSides.grid(column=0, row=1, padx=15, pady=15)
        frameHeight.grid(column=1, row=1, padx=15, pady=15)
        frameAreas.grid(column=0, row=2, padx=15, pady=15)
        frameAngles.grid(column=1, row=2, padx=15, pady=15)

        def warningWithDelete(a = "There couldn't exist a triangle with dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        def diagramWindow(a, h1):
            top = Toplevel()
            top.title('Shape diagram')

            polygon1 = Polygon([(0, 0), (a, 0), (a/2, h1)])

            fig, ax = plt.subplots(1, 1)

            ax.add_patch(polygon1)

            plt.ylim(0, math.ceil(h1))
            plt.xlim(0, math.ceil(a))
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)  # Use grid manager for the canvas

        def twoSidesCalc(a, b):
            if a + b > b and b + b > a:
                p = a + 2 * b
                halfP = p / 2

                firstSideInput.delete(0, tk.END)
                secondSideInput.delete(0, tk.END)

                firstSideInput.insert(0, str(a))
                secondSideInput.insert(0, str(b))

                perimeterInput.delete(0, tk.END)
                perimeterInput.insert(0, str(p))

                s = math.sqrt(halfP * (halfP - a) * (halfP - b) * (halfP - b))
                areaInput.delete(0, tk.END)
                areaInput.insert(0, str(s))

                h1 = s * 2 / a
                h2 = s * 2 / b

                firstHeightInput.delete(0, tk.END)
                secondHeightInput.delete(0, tk.END)

                firstHeightInput.insert(0, str(h1))
                secondHeightInput.insert(0, str(h2))

                alphaInput.configure(state="normal")
                betaInput.configure(state="normal")

                alphaInput.delete(0, tk.END)
                betaInput.delete(0, tk.END)

                alpha = math.acos(((b ** 2) + (b ** 2) - (a ** 2)) / (2 * b * b)) * (180.0 / math.pi)
                beta = math.acos(((a ** 2) + (b ** 2) - (b ** 2)) / (2 * a * b)) * (180.0 / math.pi)

                alphaInput.insert(0, str(alpha))
                betaInput.insert(0, str(beta))

                alphaInput.configure(state="disabled")
                betaInput.configure(state="disabled")
                diagramWindow(a, b, h1)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateTriangle():
            value = checkEnoughInformation()
            aVal = firstSideInput.get()
            if aVal != "":
                a = float(firstSideInput.get())
            bVal = secondSideInput.get()
            if bVal != "":
                b = float(secondSideInput.get())
            sVal = areaInput.get()
            if sVal != "":
                s = float(areaInput.get())
            pVal = perimeterInput.get()
            if pVal != "":
                p = float(perimeterInput.get())

            if value == 1:
                try:
                    if a<0 or b<0:
                        warningWithDelete()
                    twoSidesCalc(a,b)
                except:
                    warningWithDelete()
            elif value == 2:
                if pVal != "":
                    try:
                        if aVal!="":
                            if a<0 or p<0:
                                warningWithDelete()
                            b = (p-a)/2
                            twoSidesCalc(a, b)
                        elif bVal!="":
                            if b<0 or p<0:
                                warningWithDelete()
                            a = p-2*b
                            twoSidesCalc(a,b)
                    except:
                        warningWithDelete()
                elif sVal != "":
                    try:
                        if aVal != "":
                            if a < 0 or s < 0:
                                warningWithDelete()
                            h1 = 2*s/a
                            b = math.sqrt((a/2)**2 + h1**2)
                            twoSidesCalc(a, b)
                        elif bVal != "":
                            if b < 0 or s < 0:
                                warningWithDelete()
                            h2 = 2*s/b
                            alpha = math.asin(h2/b)
                            a = 2*b*math.sin((alpha)/2)
                            twoSidesCalc(a, b)
                    except:
                        deleteAllValues()
                        messagebox.showwarning("Error with calculations",
                                               "There couldn't exist a triangle with dimensions")
                else:
                    try:
                        return 0
                    except:
                        deleteAllValues()
                        messagebox.showwarning("Error with calculations",
                                               "There couldn't exist a triangle with dimensions")
            else:
                warningWithDelete("Not enough information")


        def checkEnoughInformation():
            a = firstSideInput.get()
            b = secondSideInput.get()

            numberOfSides = 0
            if a != "":
                numberOfSides += 1
            if b != "":
                numberOfSides += 1

            h1 = firstHeightInput.get()
            h2 = secondHeightInput.get()

            numberOfHeights = 0
            if h1 != "":
                numberOfHeights += 1
            if h2 != "":
                numberOfHeights += 1

            s = areaInput.get()
            p = perimeterInput.get()

            if numberOfSides >= 2:
                return 1
            elif numberOfSides >= 1 and (s != "" or p != ""):
                return 2
            else:
                return 0

        def deleteAllValues():
            firstSideInput.delete(0, tk.END)
            secondSideInput.delete(0, tk.END)
            perimeterInput.delete(0, tk.END)
            areaInput.delete(0, tk.END)
            firstHeightInput.delete(0, tk.END)
            secondHeightInput.delete(0, tk.END)

            alphaInput.configure(state="normal")
            betaInput.configure(state="normal")
            alphaInput.delete(0, tk.END)
            betaInput.delete(0, tk.END)
            alphaInput.configure(state="disabled")
            betaInput.configure(state="disabled")

        buttonBack = tk.Button(frameTriangleDiagram,
                               text="Go back",
                               font=(fontName, 15),
                               command=lambda: chooseShape(2)
                               )
        buttonCalc = tk.Button(frameTriangleDiagram,
                               text="Calculate",
                               font=(fontName, 15),
                               command=lambda: calculateTriangle()
                               )
        buttonTrash = tk.Button(frameTriangleDiagram,
                                text="Delete all values",
                                font=(fontName, 15),
                                command=lambda: deleteAllValues()
                                )
        buttonBack.grid(column=0, row=0, padx=5, pady=5)
        buttonCalc.grid(column=1, row=0, padx=5, pady=5)
        buttonTrash.grid(column=2, row=0, padx=5, pady=5)

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
                                   text="Side b (two sides): ",
                                   bd=5,
                                   bg='#DDDDDD',
                                   font=(fontName, 15),
                                   )
        secondSideInput = tk.Entry(frameSides,
                                   bd=5,
                                   bg="#FFFFFF",
                                   font=(fontName, 15),
                                   )


        firstSideLabel.grid(column=0, row=0, pady=15)
        firstSideInput.grid(column=1, row=0, padx=5, pady=15)
        secondSideLabel.grid(column=0, row=1, pady=15)
        secondSideInput.grid(column=1, row=1, padx=5, pady=15)

        firstHeightLabel = tk.Label(frameHeight,
                                    text="Height on a: ",
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
                                     text="Height on b: ",
                                     bd=5,
                                     bg='#DDDDDD',
                                     font=(fontName, 15),
                                     )
        secondHeightInput = tk.Entry(frameHeight,
                                     bd=5,
                                     bg="#FFFFFF",
                                     font=(fontName, 15),
                                     )


        firstHeightLabel.grid(column=0, row=0, pady=15)
        firstHeightInput.grid(column=1, row=0, padx=5, pady=15)
        secondHeightLabel.grid(column=0, row=1, pady=15)
        secondHeightInput.grid(column=1, row=1, padx=5, pady=15)

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

        alphaLabel = tk.Label(frameAngles,
                              text="Alpha angle: ",
                              bd=5,
                              bg='#DDDDDD',
                              font=(fontName, 15),
                              )
        alphaInput = tk.Entry(frameAngles,
                              name="alphaInput",
                              bd=5,
                              bg="#FFFFFF",
                              font=(fontName, 15),
                              state="disabled"
                              )

        betaLabel = tk.Label(frameAngles,
                             text="Beta angle: ",
                             bd=5,
                             bg='#DDDDDD',
                             font=(fontName, 15),
                             )
        betaInput = tk.Entry(frameAngles,
                             bd=5,
                             bg="#FFFFFF",
                             font=(fontName, 15),
                             state="disabled"
                             )

        alphaLabel.grid(column=0, row=0, pady=15)
        alphaInput.grid(column=1, row=0, padx=5, pady=15)
        betaLabel.grid(column=0, row=1, pady=15)
        betaInput.grid(column=1, row=1, padx=5, pady=15)


    elif shape == "equTriangle":
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=1)

        frameTriangleDiagram = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameTriangleDiagram.columnconfigure(0, weight=1)
        frameTriangleDiagram.columnconfigure(1, weight=1)
        frameTriangleDiagram.rowconfigure(0, weight=1)
        frameTriangleDiagram.rowconfigure(1, weight=1)

        frameSides = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameSides.columnconfigure(0, weight=1)
        frameSides.columnconfigure(1, weight=1)
        frameSides.rowconfigure(0, weight=1)

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

        frameAngles.columnconfigure(0, weight=1)
        frameAngles.columnconfigure(1, weight=1)
        frameAngles.rowconfigure(0, weight=1)

        frameTriangleDiagram.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
        frameSides.grid(column=0, row=1, padx=15, pady=15)
        frameHeight.grid(column=1, row=1, padx=15, pady=15)
        frameAreas.grid(column=0, row=2, padx=15, pady=15)
        frameAngles.grid(column=1, row=2, padx=15, pady=15)

        def diagramWindow(a, h1):
            top = Toplevel()
            top.title('Shape diagram')

            polygon1 = Polygon([(0, 0), (a, 0), (a/2, h1)])

            fig, ax = plt.subplots(1, 1)

            ax.add_patch(polygon1)

            plt.ylim(0, math.ceil(h1))
            plt.xlim(0, math.ceil(a))
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)  # Use grid manager for the canvas

        def oneSideCalc(a):
            if a>0:
                p = 3*a
                h = a * math.sqrt(3) / 2
                s = a**2 * math.sqrt(3) / 4
                r = a * math.sqrt(3) / 6
                R = a * math.sqrt(3) / 3

                firstSideInput.delete(0, tk.END)

                firstSideInput.insert(0, str(a))

                perimeterInput.delete(0, tk.END)
                perimeterInput.insert(0, str(p))

                areaInput.delete(0, tk.END)
                areaInput.insert(0, str(s))

                firstHeightInput.delete(0, tk.END)
                firstHeightInput.insert(0, str(h))

                inRadiusInput.delete(0, tk.END)
                inRadiusInput.insert(0, str(r))
                outRadiusInput.delete(0, tk.END)
                outRadiusInput.insert(0, str(R))

                diagramWindow(a,h)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateTriangle():
            value = checkEnoughInformation()
            aVal = firstSideInput.get()
            if aVal != "":
                a = float(firstSideInput.get())
            sVal = areaInput.get()
            if sVal != "":
                s = float(areaInput.get())
            pVal = perimeterInput.get()
            if pVal != "":
                p = float(perimeterInput.get())
            hVal = firstHeightInput.get()
            if hVal != "":
                h = float(firstHeightInput.get())
            rVal = inRadiusInput.get()
            if rVal != "":
                r = float(inRadiusInput.get())
            outRVal = outRadiusInput.get()
            if outRVal != "":
                R = float(outRadiusInput.get())


            if value == 1:
                try:
                    if a<0:
                        warningWithDelete()
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 2:
                try:
                    if h<0:
                        warningWithDelete()
                    a = 2*h*math.sqrt(3)/3
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 3:
                try:
                    if r<0:
                        warningWithDelete()
                    a = 2*math.sqrt(3)*r
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 4:
                try:
                    if R<0:
                        warningWithDelete()
                    a = math.sqrt(3) * R
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 5:
                try:
                    if s < 0:
                        warningWithDelete()
                    a = math.sqrt(4*s*math.sqrt(3)/3)
                    oneSideCalc(a)

                except:
                    warningWithDelete()
            elif value == 6:
                try:
                    if p<0:
                        warningWithDelete()
                    a = p/3
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            else:
                warningWithDelete("Not enough information")


        def checkEnoughInformation():
            a = firstSideInput.get()
            h = firstHeightInput.get()
            r = inRadiusInput.get()
            R = outRadiusInput.get()
            s = areaInput.get()
            p = perimeterInput.get()

            if a!="":
                return 1
            elif h!="":
                return 2
            elif r!="":
                return 3
            elif R!="":
                return 4
            elif s!="":
                return 5
            elif p!="":
                return 6
            else:
                return 0

        def deleteAllValues():
            firstSideInput.delete(0, tk.END)
            perimeterInput.delete(0, tk.END)
            areaInput.delete(0, tk.END)
            firstHeightInput.delete(0, tk.END)
            inRadiusInput.delete(0, tk.END)
            outRadiusInput.delete(0, tk.END)


        buttonBack = tk.Button(frameTriangleDiagram,
                               text="Go back",
                               font=(fontName, 15),
                               command=lambda: chooseShape(2)
                               )
        buttonCalc = tk.Button(frameTriangleDiagram,
                               text="Calculate",
                               font=(fontName, 15),
                               command=lambda: calculateTriangle()
                               )
        buttonTrash = tk.Button(frameTriangleDiagram,
                                text="Delete all values",
                                font=(fontName, 15),
                                command=lambda: deleteAllValues()
                                )
        buttonBack.grid(column=0, row=0, padx=5, pady=5)
        buttonCalc.grid(column=1, row=0, padx=5, pady=5)
        buttonTrash.grid(column=2, row=0, padx=5, pady=5)

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



        firstSideLabel.grid(column=0, row=0, pady=15)
        firstSideInput.grid(column=1, row=0, padx=5, pady=15)

        firstHeightLabel = tk.Label(frameHeight,
                                    text="Height on a: ",
                                    bd=5,
                                    bg='#DDDDDD',
                                    font=(fontName, 15),
                                    )
        firstHeightInput = tk.Entry(frameHeight,
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 15),
                                    )
        inRadiusLabel = tk.Label(frameHeight,
                                    text="Inradius: ",
                                    bd=5,
                                    bg='#DDDDDD',
                                    font=(fontName, 15),
                                    )
        inRadiusInput = tk.Entry(frameHeight,
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 15),
                                    )
        outRadiusLabel = tk.Label(frameHeight,
                                    text="Circumradius: ",
                                    bd=5,
                                    bg='#DDDDDD',
                                    font=(fontName, 15),
                                    )
        outRadiusInput = tk.Entry(frameHeight,
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 15),
                                    )



        firstHeightLabel.grid(column=0, row=0, pady=15)
        firstHeightInput.grid(column=1, row=0, padx=5, pady=15)
        inRadiusLabel.grid(column=0, row=1, pady=15)
        inRadiusInput.grid(column=1, row=1, padx=5, pady=15)
        outRadiusLabel.grid(column=0, row=2, pady=15)
        outRadiusInput.grid(column=1, row=2, padx=5, pady=15)

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

        alphaLabel = tk.Label(frameAngles,
                              text="Alpha angle: ",
                              bd=5,
                              bg='#DDDDDD',
                              font=(fontName, 15),
                              )
        alphaInput = tk.Entry(frameAngles,
                              name="alphaInput",
                              bd=5,
                              bg="#FFFFFF",
                              font=(fontName, 15),
                              state="disabled"
                              )


        alphaLabel.grid(column=0, row=0, pady=15)
        alphaInput.grid(column=1, row=0, padx=5, pady=15)

        alphaInput.configure(state="normal")
        alphaInput.insert(0, str(60))
        alphaInput.configure(state="disabled")


    elif shape == "square":
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=1)

        frameMenu = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameMenu.columnconfigure(0, weight=1)
        frameMenu.columnconfigure(1, weight=1)
        frameMenu.rowconfigure(0, weight=1)
        frameMenu.rowconfigure(1, weight=1)

        frameSides = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameSides.columnconfigure(0, weight=1)
        frameSides.columnconfigure(1, weight=1)
        frameSides.rowconfigure(0, weight=1)

        frameOthers = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameOthers.columnconfigure(0, weight=1)
        frameOthers.columnconfigure(1, weight=1)
        frameOthers.rowconfigure(0, weight=1)
        frameOthers.rowconfigure(1, weight=1)
        frameOthers.rowconfigure(2, weight=1)

        frameAreas = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAreas.columnconfigure(0, weight=1)
        frameAreas.columnconfigure(1, weight=1)
        frameAreas.rowconfigure(0, weight=1)
        frameAreas.rowconfigure(1, weight=1)

        frameAngles = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAngles.columnconfigure(0, weight=1)
        frameAngles.columnconfigure(1, weight=1)
        frameAngles.rowconfigure(0, weight=1)

        frameMenu.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
        frameSides.grid(column=0, row=1, padx=15, pady=15)
        frameOthers.grid(column=1, row=1, padx=15, pady=15)
        frameAreas.grid(column=0, row=2, padx=15, pady=15)
        frameAngles.grid(column=1, row=2, padx=15, pady=15)

        def warningWithDelete(a = "There couldn't exist a triangle with dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        def diagramWindow(a):
            top = Toplevel()
            top.title('Shape diagram')

            polygon1 = Polygon([(0, 0), (a, 0), (a, a), (0, a)])

            fig, ax = plt.subplots(1, 1)

            ax.add_patch(polygon1)

            plt.xlim(0, a)
            plt.ylim(0, a)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)  # Use grid manager for the canvas

        def oneSideCalc(a):
            if a > 0:
                p = 4 * a
                d = a * math.sqrt(2)
                s = a ** 2
                r = a / 2
                R = d / 2

                firstSideInput.delete(0, tk.END)
                firstSideInput.insert(0, str(a))

                perimeterInput.delete(0, tk.END)
                perimeterInput.insert(0, str(p))

                areaInput.delete(0, tk.END)
                areaInput.insert(0, str(s))

                firstDiagonal.delete(0, tk.END)
                firstDiagonal.insert(0, str(d))

                inRadiusInput.delete(0, tk.END)
                inRadiusInput.insert(0, str(r))
                outRadiusInput.delete(0, tk.END)
                outRadiusInput.insert(0, str(R))

                diagramWindow(a)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateSquare():
            value = checkEnoughInformation()
            aVal = firstSideInput.get()
            if aVal != "":
                a = float(firstSideInput.get())
            sVal = areaInput.get()
            if sVal != "":
                s = float(areaInput.get())
            pVal = perimeterInput.get()
            if pVal != "":
                p = float(perimeterInput.get())
            dVal = firstDiagonal.get()
            if dVal != "":
                d = float(firstDiagonal.get())
            rVal = inRadiusInput.get()
            if rVal != "":
                r = float(inRadiusInput.get())
            outRVal = outRadiusInput.get()
            if outRVal != "":
                R = float(outRadiusInput.get())


            if value == 1:
                try:
                    if a<0:
                        warningWithDelete()
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 2:
                try:
                    if d<0:
                        warningWithDelete()
                    a = d*math.sqrt(2)/2
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 3:
                try:
                    if r<0:
                        warningWithDelete()
                    a = 2*r
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 4:
                try:
                    if R<0:
                        warningWithDelete()
                    d = 2*R
                    a = d * math.sqrt(2) / 2
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 5:
                try:
                    if s < 0:
                        warningWithDelete()
                    a = math.sqrt(s)
                    oneSideCalc(a)

                except:
                    warningWithDelete()
            elif value == 6:
                try:
                    if p<0:
                        warningWithDelete()
                    a = p/4
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            else:
                warningWithDelete("Not enough information")


        def checkEnoughInformation():
            a = firstSideInput.get()
            d = firstDiagonal.get()
            r = inRadiusInput.get()
            R = outRadiusInput.get()
            s = areaInput.get()
            p = perimeterInput.get()

            if a!="":
                return 1
            elif d!="":
                return 2
            elif r!="":
                return 3
            elif R!="":
                return 4
            elif s!="":
                return 5
            elif p!="":
                return 6
            else:
                return 0

        def deleteAllValues():
            firstSideInput.delete(0, tk.END)
            perimeterInput.delete(0, tk.END)
            areaInput.delete(0, tk.END)
            firstDiagonal.delete(0, tk.END)
            inRadiusInput.delete(0, tk.END)
            outRadiusInput.delete(0, tk.END)


        buttonBack = tk.Button(frameMenu,
                               text="Go back",
                               font=(fontName, 15),
                               command=lambda: chooseShape(2)
                               )
        buttonCalc = tk.Button(frameMenu,
                               text="Calculate",
                               font=(fontName, 15),
                               command=lambda: calculateSquare()
                               )
        buttonTrash = tk.Button(frameMenu,
                                text="Delete all values",
                                font=(fontName, 15),
                                command=lambda: deleteAllValues()
                                )
        buttonBack.grid(column=0, row=0, padx=5, pady=5)
        buttonCalc.grid(column=1, row=0, padx=5, pady=5)
        buttonTrash.grid(column=2, row=0, padx=5, pady=5)

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



        firstSideLabel.grid(column=0, row=0, pady=15)
        firstSideInput.grid(column=1, row=0, padx=5, pady=15)

        firstDiagonalLabel = tk.Label(frameOthers,
                                    text="Diagonal: ",
                                    bd=5,
                                    bg='#DDDDDD',
                                    font=(fontName, 15),
                                    )
        firstDiagonal = tk.Entry(frameOthers,
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 15),
                                    )
        inRadiusLabel = tk.Label(frameOthers,
                                    text="Inradius: ",
                                    bd=5,
                                    bg='#DDDDDD',
                                    font=(fontName, 15),
                                    )
        inRadiusInput = tk.Entry(frameOthers,
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 15),
                                    )
        outRadiusLabel = tk.Label(frameOthers,
                                    text="Circumradius: ",
                                    bd=5,
                                    bg='#DDDDDD',
                                    font=(fontName, 15),
                                    )
        outRadiusInput = tk.Entry(frameOthers,
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 15),
                                    )



        firstDiagonalLabel.grid(column=0, row=0, pady=15)
        firstDiagonal.grid(column=1, row=0, padx=5, pady=15)
        inRadiusLabel.grid(column=0, row=1, pady=15)
        inRadiusInput.grid(column=1, row=1, padx=5, pady=15)
        outRadiusLabel.grid(column=0, row=2, pady=15)
        outRadiusInput.grid(column=1, row=2, padx=5, pady=15)

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

        alphaLabel = tk.Label(frameAngles,
                              text="Alpha angle: ",
                              bd=5,
                              bg='#DDDDDD',
                              font=(fontName, 15),
                              )
        alphaInput = tk.Entry(frameAngles,
                              name="alphaInput",
                              bd=5,
                              bg="#FFFFFF",
                              font=(fontName, 15),
                              state="disabled"
                              )


        alphaLabel.grid(column=0, row=0, pady=15)
        alphaInput.grid(column=1, row=0, padx=5, pady=15)

        alphaInput.configure(state="normal")
        alphaInput.insert(0, str(90))
        alphaInput.configure(state="disabled")


    elif shape == "rectangle":
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=1)

        frameMenu = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameMenu.columnconfigure(0, weight=1)
        frameMenu.columnconfigure(1, weight=1)
        frameMenu.rowconfigure(0, weight=1)
        frameMenu.rowconfigure(1, weight=1)

        frameSides = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameSides.columnconfigure(0, weight=1)
        frameSides.columnconfigure(1, weight=1)
        frameSides.rowconfigure(0, weight=1)

        frameOthers = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameOthers.columnconfigure(0, weight=1)
        frameOthers.columnconfigure(1, weight=1)
        frameOthers.rowconfigure(0, weight=1)
        frameOthers.rowconfigure(1, weight=1)
        frameOthers.rowconfigure(2, weight=1)

        frameAreas = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAreas.columnconfigure(0, weight=1)
        frameAreas.columnconfigure(1, weight=1)
        frameAreas.rowconfigure(0, weight=1)
        frameAreas.rowconfigure(1, weight=1)

        frameAngles = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAngles.columnconfigure(0, weight=1)
        frameAngles.columnconfigure(1, weight=1)
        frameAngles.rowconfigure(0, weight=1)
        frameAngles.rowconfigure(1, weight=1)

        frameMenu.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
        frameSides.grid(column=0, row=1, padx=15, pady=15)
        frameOthers.grid(column=1, row=1, padx=15, pady=15)
        frameAreas.grid(column=0, row=2, padx=15, pady=15)
        frameAngles.grid(column=1, row=2, padx=15, pady=15)

        def warningWithDelete(a = "There couldn't exist a triangle with dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        def diagramWindow(a,b):
            top = Toplevel()
            top.title('Shape diagram')

            polygon1 = Polygon([(0, 0), (a, 0), (a, b), (0, b)])

            fig, ax = plt.subplots(1, 1)

            ax.add_patch(polygon1)

            plt.xlim(0, a)
            plt.ylim(0, b)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)  # Use grid manager for the canvas

        def sideCalc(a, b):
            if a > 0 and b > 0:
                p = 2 * (a + b)
                d = math.sqrt(a**2 + b**2)
                s = a*b
                alpha = math.atan(b/a) * (180 / math.pi)
                beta = math.atan(a/b) * (180 / math.pi)

                firstSideInput.delete(0, tk.END)
                firstSideInput.insert(0, str(a))

                secondSideInput.delete(0, tk.END)
                secondSideInput.insert(0, str(b))

                perimeterInput.delete(0, tk.END)
                perimeterInput.insert(0, str(p))

                areaInput.delete(0, tk.END)
                areaInput.insert(0, str(s))

                firstDiagonal.delete(0, tk.END)
                firstDiagonal.insert(0, str(d))

                alphaInput.configure(state="normal")
                betaInput.configure(state="normal")

                alphaInput.delete(0, tk.END)
                betaInput.delete(0, tk.END)

                alphaInput.insert(0, str(alpha))
                betaInput.insert(0, str(beta))

                alphaInput.configure(state="disabled")
                betaInput.configure(state="disabled")

                diagramWindow(a, b)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateSquare():
            value = checkEnoughInformation()
            aVal = firstSideInput.get()
            if aVal != "":
                a = float(firstSideInput.get())
            bVal = secondSideInput.get()
            if bVal != "":
                    b = float(secondSideInput.get())
            sVal = areaInput.get()
            if sVal != "":
                s = float(areaInput.get())
            pVal = perimeterInput.get()
            if pVal != "":
                p = float(perimeterInput.get())
            dVal = firstDiagonal.get()
            if dVal != "":
                d = float(firstDiagonal.get())


            if value == 1:
                try:
                    if a < 0 or b < 0:
                        warningWithDelete()
                    sideCalc(a, b)
                except:
                    warningWithDelete()
            elif value == 2:
                try:
                    if aVal != "":
                        if a < 0 or s < 0:
                            warningWithDelete()
                        b = s / a
                        sideCalc(a, b)
                    elif bVal != "":
                        if b < 0 or s < 0:
                            warningWithDelete()
                        a = s / b
                        sideCalc(a, b)
                except:
                    warningWithDelete()
            elif value == 3:
                try:
                    if aVal != "":
                        if a < 0 or d < 0:
                            warningWithDelete()
                        b = math.sqrt(d**2 - a**2)
                        sideCalc(a, b)
                    elif bVal != "":
                        if b < 0 or d < 0:
                            warningWithDelete()
                        a = math.sqrt(d**2 - b**2)
                        sideCalc(a, b)
                except:
                    warningWithDelete()
            elif value == 4:
                try:
                    if aVal != "":
                        if a < 0 or p < 0:
                            warningWithDelete()
                        b = (p-2*a)/2
                        sideCalc(a, b)
                    elif bVal != "":
                        if b < 0 or p < 0:
                            warningWithDelete()
                        a = (p-2*b)/2
                        sideCalc(a, b)
                except:
                    warningWithDelete()
            elif value == 5:
                try:
                    if s < 0 or d < 0:
                        warningWithDelete()

                    p = 2 * math.sqrt(d**2 + 2*s)
                    a = (p / 2 + math.sqrt((p ** 2) / 4 - 4 * s)) / 2
                    b = (p / 2 - math.sqrt((p ** 2) / 4 - 4 * s)) / 2
                    sideCalc(a, b)

                except:
                    warningWithDelete()
            elif value == 6:
                try:
                    if s < 0 or p < 0:
                        warningWithDelete()
                    a = (p / 2 + math.sqrt((p ** 2) / 4 - 4 * s)) / 2
                    b = (p / 2 - math.sqrt((p ** 2) / 4 - 4 * s)) / 2
                    sideCalc(a, b)

                except:
                    warningWithDelete()
            elif value == 7:
                try:
                    if p<0 or d < 0:
                        warningWithDelete()
                    s = (p**2 - 4*d**2) / 8
                    a = (p / 2 + math.sqrt((p ** 2) / 4 - 4 * s)) / 2
                    b = (p / 2 - math.sqrt((p ** 2) / 4 - 4 * s)) / 2
                    sideCalc(a, b)
                except:
                    warningWithDelete()
            else:
                warningWithDelete("Not enough information")


        def checkEnoughInformation():
            a = firstSideInput.get()
            b = secondSideInput.get()
            d = firstDiagonal.get()
            s = areaInput.get()
            p = perimeterInput.get()

            if a!="" or b!="":
                if a!="" and b!="":
                    return 1
                elif s != "":
                    return 2
                elif d != "":
                    return 3
                elif p != "":
                    return 4
            elif s!="":
                if d!="":
                    return 5
                elif p!="":
                    return 6
            elif p!="" and d!="":
                return 7
            else:
                return 0

        def deleteAllValues():
            firstSideInput.delete(0, tk.END)
            secondSideInput.delete(0, tk.END)
            perimeterInput.delete(0, tk.END)
            areaInput.delete(0, tk.END)
            firstDiagonal.delete(0, tk.END)
            alphaInput.configure(state="normal")
            betaInput.configure(state="normal")
            alphaInput.delete(0, tk.END)
            betaInput.delete(0, tk.END)
            alphaInput.configure(state="disabled")
            betaInput.configure(state="disabled")



        buttonBack = tk.Button(frameMenu,
                               text="Go back",
                               font=(fontName, 15),
                               command=lambda: chooseShape(2)
                               )
        buttonCalc = tk.Button(frameMenu,
                               text="Calculate",
                               font=(fontName, 15),
                               command=lambda: calculateSquare()
                               )
        buttonTrash = tk.Button(frameMenu,
                                text="Delete all values",
                                font=(fontName, 15),
                                command=lambda: deleteAllValues()
                                )
        buttonBack.grid(column=0, row=0, padx=5, pady=5)
        buttonCalc.grid(column=1, row=0, padx=5, pady=5)
        buttonTrash.grid(column=2, row=0, padx=5, pady=5)

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



        firstSideLabel.grid(column=0, row=0, pady=15)
        firstSideInput.grid(column=1, row=0, padx=5, pady=15)
        secondSideLabel.grid(column=0, row=1, pady=15)
        secondSideInput.grid(column=1, row=1, padx=5, pady=15)

        firstDiagonalLabel = tk.Label(frameOthers,
                                    text="Diagonal: ",
                                    bd=5,
                                    bg='#DDDDDD',
                                    font=(fontName, 15),
                                    )
        firstDiagonal = tk.Entry(frameOthers,
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 15),
                                    )



        firstDiagonalLabel.grid(column=0, row=0, pady=15)
        firstDiagonal.grid(column=1, row=0, padx=5, pady=15)

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

        alphaLabel = tk.Label(frameAngles,
                              text="Angle between the diagonal and side a: ",
                              bd=5,
                              bg='#DDDDDD',
                              font=(fontName, 15),
                              )
        alphaInput = tk.Entry(frameAngles,
                              name="alphaInput",
                              bd=5,
                              bg="#FFFFFF",
                              font=(fontName, 15),
                              state="disabled"
                              )
        betaLabel = tk.Label(frameAngles,
                              text="Angle between the diagonal and side b: ",
                              bd=5,
                              bg='#DDDDDD',
                              font=(fontName, 15),
                              )
        betaInput = tk.Entry(frameAngles,
                              name="betaInput",
                              bd=5,
                              bg="#FFFFFF",
                              font=(fontName, 15),
                              state="disabled"
                              )


        alphaLabel.grid(column=0, row=0, pady=15)
        alphaInput.grid(column=1, row=0, padx=5, pady=15)
        betaLabel.grid(column=0, row=1, pady=15)
        betaInput.grid(column=1, row=1, padx=5, pady=15)


    elif shape == "rhombus":
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=1)

        frameMenu = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameMenu.columnconfigure(0, weight=1)
        frameMenu.columnconfigure(1, weight=1)
        frameMenu.rowconfigure(0, weight=1)
        frameMenu.rowconfigure(1, weight=1)

        frameSides = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameSides.columnconfigure(0, weight=1)
        frameSides.columnconfigure(1, weight=1)
        frameSides.rowconfigure(0, weight=1)

        frameOthers = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameOthers.columnconfigure(0, weight=1)
        frameOthers.columnconfigure(1, weight=1)
        frameOthers.rowconfigure(0, weight=1)
        frameOthers.rowconfigure(1, weight=1)
        frameOthers.rowconfigure(2, weight=1)

        frameAreas = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAreas.columnconfigure(0, weight=1)
        frameAreas.columnconfigure(1, weight=1)
        frameAreas.rowconfigure(0, weight=1)
        frameAreas.rowconfigure(1, weight=1)

        frameAngles = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAngles.columnconfigure(0, weight=1)
        frameAngles.columnconfigure(1, weight=1)
        frameAngles.rowconfigure(0, weight=1)
        frameAngles.rowconfigure(1, weight=1)

        frameMenu.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
        frameSides.grid(column=0, row=1, padx=15, pady=15)
        frameOthers.grid(column=1, row=1, padx=15, pady=15)
        frameAreas.grid(column=0, row=2, padx=15, pady=15)
        frameAngles.grid(column=1, row=2, padx=15, pady=15)

        def warningWithDelete(a = "There couldn't exist a triangle with dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        def diagramWindow(a,h):
            top = Toplevel()
            top.title('Shape diagram')

            x = math.sqrt(a**2 - h**2)
            xlimit = a + x

            polygon1 = Polygon([(0, 0), (a, 0), (x+a, h), (x, h)])

            fig, ax = plt.subplots(1, 1)

            ax.add_patch(polygon1)

            plt.xlim(0, xlimit)
            plt.ylim(0, h)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)  # Use grid manager for the canvas

        def sideCalc(a, h):
            if a > 0 and h > 0:
                p = 4 * a
                s = a*h
                alpha = math.asin(h/a)
                beta = 180 - alpha * (180 / math.pi)
                d1 = 2 * a * math.cos(alpha/2)
                d2 = 2 * a * math.sin(alpha/2)
                alpha = alpha * (180 / math.pi)

                firstSideInput.delete(0, tk.END)
                firstSideInput.insert(0, str(a))
                firstHeightInput.delete(0, tk.END)
                firstHeightInput.insert(0, str(h))

                perimeterInput.delete(0, tk.END)
                perimeterInput.insert(0, str(p))

                areaInput.delete(0, tk.END)
                areaInput.insert(0, str(s))

                firstDiagonal.delete(0, tk.END)
                firstDiagonal.insert(0, str(d1))
                secondDiagonal.delete(0, tk.END)
                secondDiagonal.insert(0, str(d2))


                alphaInput.configure(state="normal")
                betaInput.configure(state="normal")

                alphaInput.delete(0, tk.END)
                betaInput.delete(0, tk.END)

                alphaInput.insert(0, str(alpha))
                betaInput.insert(0, str(beta))

                alphaInput.configure(state="disabled")
                betaInput.configure(state="disabled")

                diagramWindow(a, h)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateSquare():
            value = checkEnoughInformation()
            aVal = firstSideInput.get()
            if aVal != "":
                a = float(firstSideInput.get())
            sVal = areaInput.get()
            if sVal != "":
                s = float(areaInput.get())
            pVal = perimeterInput.get()
            if pVal != "":
                p = float(perimeterInput.get())
            d1Val = firstDiagonal.get()
            if d1Val != "":
                d1 = float(firstDiagonal.get())
            d2Val = secondDiagonal.get()
            if d2Val != "":
                d2 = float(secondDiagonal.get())
            hVal = firstHeightInput.get()
            if hVal != "":
                h = float(firstHeightInput.get())


            if value == 1:
                print(a,h)
                try:
                    if pVal != "":
                        if p < 0:
                            warningWithDelete()
                        a = p / 4
                    if a < 0 or h < 0:
                        warningWithDelete()
                    sideCalc(a, h)
                except:
                    warningWithDelete()
            elif value == 2:
                try:
                    if pVal != "":
                        if p < 0:
                            warningWithDelete()
                        a = p / 4
                    if a < 0 or s < 0:
                        warningWithDelete()
                    h = s / a
                    sideCalc(a, h)
                except:
                    warningWithDelete()
            elif value == 3:
                try:
                    if pVal != "":
                        if p < 0:
                            warningWithDelete()
                        a = p / 4
                    if a < 0 or d1 < 0:
                        warningWithDelete()
                    alpha = 2 * math.acos((d1/2)/a)
                    h = a * math.sin( alpha )
                    sideCalc(a, h)
                except:
                    warningWithDelete()
            elif value == 4:
                try:
                    if pVal != "":
                        if p < 0:
                            warningWithDelete()
                        a = p / 4
                    if a < 0 or d2 < 0:
                        warningWithDelete()
                    alpha = 2 * math.asin((d2/2)/a)
                    h = a * math.sin( alpha )
                    sideCalc(a, h)
                except:
                    warningWithDelete()
            elif value == 5:
                try:
                    if s < 0 or h < 0:
                        warningWithDelete()
                    a = s / h
                    sideCalc(a, h)

                except:
                    warningWithDelete()
            elif value == 6:
                try:
                    if h < 0 or d1 < 0:
                        warningWithDelete()
                    alpha = 2 * math.asin(h/d1)
                    a = h / math.sin(alpha)
                    sideCalc(a, h)
                except:
                    warningWithDelete()
            elif value == 7:
                try:
                    if h < 0 or d2 < 0:
                        warningWithDelete()
                    alpha = 2 * math.asin(h/d2)
                    a = h / math.cos(alpha - math.radians(90))
                    sideCalc(a, h)
                except:
                    warningWithDelete()
            elif value == 8:
                try:
                    if s < 0 or d1 < 0:
                        warningWithDelete()
                    d2 = 2 * s / d1
                    a = math.sqrt((d1/2)**2 + (d2/2)**2)
                    h = s/a
                    sideCalc(a, h)
                except:
                    warningWithDelete()
            elif value == 9:
                try:
                    if s < 0 or d2 < 0:
                        warningWithDelete()
                    d1 = 2 * s / d2
                    a = math.sqrt((d1/2)**2 + (d2/2)**2)
                    h = s/a
                    sideCalc(a, h)
                except:
                    warningWithDelete()
            elif value == 10:
                try:
                    if d2 < 0 or d1 < 0:
                        warningWithDelete()
                    print(d1, d2)
                    a = math.sqrt((d1/2)**2 + (d2/2)**2)

                    s = d1 * d2 / 2
                    h = s/a
                    sideCalc(a, h)
                except:
                    warningWithDelete()
            else:
                warningWithDelete("Not enough information")


        def checkEnoughInformation():
            a = firstSideInput.get()
            h = firstHeightInput.get()
            d1 = firstDiagonal.get()
            d2 = secondDiagonal.get()
            s = areaInput.get()
            p = perimeterInput.get()

            if a!="":
                if h!="":
                    return 1
                elif s!="":
                    return 2
                elif d1 != "":
                    return 3
                elif d2 != "":
                    return 4
                else: return 0
            elif p!="":
                if h!="":
                    return 1
                elif s!="":
                    return 2
                elif d1 != "":
                    return 3
                elif d2 != "":
                    return 4
                else: return 0
            elif h != "":
                if s != "":
                    return 5
                elif d1 != "":
                    return 6
                elif d2 != "":
                    return 7
            elif s != "":
                if d1 != "":
                    return 8
                elif d2 != "":
                    return 9
            elif d1 != "" and d2 !="":
                return 10
            else:
                return 0

        def deleteAllValues():
            firstSideInput.delete(0, tk.END)
            firstHeightInput.delete(0, tk.END)
            perimeterInput.delete(0, tk.END)
            areaInput.delete(0, tk.END)
            firstDiagonal.delete(0, tk.END)
            secondDiagonal.delete(0, tk.END)
            alphaInput.configure(state="normal")
            betaInput.configure(state="normal")
            alphaInput.delete(0, tk.END)
            betaInput.delete(0, tk.END)
            alphaInput.configure(state="disabled")
            betaInput.configure(state="disabled")



        buttonBack = tk.Button(frameMenu,
                               text="Go back",
                               font=(fontName, 15),
                               command=lambda: chooseShape(2)
                               )
        buttonCalc = tk.Button(frameMenu,
                               text="Calculate",
                               font=(fontName, 15),
                               command=lambda: calculateSquare()
                               )
        buttonTrash = tk.Button(frameMenu,
                                text="Delete all values",
                                font=(fontName, 15),
                                command=lambda: deleteAllValues()
                                )
        buttonBack.grid(column=0, row=0, padx=5, pady=5)
        buttonCalc.grid(column=1, row=0, padx=5, pady=5)
        buttonTrash.grid(column=2, row=0, padx=5, pady=5)

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

        firstSideLabel.grid(column=0, row=0, pady=15)
        firstSideInput.grid(column=1, row=0, padx=5, pady=15)


        firstHeightLabel = tk.Label(frameOthers,
                                    text="Height: ",
                                    bd=5,
                                    bg='#DDDDDD',
                                    font=(fontName, 15),
                                    )
        firstHeightInput = tk.Entry(frameOthers,
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 15),
                                    )
        firstDiagonalLabel = tk.Label(frameOthers,
                                    text="Longer diagonal: ",
                                    bd=5,
                                    bg='#DDDDDD',
                                    font=(fontName, 15),
                                    )
        firstDiagonal = tk.Entry(frameOthers,
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 15),
                                    )
        secondDiagonalLabel = tk.Label(frameOthers,
                                    text="Shorter diagonal: ",
                                    bd=5,
                                    bg='#DDDDDD',
                                    font=(fontName, 15),
                                    )
        secondDiagonal = tk.Entry(frameOthers,
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 15),
                                    )

        firstHeightLabel.grid(column=0, row=0, pady=15)
        firstHeightInput.grid(column=1, row=0, padx=5, pady=15)
        firstDiagonalLabel.grid(column=0, row=1, pady=15)
        firstDiagonal.grid(column=1, row=1, padx=5, pady=15)
        secondDiagonalLabel.grid(column=0, row=2, pady=15)
        secondDiagonal.grid(column=1, row=2, padx=5, pady=15)

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

        alphaLabel = tk.Label(frameAngles,
                              text="Angle alpha: ",
                              bd=5,
                              bg='#DDDDDD',
                              font=(fontName, 15),
                              )
        alphaInput = tk.Entry(frameAngles,
                              name="alphaInput",
                              bd=5,
                              bg="#FFFFFF",
                              font=(fontName, 15),
                              state="disabled"
                              )
        betaLabel = tk.Label(frameAngles,
                              text="Angle beta: ",
                              bd=5,
                              bg='#DDDDDD',
                              font=(fontName, 15),
                              )
        betaInput = tk.Entry(frameAngles,
                              name="betaInput",
                              bd=5,
                              bg="#FFFFFF",
                              font=(fontName, 15),
                              state="disabled"
                              )


        alphaLabel.grid(column=0, row=0, pady=15)
        alphaInput.grid(column=1, row=0, padx=5, pady=15)
        betaLabel.grid(column=0, row=1, pady=15)
        betaInput.grid(column=1, row=1, padx=5, pady=15)


dimensions()
window.mainloop()
