"""
pip install matplotlib
pip install tkinter
Matplotlib needed to plot diagrams of polygons
tkinter needed for GUI
"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import math
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Most of the code is GUI
'''
Some shortcuts for required content for assignment:
variable declaration: 24 line (and a lot of other)
arithmetic expression: 249 line
use of if else: 45 line
use of sequence types: 230 line
use of for loop: 31 line
use of while loop: 3071 line
a function: 33 line
output: GUI (278 line)
'''

window = tk.Tk()
fontName = "Arial" # We assign a fontName variable a font, to be able to easily change it

def dimensions(): # First function in the code is for the first window to appear in app, where the user will choose the dimensions
    # By the next loop we clear everything in the existing window, so we can start from blank page
    for widget in window.winfo_children():
        widget.destroy()

    # GUI: We make windows' grid
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)

    #GUI:
    greeting = tk.Label(text="Hello to AreaAce!", width=50, height=3, font=(fontName, 25)).grid(column=0, columnspan=2,row=0, padx=15, pady=15)
    chooseDimensions = tk.Label(text="Choose with which dimensions you want to work with:", font=(fontName, 15)).grid(column=0, columnspan=2, row=1, padx=15, pady=15)

    # After clicking one of this buttons, it will start a funciton with a parameter
    twoDButton = tk.Button(text="2D", width=10, height=3, activebackground="#EEEEEE", bd=5, bg="#FFFFFF", font=(fontName, 40, "bold"), command=lambda: chooseShape(2)).grid(column=0, row=2, padx=15, pady=15)
    threeDButton = tk.Button(text="3D", width=10, height=3, activebackground="#EEEEEE", bd=5, bg="#FFFFFF", font=(fontName, 40, "bold"), command=lambda: chooseShape(3)).grid(column=1, row=2, padx=15, pady=15)

#Second function, second page in our app, user will simply choose a shape in this page
def chooseShape(n):
    if n == 2: # When the user choose the 2nd dimension, we open 2nd dimensions shapes
        for widget in window.winfo_children(): # As well as in the first page, we clear the page fully
            widget.destroy()
        #GUI till line 174:
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=3)
        window.rowconfigure(3, weight=3)

        chooseShape = tk.Label(text="Choose the shape:", font=(fontName, 25))
        backButton = tk.Button(text="Go back", font=(fontName, 15), command=dimensions)

        chooseShape.grid(column=0, columnspan=2,  row=1, padx=15, pady=15)
        backButton.grid(column=0, columnspan=2,  row=0, padx=15, pady=15)

        frameTriangles = Frame(window, width=500, height=300, bg='#DDDDDD')
        frameTriangles.grid(column=0, row=2, padx=15, pady=15)

        frameTriangles.columnconfigure(0, weight=1)
        frameTriangles.columnconfigure(1, weight=1)
        frameTriangles.rowconfigure(0, weight=1)
        frameTriangles.rowconfigure(1, weight=1)

        triangleButton = tk.Button(frameTriangles, text="Triangle", activebackground="#EEEEEE", bd=5, bg="#FFFFFF",font=(fontName, 20, "bold"), command=lambda: calcShape("triangle"))
        rightTriangleButton = tk.Button(frameTriangles, text="Right\nTriangle", activebackground="#EEEEEE", bd=5,bg="#FFFFFF", font=(fontName, 20, "bold"),command=lambda: calcShape("rightTriangle"))
        isoTriangleButton = tk.Button(frameTriangles, text="Isosceles\nTriangle", activebackground="#EEEEEE", bd=5,bg="#FFFFFF", font=(fontName, 20, "bold"),command=lambda: calcShape("isoTriangle"))
        equaTriangleButton = tk.Button(frameTriangles, text="Equilateral\nTriangle", activebackground="#EEEEEE", bd=5,bg="#FFFFFF", font=(fontName, 20, "bold"),command=lambda: calcShape("equTriangle"))

        triangleButton.grid(column=0, row=0, padx=15, pady=15)
        rightTriangleButton.grid(column=1, row=0, padx=15, pady=15)
        isoTriangleButton.grid(column=0, row=1, padx=15, pady=15)
        equaTriangleButton.grid(column=1, row=1, padx=15, pady=15)

        frameQuad = Frame(window, width=500, height=600, bg='#DDDDDD')
        frameQuad.grid(column=1, row=2, padx=15, pady=15)

        frameQuad.columnconfigure(0, weight=1)
        frameQuad.columnconfigure(1, weight=1)
        frameQuad.rowconfigure(0, weight=1)
        frameQuad.rowconfigure(1, weight=1)
        frameQuad.rowconfigure(2, weight=1)
        frameQuad.rowconfigure(3, weight=1)

        squareButton = tk.Button(frameQuad, text="Square", compound=BOTTOM, activebackground="#EEEEEE", bd=5,bg="#FFFFFF", font=(fontName, 20, "bold"), command=lambda: calcShape("square"))
        rectangleButton = tk.Button(frameQuad, text="Rectangle", activebackground="#EEEEEE", bd=5, bg="#FFFFFF",font=(fontName, 20, "bold"), command=lambda: calcShape("rectangle"))
        rhombusButton = tk.Button(frameQuad, text="Rhombus", activebackground="#EEEEEE", bd=5, bg="#FFFFFF",font=(fontName, 20, "bold"), command=lambda: calcShape("rhombus"))

        squareButton.grid(column=0, row=0, padx=15, pady=15)
        rectangleButton.grid(column=1, row=0, padx=15, pady=15)
        rhombusButton.grid(column=0, columnspan=2, row=1, padx=15, pady=15)

        frameCircles = Frame(window, width=500, height=300, bg='#DDDDDD')
        frameCircles.grid(column=0, row=3, padx=15, pady=15)

        frameCircles.columnconfigure(0, weight=1)
        frameCircles.rowconfigure(0, weight=1)
        frameCircles.rowconfigure(1, weight=1)

        circleButton = tk.Button(frameCircles, text="Circle", activebackground="#EEEEEE", bd=5, bg="#FFFFFF",font=(fontName, 20, "bold"), command=lambda: calcShape("circle"))
        ellipseButton = tk.Button(frameCircles, text="Ellipse", activebackground="#EEEEEE", bd=5, bg="#FFFFFF",font=(fontName, 20, "bold"), command=lambda: calcShape("ellipse"))

        circleButton.grid(column=0, row=0, padx=15, pady=15)
        ellipseButton.grid(column=0, row=1, padx=15, pady=15)

        frameRegular = Frame(window, width=500, height=300, bg='#DDDDDD')
        frameRegular.grid(column=1, row=3, padx=15, pady=15)

        frameRegular.columnconfigure(0, weight=1)
        frameRegular.columnconfigure(1, weight=1)
        frameRegular.rowconfigure(0, weight=1)
        frameRegular.rowconfigure(1, weight=1)

        nRegularShape = tk.Button(frameRegular, text="Sided regular polygon", activebackground="#EEEEEE", bd=5,bg="#FFFFFF", font=(fontName, 20, "bold"),command=lambda: calcShape("polygon", int(nSideShapeInput.get())))
        nSideShapeInput = tk.Entry(frameRegular, width=4, bd=5, bg="#FFFFFF", font=(fontName, 15))

        nRegularShape.grid(column=1, row=0, padx=15, pady=15)
        nSideShapeInput.grid(column=0, row=0, padx=15, pady=15)



    elif n == 3:
        for widget in window.winfo_children():
            widget.destroy()

        window.columnconfigure(0, weight=1)  # Center-align the first column
        window.columnconfigure(1, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)

        chooseShape = tk.Label(
            text="Choose the shape:",
            font=(fontName, 25)
        )

        backButton = tk.Button(
            text="Go back",
            font=(fontName, 15),
            command=lambda: dimensions()
        )

        chooseShape.grid(column=0, columnspan=2, row=1, padx=15, pady=15)
        backButton.grid(column=0, columnspan=2, row=0, padx=15, pady=15)

        frame3d = Frame(window, width=750, height=400, bg='#DDDDDD')
        frame3d.grid(column=0, row=2, padx=15, pady=15)

        frame3d.columnconfigure(0, weight=1)  # Center-align the first column
        frame3d.columnconfigure(1, weight=1)
        frame3d.rowconfigure(0, weight=1)
        frame3d.rowconfigure(1, weight=1)

        sphereButton = tk.Button(frame3d, text="Sphere", width=10, height=3, activebackground="#EEEEEE", bd=5,bg="#FFFFFF", font=(fontName, 40, "bold"), command=lambda: calcShape("sphere"))
        cubeButton = tk.Button(frame3d, text="Cube", width=10, height=3, activebackground="#EEEEEE", bd=5, bg="#FFFFFF",font=(fontName, 40, "bold"), command=lambda: calcShape("cube"))

        sphereButton.grid(column=0, row=0, padx=15, pady=15)
        cubeButton.grid(column=1, row=0, padx=15, pady=15)

def calcShape(shape, nSides = 0): # 3rd window, when the user has choosen the shape
    # We will do calculations in this function, it gets to arguments, shape: name of the shape. nSides: refers to amount of sides of n-sided right polygon
    for widget in window.winfo_children():
        widget.destroy()

    if shape == "triangle": # We simply check for every single name and if the user choose triangle, we will run this code
        # After this if, every other elif, looks similar to this, just, the other do calculations for
        # other shapes. For example for circle, we need to only have radius, area and perimeter, wherese for
        # triangle, we need to have much more dimensions
        #GUI till 231 line
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

        # Next function deletes the inputs, and throws a warning to user, to indicate we had a problem with calculations
        def warningWithDelete(a = "There couldn't exist a triangle with dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        # Next function is to plot the diagram
        def diagramWindow(a, b, h2):
            # It gets as arguments two sides of triangle, and one of the heights
            # We can notice that to plot any triangle, this three numbers are enough

            top = Toplevel() # GUI: We create a new window
            top.title('Triangle diagram')

            xPlot = math.sqrt(a ** 2 - h2 ** 2) # We calculate the offset of x of the triangle from the third point of triangle
            polygon1 = Polygon([(0, 0), (b, 0), (xPlot, h2)]) # We create a polygon with the numbers we have

            fig, ax = plt.subplots(1, 1) # Give subplots of 1 and 1 for equal diagram

            ax.add_patch(polygon1)
            #limits of diagram:
            # we can notice that the height is basically limit for y, and second point for x
            plt.ylim(0, h2)
            plt.xlim(0, b)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)  # Use grid manager for the canvas

        def threeSidesCalc(a, b, c):
        #This function is used to calculate all the dimensions of a triangle by three sides
            if a + b > c and a + c > b and b + c > a: # By this line we check if the triangle could exist
                # If no, it will throw an error (see the line where the function is called)

                # We calculate everything:
                p = a + b + c
                halfP = p / 2
                s = math.sqrt(halfP * (halfP - a) * (halfP - b) * (halfP - c))
                h1 = s * 2 / a
                h2 = s * 2 / b
                h3 = s * 2 / c
                alpha = math.acos(((b ** 2) + (c ** 2) - (a ** 2)) / (2 * b * c)) * (180.0 / math.pi)
                beta = math.acos(((a ** 2) + (c ** 2) - (b ** 2)) / (2 * a * c)) * (180.0 / math.pi)
                gamma = math.acos(((a ** 2) + (b ** 2) - (c ** 2)) / (2 * b * a)) * (180.0 / math.pi)

                deleteAllValues()
                # We delete and put the values to display to user
                firstSideInput.insert(0, str(round(a, 13)))
                secondSideInput.insert(0, str(round(b, 13)))
                thirdSideInput.insert(0, str(round(c, 13)))
                perimeterInput.insert(0, str(round(p, 13)))
                areaInput.insert(0, str(round(s, 13)))
                firstHeightInput.insert(0, str(round(h1, 13)))
                secondHeightInput.insert(0, str(round(h2, 13)))
                thirdHeightInput.insert(0, str(round(h3, 13)))

                alphaInput.configure(state="normal")
                betaInput.configure(state="normal")
                gammaInput.configure(state="normal")

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
            # This function is needed to get all the information user gave us
            # and bring it to form that we have all three sides, so we can call the previous function
            # to calculate everything using 3 sides
            value = checkEnoughInformation() #Here we check the information is enough or no, we call another function
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

            if value == 1: # Value is telling, what information did the user gave us, so we can calculate everything efficiently
                try:
                    threeSidesCalc(a, b, c)
                except:
                    warningWithDelete()

            elif value == 2:
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
                    warningWithDelete("Not enough information given")
                    '''
                    halfP = p / 2
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
                    threeSidesCalc(a,b,c)
                    '''

                elif bVal != "":
                    warningWithDelete("Not enough information given")
                    b = p - a - c
                elif cVal != "":
                    warningWithDelete("Not enough information given")
                    c = p - a - b
            else:
                warningWithDelete("Not enough information given")

        def checkEnoughInformation():
            a = firstSideInput.get()
            b = secondSideInput.get()
            c = thirdSideInput.get()
            # We basically check, what the user has given us, because for different inputs
            # lets say 3 sides, and 2 sides and area, we need to have two various functions
            # calculating the third side.
            # We can see that for the first, we already have 3 sides. But for second one, we need
            # to at first calculate, and only then call the function to calculate the triangle
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

        def deleteAllValues(): # We delete every input from the page
            for entry in [firstSideInput, secondSideInput, thirdSideInput, perimeterInput, areaInput, firstHeightInput,
                          secondHeightInput, thirdHeightInput]:
                entry.delete(0, tk.END)

            for entry in [alphaInput, betaInput, gammaInput]:
                entry.configure(state="normal")
                entry.delete(0, tk.END)
                entry.configure(state="disabled")

        buttonBack, buttonCalc, buttonTrash = (
            tk.Button(frameTriangleDiagram, text="Go back", font=(fontName, 15), command=lambda: chooseShape(2)),
            tk.Button(frameTriangleDiagram, text="Calculate", font=(fontName, 15), command=lambda: calculateTriangle()),
            tk.Button(frameTriangleDiagram, text="Delete all values", font=(fontName, 15),command=lambda: deleteAllValues())
        )
        buttonBack.grid(column=0, row=0, padx=5, pady=5)
        buttonCalc.grid(column=1, row=0, padx=5, pady=5)
        buttonTrash.grid(column=2, row=0, padx=5, pady=5)

        firstSideLabel, firstSideInput = tk.Label(frameSides, text="Side a: ", bd=5, bg='#DDDDDD',
                                                  font=(fontName, 15)), tk.Entry(frameSides, bd=5, bg="#FFFFFF",
                                                                                 font=(fontName, 15))
        secondSideLabel, secondSideInput = tk.Label(frameSides, text="Side b: ", bd=5, bg='#DDDDDD',
                                                    font=(fontName, 15)), tk.Entry(frameSides, bd=5, bg="#FFFFFF",
                                                                                   font=(fontName, 15))
        thirdSideLabel, thirdSideInput = tk.Label(frameSides, text="Side c: ", bd=5, bg='#DDDDDD',
                                                  font=(fontName, 15)), tk.Entry(frameSides, bd=5, bg="#FFFFFF",
                                                                                 font=(fontName, 15))

        firstSideLabel.grid(column=0, row=0, pady=15)
        firstSideInput.grid(column=1, row=0, padx=5, pady=15)
        secondSideLabel.grid(column=0, row=1, pady=15)
        secondSideInput.grid(column=1, row=1, padx=5, pady=15)
        thirdSideLabel.grid(column=0, row=2, pady=15)
        thirdSideInput.grid(column=1, row=2, padx=5, pady=15)

        firstHeightLabel, firstHeightInput = tk.Label(frameHeight, text="Height on a: ", bd=5, bg='#DDDDDD',
                                                      font=(fontName, 15)), tk.Entry(frameHeight, bd=5, bg="#FFFFFF",
                                                                                     font=(fontName, 15))
        secondHeightLabel, secondHeightInput = tk.Label(frameHeight, text="Height on b: ", bd=5, bg='#DDDDDD',
                                                        font=(fontName, 15)), tk.Entry(frameHeight, bd=5, bg="#FFFFFF",
                                                                                       font=(fontName, 15))
        thirdHeightLabel, thirdHeightInput = tk.Label(frameHeight, text="Height on c: ", bd=5, bg='#DDDDDD',
                                                      font=(fontName, 15)), tk.Entry(frameHeight, bd=5, bg="#FFFFFF",
                                                                                     font=(fontName, 15))

        firstHeightLabel.grid(column=0, row=0, pady=15)
        firstHeightInput.grid(column=1, row=0, padx=5, pady=15)
        secondHeightLabel.grid(column=0, row=1, pady=15)
        secondHeightInput.grid(column=1, row=1, padx=5, pady=15)
        thirdHeightLabel.grid(column=0, row=2, pady=15)
        thirdHeightInput.grid(column=1, row=2, padx=5, pady=15)

        areaLabel, areaInput = tk.Label(frameAreas, text="Area: ", bd=5, bg='#DDDDDD', font=(fontName, 15)), tk.Entry(frameAreas, bd=5, bg="#FFFFFF", font=(fontName, 15))
        perimeterLabel, perimeterInput = tk.Label(frameAreas, text="Perimeter: ", bd=5, bg='#DDDDDD',
                                                  font=(fontName, 15)), tk.Entry(frameAreas, bd=5, bg="#FFFFFF",
                                                                                 font=(fontName, 15))

        areaLabel.grid(column=0, row=0, pady=15)
        areaInput.grid(column=1, row=0, padx=5, pady=15)
        perimeterLabel.grid(column=0, row=1, pady=15)
        perimeterInput.grid(column=1, row=1, padx=5, pady=15)

        alphaLabel, alphaInput = tk.Label(frameAngles, text="Alpha angle: ", bd=5, bg='#DDDDDD',
                                          font=(fontName, 15)), tk.Entry(frameAngles, name="alphaInput", bd=5,bg="#FFFFFF", font=(fontName, 15),state="disabled")
        betaLabel, betaInput = tk.Label(frameAngles, text="Beta angle: ", bd=5, bg='#DDDDDD',
                                        font=(fontName, 15)), tk.Entry(frameAngles, bd=5, bg="#FFFFFF",font=(fontName, 15), state="disabled")
        gammaLabel, gammaInput = tk.Label(frameAngles, text="Gamma angle: ", bd=5, bg='#DDDDDD',
                                          font=(fontName, 15)), tk.Entry(frameAngles, bd=5, bg="#FFFFFF",font=(fontName, 15), state="disabled")

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
            top.title('Triangle diagram')

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

                    if b<0 or c<0:
                        warningWithDelete()
                        return 0
                    elif b > c:
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
                    elif a > c:
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

                if a < 0 or b < 0 or c < 0:
                    warningWithDelete()
                    return 0
                elif (b > c) or (a > c):
                    warningWithDelete("C must be greater than b.")
                    return 0

                if (a ** 2 + b ** 2 != c ** 2):
                    warningWithDelete()
                    return 0

                s = a * b / 2
                p = a + b + c
                h = 2 * s / c

                alpha = math.atan(a / b) * (180 / math.pi)
                beta = 90 - alpha

            deleteAllValues()
            firstSideInput.insert(0, str(round(a, 13)))
            secondSideInput.insert(0, str(round(b, 13)))
            thirdSideInput.insert(0, str(round(c, 13)))

            perimeterInput.insert(0, str(round(p, 13)))

            areaInput.insert(0, str(round(s, 13)))

            heightInput.insert(0, str(round(h, 13)))

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
                        warningWithDelete()
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
                    if hVal == "":
                        r = 2 * s / p
                        rR = (s - r ** 2) / (2 * r)

                        c = rR * 2

                        a = 0.5 * (c + 2 * r + math.sqrt(c ** 2 - 4 * c * r - 4 * r ** 2))
                        b = math.sqrt(c ** 2 - a ** 2)

                        threeSidesCalc(a, b, c)
                    else:
                        warningWithDelete("Not enough information given")
            except:
                warningWithDelete()

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
                return 0

        def deleteAllValues():
            inputs_to_clear = [firstSideInput, secondSideInput, thirdSideInput, perimeterInput, areaInput, heightInput]
            inputs_to_enable_disable = [alphaInput, betaInput]

            for entry in inputs_to_clear:
                entry.delete(0, tk.END)

            for entry in inputs_to_enable_disable:
                entry.configure(state="normal")
                entry.delete(0, tk.END)
                entry.configure(state="disabled")

        buttonBack, buttonCalc, buttonTrash = (
            tk.Button(frameTriangleDiagram, text="Go back", font=(fontName, 15), command=lambda: chooseShape(2)),
            tk.Button(frameTriangleDiagram, text="Calculate", font=(fontName, 15), command=lambda: calculateTriangle()),
            tk.Button(frameTriangleDiagram, text="Delete all values", font=(fontName, 15),
                      command=lambda: deleteAllValues())
        )
        buttonBack.grid(column=0, row=0, padx=5, pady=5)
        buttonCalc.grid(column=1, row=0, padx=5, pady=5)
        buttonTrash.grid(column=2, row=0, padx=5, pady=5)

        firstSideLabel, firstSideInput = tk.Label(frameSides, text="Side a: ", bd=5, bg='#DDDDDD',
                                                  font=(fontName, 15)), tk.Entry(frameSides, bd=5, bg="#FFFFFF",font=(fontName, 15))
        secondSideLabel, secondSideInput = tk.Label(frameSides, text="Side b: ", bd=5, bg='#DDDDDD',
                                                    font=(fontName, 15)), tk.Entry(frameSides, bd=5, bg="#FFFFFF",font=(fontName, 15))
        thirdSideLabel, thirdSideInput = tk.Label(frameSides, text="Side c: ", bd=5, bg='#DDDDDD',
                                                  font=(fontName, 15)), tk.Entry(frameSides, bd=5, bg="#FFFFFF",font=(fontName, 15))

        firstSideLabel.grid(column=0, row=0, pady=15)
        firstSideInput.grid(column=1, row=0, padx=5, pady=15)
        secondSideLabel.grid(column=0, row=1, pady=15)
        secondSideInput.grid(column=1, row=1, padx=5, pady=15)
        thirdSideLabel.grid(column=0, row=2, pady=15)
        thirdSideInput.grid(column=1, row=2, padx=5, pady=15)

        firstHeightLabel, heightInput = tk.Label(frameHeight, text="Height on c: ", bd=5, bg='#DDDDDD', font=(fontName, 15)), tk.Entry(frameHeight, bd=5, bg="#FFFFFF", font=(fontName, 15))


        firstHeightLabel.grid(column=0, row=0, pady=15)
        heightInput.grid(column=1, row=0, padx=5, pady=15)

        areaLabel, areaInput, perimeterLabel, perimeterInput = tk.Label(frameAreas, text="Area: ", bd=5, bg='#DDDDDD', font=(fontName, 15)), tk.Entry(frameAreas, bd=5, bg="#FFFFFF", font=(fontName, 15)), tk.Label(frameAreas, text="Perimeter: ", bd=5, bg='#DDDDDD', font=(fontName, 15)), tk.Entry(frameAreas, bd=5, bg="#FFFFFF", font=(fontName, 15))


        areaLabel.grid(column=0, row=0, pady=15)
        areaInput.grid(column=1, row=0, padx=5, pady=15)
        perimeterLabel.grid(column=0, row=1, pady=15)
        perimeterInput.grid(column=1, row=1, padx=5, pady=15)

        alphaLabel, alphaInput = tk.Label(frameAngles, text="Alpha angle: ", bd=5, bg='#DDDDDD',
                                          font=(fontName, 15)), tk.Entry(frameAngles, name="alphaInput", bd=5,bg="#FFFFFF", font=(fontName, 15),state="disabled")
        betaLabel, betaInput = tk.Label(frameAngles, text="Beta angle: ", bd=5, bg='#DDDDDD',
                                        font=(fontName, 15)), tk.Entry(frameAngles, bd=5, bg="#FFFFFF",font=(fontName, 15), state="disabled")
        gammaLabel, gammaInput = tk.Label(frameAngles, text="Gamma angle: ", bd=5, bg='#DDDDDD',
                                          font=(fontName, 15)), tk.Entry(frameAngles, bd=5, bg="#FFFFFF",font=(fontName, 15), state="disabled")

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
            top.title('Triangle diagram')
            polygon1 = Polygon([(0, 0), (a, 0), (a/2, h1)])

            fig, ax = plt.subplots(1, 1)

            ax.add_patch(polygon1)
            plt.ylim(0, h1)
            plt.xlim(0, a)
            ax.set_aspect('equal', adjustable='box')
            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)

        def twoSidesCalc(a, b):
            if a + b > b and b + b > a:
                p = a + 2 * b
                halfP = p / 2
                s = math.sqrt(halfP * (halfP - a) * (halfP - b) * (halfP - b))
                h1 = s * 2 / a
                h2 = s * 2 / b
                alpha = math.acos(((b ** 2) + (b ** 2) - (a ** 2)) / (2 * b * b)) * (180.0 / math.pi)
                beta = math.acos(((a ** 2) + (b ** 2) - (b ** 2)) / (2 * a * b)) * (180.0 / math.pi)

                deleteAllValues()

                firstSideInput.insert(0, str(round(a, 13)))
                secondSideInput.insert(0, str(round(b, 13)))
                perimeterInput.insert(0, str(round(p, 13)))
                areaInput.insert(0, str(round(s, 13)))
                firstHeightInput.insert(0, str(round(h1, 13)))
                secondHeightInput.insert(0, str(round(h2, 13)))

                alphaInput.configure(state="normal")
                betaInput.configure(state="normal")
                alphaInput.insert(0, str(alpha))
                betaInput.insert(0, str(beta))
                alphaInput.configure(state="disabled")
                betaInput.configure(state="disabled")
                diagramWindow(a, h1)

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
                            if a < 0 or p < 0:
                                warningWithDelete()
                            b = (p-a)/2
                            twoSidesCalc(a, b)
                        elif bVal!="":
                            if b < 0 or p < 0:
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

        buttonBack, buttonCalc, buttonTrash = (
            tk.Button(frameTriangleDiagram, text="Go back", font=(fontName, 15), command=lambda: chooseShape(2)),
            tk.Button(frameTriangleDiagram, text="Calculate", font=(fontName, 15), command=lambda: calculateTriangle()),
            tk.Button(frameTriangleDiagram, text="Delete all values", font=(fontName, 15),
                      command=lambda: deleteAllValues())
        )
        buttonBack.grid(column=0, row=0, padx=5, pady=5)
        buttonCalc.grid(column=1, row=0, padx=5, pady=5)
        buttonTrash.grid(column=2, row=0, padx=5, pady=5)

        firstSideLabel, firstSideInput = tk.Label(frameSides, text="Side a: ", bd=5, bg='#DDDDDD',
                                                  font=(fontName, 15)), tk.Entry(frameSides, bd=5, bg="#FFFFFF",font=(fontName, 15))
        secondSideLabel, secondSideInput = tk.Label(frameSides, text="Side b (two sides): ", bd=5, bg='#DDDDDD',
                                                    font=(fontName, 15)), tk.Entry(frameSides, bd=5, bg="#FFFFFF",font=(fontName, 15))

        firstSideLabel.grid(column=0, row=0, pady=15)
        firstSideInput.grid(column=1, row=0, padx=5, pady=15)
        secondSideLabel.grid(column=0, row=1, pady=15)
        secondSideInput.grid(column=1, row=1, padx=5, pady=15)

        firstHeightLabel, firstHeightInput = tk.Label(frameHeight, text="Height on a: ", bd=5, bg='#DDDDDD',
                                                      font=(fontName, 15)), tk.Entry(frameHeight, bd=5, bg="#FFFFFF",font=(fontName, 15))
        secondHeightLabel, secondHeightInput = tk.Label(frameHeight, text="Height on b: ", bd=5, bg='#DDDDDD',
                                                        font=(fontName, 15)), tk.Entry(frameHeight, bd=5, bg="#FFFFFF",font=(fontName, 15))

        firstHeightLabel.grid(column=0, row=0, pady=15)
        firstHeightInput.grid(column=1, row=0, padx=5, pady=15)
        secondHeightLabel.grid(column=0, row=1, pady=15)
        secondHeightInput.grid(column=1, row=1, padx=5, pady=15)

        areaLabel, areaInput = tk.Label(frameAreas, text="Area: ", bd=5, bg='#DDDDDD', font=(fontName, 15)), tk.Entry(frameAreas, bd=5, bg="#FFFFFF", font=(fontName, 15))
        perimeterLabel, perimeterInput = tk.Label(frameAreas, text="Perimeter: ", bd=5, bg='#DDDDDD', font=(fontName, 15)), tk.Entry(frameAreas, bd=5, bg="#FFFFFF",font=(fontName, 15))

        areaLabel.grid(column=0, row=0, pady=15)
        areaInput.grid(column=1, row=0, padx=5, pady=15)
        perimeterLabel.grid(column=0, row=1, pady=15)
        perimeterInput.grid(column=1, row=1, padx=5, pady=15)

        alphaLabel, alphaInput = tk.Label(frameAngles, text="Alpha angle: ", bd=5, bg='#DDDDDD',
                                          font=(fontName, 15)), tk.Entry(frameAngles, name="alphaInput", bd=5,bg="#FFFFFF", font=(fontName, 15),state="disabled")
        betaLabel, betaInput = tk.Label(frameAngles, text="Beta angle: ", bd=5, bg='#DDDDDD',
                                        font=(fontName, 15)), tk.Entry(frameAngles, bd=5, bg="#FFFFFF", font=(fontName, 15), state="disabled")

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
            top.title('Triangle diagram')

            polygon1 = Polygon([(0, 0), (a, 0), (a/2, h1)])

            fig, ax = plt.subplots(1, 1)

            ax.add_patch(polygon1)

            plt.ylim(0, h1)
            plt.xlim(0, a)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)

        def oneSideCalc(a):
            if a>0:
                p = 3*a
                h = a * math.sqrt(3) / 2
                s = a**2 * math.sqrt(3) / 4
                r = a * math.sqrt(3) / 6
                R = a * math.sqrt(3) / 3

                deleteAllValues()

                firstSideInput.insert(0, str(round(a, 13)))
                perimeterInput.insert(0, str(round(p, 13)))
                areaInput.insert(0, str(round(s, 13)))
                firstHeightInput.insert(0, str(round(h, 13)))
                inRadiusInput.insert(0, str(round(r, 13)))
                outRadiusInput.insert(0, str(round(R, 13)))

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

        def warningWithDelete(a = "There couldn't exist a square with such dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        def diagramWindow(a):
            top = Toplevel()
            top.title('Square diagram')

            polygon1 = Polygon([(0, 0), (a, 0), (a, a), (0, a)])

            fig, ax = plt.subplots(1, 1)

            ax.add_patch(polygon1)

            plt.xlim(0, a)
            plt.ylim(0, a)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)

        def oneSideCalc(a):
            if a > 0:
                p = 4 * a
                d = a * math.sqrt(2)
                s = a ** 2
                r = a / 2
                R = d / 2

                deleteAllValues()

                firstSideInput.insert(0, str(round(a, 13)))
                perimeterInput.insert(0, str(round(p, 13)))
                areaInput.insert(0, str(round(s, 13)))
                firstDiagonal.insert(0, str(round(d, 13)))
                inRadiusInput.insert(0, str(round(r, 13)))
                outRadiusInput.insert(0, str(round(R, 13)))

                diagramWindow(a)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateShape():
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
                               command=lambda: calculateShape()
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

        def warningWithDelete(a = "There couldn't exist a rectangle with such dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        def diagramWindow(a,b):
            top = Toplevel()
            top.title('Rectangle diagram')

            polygon1 = Polygon([(0, 0), (a, 0), (a, b), (0, b)])

            fig, ax = plt.subplots(1, 1)

            ax.add_patch(polygon1)

            plt.xlim(0, a)
            plt.ylim(0, b)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)

        def sideCalc(a, b):
            if a > 0 and b > 0:
                p = 2 * (a + b)
                d = math.sqrt(a**2 + b**2)
                s = a*b
                alpha = math.atan(b/a) * (180 / math.pi)
                beta = math.atan(a/b) * (180 / math.pi)

                deleteAllValues()

                firstSideInput.insert(0, str(round(a, 13)))
                secondSideInput.insert(0, str(round(b, 13)))
                perimeterInput.insert(0, str(round(p, 13)))
                areaInput.insert(0, str(round(s, 13)))
                firstDiagonal.insert(0, str(round(d, 13)))

                alphaInput.configure(state="normal")
                betaInput.configure(state="normal")

                alphaInput.insert(0, str(alpha))
                betaInput.insert(0, str(beta))

                alphaInput.configure(state="disabled")
                betaInput.configure(state="disabled")

                diagramWindow(a, b)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateShape():
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
                    if p < 0 or d < 0:
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
                               command=lambda: calculateShape()
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

        def warningWithDelete(a = "There couldn't exist a rhombus with such dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        def diagramWindow(a,h):
            top = Toplevel()
            top.title('Rhombus diagram')

            x = math.sqrt(a**2 - h**2)
            xlimit = a + x

            polygon1 = Polygon([(0, 0), (a, 0), (x+a, h), (x, h)])

            fig, ax = plt.subplots(1, 1)

            ax.add_patch(polygon1)

            plt.xlim(0, xlimit)
            plt.ylim(0, h)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)

        def sideCalc(a, h):
            if a > 0 and h > 0:
                p = 4 * a
                s = a*h
                alpha = math.asin(h/a)
                beta = 180 - alpha * (180 / math.pi)
                d1 = 2 * a * math.cos(alpha/2)
                d2 = 2 * a * math.sin(alpha/2)
                alpha = alpha * (180 / math.pi)

                deleteAllValues()

                firstSideInput.insert(0, str(round(a, 13)))
                firstHeightInput.insert(0, str(round(h, 13)))
                perimeterInput.insert(0, str(round(p, 13)))
                areaInput.insert(0, str(round(s, 13)))
                firstDiagonal.insert(0, str(round(d1, 13)))
                secondDiagonal.insert(0, str(round(d2, 13)))

                alphaInput.configure(state="normal")
                betaInput.configure(state="normal")

                alphaInput.insert(0, str(alpha))
                betaInput.insert(0, str(beta))

                alphaInput.configure(state="disabled")
                betaInput.configure(state="disabled")

                diagramWindow(a, h)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateShape():
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
                               command=lambda: calculateShape()
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
    elif shape == "circle":
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

        frameAreas = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAreas.columnconfigure(0, weight=1)
        frameAreas.columnconfigure(1, weight=1)
        frameAreas.rowconfigure(0, weight=1)
        frameAreas.rowconfigure(1, weight=1)

        frameMenu.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
        frameSides.grid(column=0, row=1, padx=15, pady=15)
        frameAreas.grid(column=0, row=2, padx=15, pady=15)

        def warningWithDelete(a = "There couldn't exist a circle with such dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        def diagramWindow(r):
            top = Toplevel()
            top.title('Circle diagram')

            circle = Circle((0, 0), r)


            fig, ax = plt.subplots(1, 1)
            ax.add_patch(circle)

            plt.xlim(-r, r)
            plt.ylim(-r, r)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)

        def radiusCalc(r):
            if r > 0:
                p = 2 * r * math.pi
                d = 2 * r
                s = r ** 2 * math.pi

                deleteAllValues()

                firstSideInput.insert(0, str(round(r, 13)))
                perimeterInput.insert(0, str(round(p, 13)))
                areaInput.insert(0, str(round(s, 13)))
                secondSideInput.insert(0, str(round(d, 13)))

                diagramWindow(r)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateShape():
            value = checkEnoughInformation()
            rVal = firstSideInput.get()
            if rVal != "":
                r = float(firstSideInput.get())
            sVal = areaInput.get()
            if sVal != "":
                s = float(areaInput.get())
            pVal = perimeterInput.get()
            if pVal != "":
                p = float(perimeterInput.get())
            dVal = secondSideInput.get()
            if dVal != "":
                d = float(secondSideInput.get())


            if value == 1:
                try:
                    if r<0:
                        warningWithDelete()
                    radiusCalc(r)
                except:
                    warningWithDelete()
            elif value == 2:
                try:
                    if d<0:
                        warningWithDelete()
                    r = d / 2
                    radiusCalc(r)
                except:
                    warningWithDelete()
            elif value == 3:
                try:
                    if s<0:
                        warningWithDelete()
                    r = math.sqrt(s/math.pi)
                    radiusCalc(r)
                except:
                    warningWithDelete()
            elif value == 4:
                try:
                    if p<0:
                        warningWithDelete()
                    r = p / (2*math.pi)
                    radiusCalc(r)
                except:
                    warningWithDelete()
            else:
                warningWithDelete("Not enough information")


        def checkEnoughInformation():
            r = firstSideInput.get()
            d = secondSideInput.get()
            s = areaInput.get()
            p = perimeterInput.get()

            if r!="":
                return 1
            elif d!="":
                return 2
            elif s!="":
                return 3
            elif p!="":
                return 4
            else:
                return 0

        def deleteAllValues():
            firstSideInput.delete(0, tk.END)
            perimeterInput.delete(0, tk.END)
            areaInput.delete(0, tk.END)
            secondSideInput.delete(0, tk.END)


        buttonBack = tk.Button(frameMenu,
                               text="Go back",
                               font=(fontName, 15),
                               command=lambda: chooseShape(2)
                               )
        buttonCalc = tk.Button(frameMenu,
                               text="Calculate",
                               font=(fontName, 15),
                               command=lambda: calculateShape()
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
                                  text="Radius: ",
                                  bd=5,
                                  bg='#DDDDDD',
                                  font=(fontName, 15),
                                  )
        firstSideInput = tk.Entry(frameSides,
                                  bd=5,
                                  bg="#FFFFFF",
                                  font=(fontName, 15),
                                  )
        diameterLabel = tk.Label(frameSides,
                                  text="Diameter: ",
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
        diameterLabel.grid(column=0, row=1, pady=15)
        secondSideInput.grid(column=1, row=1, padx=5, pady=15)

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
    elif shape == "ellipse":
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

        frameAreas = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAreas.columnconfigure(0, weight=1)
        frameAreas.columnconfigure(1, weight=1)
        frameAreas.rowconfigure(0, weight=1)
        frameAreas.rowconfigure(1, weight=1)

        frameMenu.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
        frameSides.grid(column=0, row=1, padx=15, pady=15)
        frameAreas.grid(column=0, row=2, padx=15, pady=15)

        def warningWithDelete(a = "There couldn't exist a ellipse with such dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        def diagramWindow(a, b):
            top = Toplevel()
            top.title('Ellipse diagram')

            ellipse = Ellipse((0, 0), 2*a, 2*b)


            fig, ax = plt.subplots(1, 1)
            ax.add_patch(ellipse)

            plt.xlim(-a, a)
            plt.ylim(-b, b)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)

        def sidesCalc(a,b):
            if a > 0 and b > 0:
                p = math.pi * (3*(a+b)/2 - math.sqrt(a*b))
                s = a * b * math.pi

                deleteAllValues()

                firstSideInput.insert(0, str(round(a, 13)))
                secondSideInput.insert(0, str(round(b, 13)))

                perimeterInput.configure(state="normal")
                perimeterInput.insert(0, str(round(p, 13)))
                perimeterInput.configure(state="disabled")

                areaInput.insert(0, str(round(s, 13)))


                diagramWindow(a,b)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateShape():
            value = checkEnoughInformation()
            aVal = firstSideInput.get()
            if aVal != "":
                a = float(firstSideInput.get())
            sVal = areaInput.get()
            if sVal != "":
                s = float(areaInput.get())
            bVal = secondSideInput.get()
            if bVal != "":
                b = float(secondSideInput.get())


            if value == 1:
                try:
                    if a<0 or b<0:
                        warningWithDelete()
                    sidesCalc(a,b)
                except:
                    warningWithDelete()
            elif value == 2:
                try:
                    if a<0 or s<0:
                        warningWithDelete()
                    b = s/(math.pi * a)
                    sidesCalc(a,b)
                except:
                    warningWithDelete()
            elif value == 3:
                try:
                    if b<0 or s<0:
                        warningWithDelete()
                    a = s / (math.pi * b)
                    sidesCalc(a, b)
                except:
                    warningWithDelete()
            else:
                warningWithDelete("Not enough information")


        def checkEnoughInformation():
            a = firstSideInput.get()
            b = secondSideInput.get()
            s = areaInput.get()

            if a!="" and b!="":
                return 1
            elif a!="" and s!="":
                return 2
            elif b!="" and s!="":
                return 3
            else:
                return 0

        def deleteAllValues():
            firstSideInput.delete(0, tk.END)
            perimeterInput.configure(state="normal")
            perimeterInput.delete(0, tk.END)
            perimeterInput.configure(state="disabled")
            areaInput.delete(0, tk.END)
            secondSideInput.delete(0, tk.END)


        buttonBack = tk.Button(frameMenu,
                               text="Go back",
                               font=(fontName, 15),
                               command=lambda: chooseShape(2)
                               )
        buttonCalc = tk.Button(frameMenu,
                               text="Calculate",
                               font=(fontName, 15),
                               command=lambda: calculateShape()
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
                                  text="Semi-major axis: ",
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
                                  text="Semi-minor axis: ",
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

        perimeterInput.configure(state="disabled")
    elif shape == "polygon":
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

        frameAreas = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAreas.columnconfigure(0, weight=1)
        frameAreas.columnconfigure(1, weight=1)
        frameAreas.rowconfigure(0, weight=1)
        frameAreas.rowconfigure(1, weight=1)

        frameRadius = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameRadius.columnconfigure(0, weight=1)
        frameRadius.columnconfigure(1, weight=1)
        frameRadius.rowconfigure(0, weight=1)
        frameRadius.rowconfigure(1, weight=1)

        frameAngles = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAngles.columnconfigure(0, weight=1)
        frameAngles.columnconfigure(1, weight=1)
        frameAngles.rowconfigure(0, weight=1)

        frameMenu.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
        frameSides.grid(column=0, row=1, padx=15, pady=15)
        frameRadius.grid(column=1, row=1, padx=15, pady=15)
        frameAreas.grid(column=0, row=2, padx=15, pady=15)
        frameAngles.grid(column=1, row=2, padx=15, pady=15)

        def warningWithDelete(a = "There couldn't exist a square with such dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        def diagramWindow(a):
            n = int(nSides)
            top = Toplevel()
            top.title(str(n) + '-sided regular polygon diagram')

            fig, ax = plt.subplots(1, 1)
            vertices = []
            i = 0
            # Calculate the coordinates of the vertices using a while loop
            while i < n:
                x = a * math.cos(2 * math.pi * i / n) + a
                y = a * math.sin(2 * math.pi * i / n) + a
                vertices.append((x, y))
                i += 1

            vertices.append(vertices[0])  # Connect the last vertex to the first to close the polygon

            polygon = Polygon(vertices)

            ax.add_patch(polygon)

            plt.xlim(0, 2*a)
            plt.ylim(0, 2*a)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)

        def oneSideCalc(a):
            n = int(nSides)
            if a > 0:
                p = a * n
                s = (n * a**2) / (4 * math.tan(math.pi / n))
                r = a / (2 * math.tan(math.pi / n))
                R = a / (2 * math.sin(math.pi / n))

                deleteAllValues()

                firstSideInput.insert(0, str(round(a, 13)))
                perimeterInput.insert(0, str(round(p, 13)))
                areaInput.insert(0, str(round(s, 13)))
                inRadiusInput.insert(0, str(round(r, 13)))
                outRadiusInput.insert(0, str(round(R, 13)))

                diagramWindow(a)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateShape():
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
            rVal = inRadiusInput.get()
            if rVal != "":
                r = float(inRadiusInput.get())
            RVal = outRadiusInput.get()
            if RVal != "":
                R = float(outRadiusInput.get())

            n = int(nSides)

            if value == 1:
                try:
                    if a<0:
                        warningWithDelete()
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 2:
                try:
                    if s<0:
                        warningWithDelete()
                    a = math.sqrt((4 * s * math.tan(math.pi / n)) / n)
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 3:
                try:
                    if p<0:
                        warningWithDelete()
                    a = p / n
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 4:
                try:
                    if r<0:
                        warningWithDelete()
                    a = 2 * r * math.sin(math.pi / n)
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 5:
                try:
                    if R<0:
                        warningWithDelete()
                    a = 2 * R * math.sin(math.pi / n)
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            else:
                warningWithDelete("Not enough information")


        def checkEnoughInformation():
            a = firstSideInput.get()
            s = areaInput.get()
            p = perimeterInput.get()
            r = inRadiusInput.get()
            R = outRadiusInput.get()

            if a!="":
                return 1
            elif s!="":
                return 2
            elif p!="":
                return 3
            elif r!="":
                return 4
            elif R!="":
                return 5
            else:
                return 0

        def deleteAllValues():
            firstSideInput.delete(0, tk.END)
            perimeterInput.delete(0, tk.END)
            areaInput.delete(0, tk.END)
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
                               command=lambda: calculateShape()
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

        inRadiusLabel = tk.Label(frameRadius,
                             text="In-radius: ",
                             bd=5,
                             bg='#DDDDDD',
                             font=(fontName, 15),
                             )
        inRadiusInput = tk.Entry(frameRadius,
                             bd=5,
                             bg="#FFFFFF",
                             font=(fontName, 15),
                             )

        outRadiusLabel = tk.Label(frameRadius,
                                  text="Out-radius: ",
                                  bd=5,
                                  bg='#DDDDDD',
                                  font=(fontName, 15),
                                  )
        outRadiusInput = tk.Entry(frameRadius,
                                  bd=5,
                                  bg="#FFFFFF",
                                  font=(fontName, 15),
                                  )

        inRadiusLabel.grid(column=0, row=0, pady=15)
        inRadiusInput.grid(column=1, row=0, padx=5, pady=15)
        outRadiusLabel.grid(column=0, row=1, pady=15)
        outRadiusInput.grid(column=1, row=1, padx=5, pady=15)

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

        if int(nSides)<=4:
            warningWithDelete("Please input proper number of sides, which is more than 4")
            chooseShape(2)
            return 0

        alphaInput.configure(state="normal")
        alphaInput.insert(0, str((int(nSides) - 2) * 180 / int(nSides)))
        alphaInput.configure(state="disabled")
    elif shape == "sphere":
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

        frameAreas = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAreas.columnconfigure(0, weight=1)
        frameAreas.columnconfigure(1, weight=1)
        frameAreas.rowconfigure(0, weight=1)
        frameAreas.rowconfigure(1, weight=1)
        frameAreas.rowconfigure(2, weight=1)
        frameAreas.rowconfigure(3, weight=1)

        frameMenu.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
        frameSides.grid(column=0, row=1, padx=15, pady=15)
        frameAreas.grid(column=0, row=2, padx=15, pady=15)

        def warningWithDelete(a = "There couldn't exist a circle with such dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)
            return 0

        def diagramWindow(r):
            top = Toplevel()
            top.title('Circle diagram')

            circle = Circle((0, 0), r)


            fig, ax = plt.subplots(1, 1)
            ax.add_patch(circle)

            plt.xlim(-r, r)
            plt.ylim(-r, r)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)

        def radiusCalc(r):
            if r > 0:
                p = 2 * r * math.pi
                d = 2 * r
                sC = r ** 2 * math.pi
                s = 4 * math.pi * (r ** 2)
                v = 4/3 * math.pi * (r ** 3)

                deleteAllValues()

                firstSideInput.insert(0, str(round(r, 13)))
                perimeterInput.insert(0, str(round(p, 13)))
                areaInput.insert(0, str(round(s, 13)))
                areaCircleInput.insert(0, str(round(sC, 13)))
                secondSideInput.insert(0, str(round(d, 13)))
                volumeInput.insert(0, str(round(v, 13)))

                diagramWindow(r)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateShape():
            value = checkEnoughInformation()
            rVal = firstSideInput.get()
            if rVal != "":
                r = float(firstSideInput.get())
            sVal = areaInput.get()
            if sVal != "":
                s = float(areaInput.get())
            pVal = perimeterInput.get()
            if pVal != "":
                p = float(perimeterInput.get())
            dVal = secondSideInput.get()
            if dVal != "":
                d = float(secondSideInput.get())
            sCVal = areaCircleInput.get()
            if sCVal != "":
                sC = float(areaCircleInput.get())
            vVal = volumeInput.get()
            if vVal != "":
                v = float(volumeInput.get())


            if value == 1:
                try:
                    if r<0:
                        warningWithDelete()
                    radiusCalc(r)
                except:
                    warningWithDelete()
            elif value == 2:
                try:
                    if d<0:
                        warningWithDelete()
                    r = d / 2
                    radiusCalc(r)
                except:
                    warningWithDelete()
            elif value == 3:
                try:
                    if s<0:
                        warningWithDelete()
                    r = math.sqrt(s/(4 * math.pi))
                    radiusCalc(r)
                except:
                    warningWithDelete()
            elif value == 4:
                try:
                    if p<0:
                        warningWithDelete()
                    r = p / (2*math.pi)
                    radiusCalc(r)
                except:
                    warningWithDelete()
            elif value == 5:
                try:
                    if v<0:
                        warningWithDelete()
                    r = math.pow((3 * v)/(4 * math.pi), 1/3)
                    radiusCalc(r)
                except:
                    warningWithDelete()
            elif value == 6:
                try:
                    if sC<0:
                        warningWithDelete()
                    r = math.sqrt(sC/(math.pi))
                    radiusCalc(r)
                except:
                    warningWithDelete()
            else:
                warningWithDelete("Not enough information")


        def checkEnoughInformation():
            r = firstSideInput.get()
            d = secondSideInput.get()
            s = areaInput.get()
            p = perimeterInput.get()
            v = volumeInput.get()
            sC = areaCircleInput.get()

            if r!="":
                return 1
            elif d!="":
                return 2
            elif s!="":
                return 3
            elif p!="":
                return 4
            elif v!="":
                return 5
            elif sC!="":
                return 6
            else:
                return 0

        def deleteAllValues():
            firstSideInput.delete(0, tk.END)
            perimeterInput.delete(0, tk.END)
            areaInput.delete(0, tk.END)
            secondSideInput.delete(0, tk.END)
            volumeInput.delete(0, tk.END)
            areaCircleInput.delete(0, tk.END)


        buttonBack = tk.Button(frameMenu,
                               text="Go back",
                               font=(fontName, 15),
                               command=lambda: chooseShape(3)
                               )
        buttonCalc = tk.Button(frameMenu,
                               text="Calculate",
                               font=(fontName, 15),
                               command=lambda: calculateShape()
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
                                  text="Radius: ",
                                  bd=5,
                                  bg='#DDDDDD',
                                  font=(fontName, 15),
                                  )
        firstSideInput = tk.Entry(frameSides,
                                  bd=5,
                                  bg="#FFFFFF",
                                  font=(fontName, 15),
                                  )
        diameterLabel = tk.Label(frameSides,
                                  text="Diameter: ",
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
        diameterLabel.grid(column=0, row=1, pady=15)
        secondSideInput.grid(column=1, row=1, padx=5, pady=15)

        volumeLabel = tk.Label(frameAreas,
                             text="Volume: ",
                             bd=5,
                             bg='#DDDDDD',
                             font=(fontName, 15),
                             )
        volumeInput = tk.Entry(frameAreas,
                             bd=5,
                             bg="#FFFFFF",
                             font=(fontName, 15),
                             )

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

        areaCircleLabel = tk.Label(frameAreas,
                             text="Area of the circle: ",
                             bd=5,
                             bg='#DDDDDD',
                             font=(fontName, 15),
                             )
        areaCircleInput = tk.Entry(frameAreas,
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

        volumeLabel.grid(column=0, row=0, pady=15)
        volumeInput.grid(column=1, row=0, padx=5, pady=15)
        areaLabel.grid(column=0, row=1, pady=15)
        areaInput.grid(column=1, row=1, padx=5, pady=15)
        areaCircleLabel.grid(column=0, row=2, pady=15)
        areaCircleInput.grid(column=1, row=2, padx=5, pady=15)
        perimeterLabel.grid(column=0, row=3, pady=15)
        perimeterInput.grid(column=1, row=3, padx=5, pady=15)
    elif shape == "cube":
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

        frameAreas = Frame(window, width=500, height=300, bg='#DDDDDD')

        frameAreas.columnconfigure(0, weight=1)
        frameAreas.columnconfigure(1, weight=1)
        frameAreas.rowconfigure(0, weight=1)
        frameAreas.rowconfigure(1, weight=1)
        frameAreas.rowconfigure(2, weight=1)
        frameAreas.rowconfigure(3, weight=1)


        frameMenu.grid(column=0, columnspan=2, row=0, padx=15, pady=15)
        frameSides.grid(column=0, row=1, padx=15, pady=15)
        frameOthers.grid(column=1, row=1, padx=15, pady=15)
        frameAreas.grid(column=0, row=2, columnspan=2, padx=15, pady=15)

        def warningWithDelete(a = "There couldn't exist a cube with such dimensions"):
            deleteAllValues()
            messagebox.showwarning("Error with calculations",
                                   a)

        def diagramWindow(a):
            top = Toplevel()
            top.title('Square diagram')

            polygon1 = Polygon([(0, 0), (a, 0), (a, a), (0, a)])

            fig, ax = plt.subplots(1, 1)

            ax.add_patch(polygon1)

            plt.xlim(0, a)
            plt.ylim(0, a)
            ax.set_aspect('equal', adjustable='box')

            canvas = FigureCanvasTkAgg(fig, master=top)
            canvas.get_tk_widget().grid(row=0, column=0)

        def oneSideCalc(a):
            if a > 0:
                p = 4 * a
                d = a * math.sqrt(3)
                dF = a * math.sqrt(2)
                sF = a ** 2
                s = sF * 6
                v = a ** 3

                deleteAllValues()

                firstSideInput.insert(0, str(round(a, 13)))
                perimeterInput.insert(0, str(round(p, 13)))
                areaInput.insert(0, str(round(s, 13)))
                diagonalInput.insert(0, str(round(d, 13)))
                faceDiagonalInput.insert(0, str(round(dF, 13)))
                areaFaceInput.insert(0, str(round(sF, 13)))
                volumeInput.insert(0, str(round(v, 13)))

                diagramWindow(a)
            else:
                deleteAllValues()
                messagebox.showwarning("Error with calculations",
                                       "There couldn't exist a triangle with such dimensions")

        def calculateShape():
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
            dVal = diagonalInput.get()
            if dVal != "":
                d = float(diagonalInput.get())
            dFVal = faceDiagonalInput.get()
            if dFVal != "":
                dF = float(faceDiagonalInput.get())
            vVal = volumeInput.get()
            if vVal != "":
                v = float(volumeInput.get())
            sFVal = areaFaceInput.get()
            if sFVal != "":
                sF = float(areaFaceInput.get())

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
                    a = d*math.sqrt(3)/3
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 3:
                try:
                    if dF<0:
                        warningWithDelete()
                    a = dF*math.sqrt(2)/2
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 4:
                try:
                    if v<0:
                        warningWithDelete()
                    a = math.pow(v, 1/3)
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            elif value == 5:
                try:
                    if s < 0:
                        warningWithDelete()
                    a = math.sqrt(s/6)
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
            elif value == 7:
                try:
                    if sF<0:
                        warningWithDelete()
                    a = math.sqrt(sF)
                    oneSideCalc(a)
                except:
                    warningWithDelete()
            else:
                warningWithDelete("Not enough information")


        def checkEnoughInformation():
            a = firstSideInput.get()
            d = diagonalInput.get()
            dF = faceDiagonalInput.get()
            v = volumeInput.get()
            s = areaInput.get()
            p = perimeterInput.get()
            sF = areaFaceInput.get()


            if a!="":
                return 1
            elif d!="":
                return 2
            elif dF!="":
                return 3
            elif v!="":
                return 4
            elif s!="":
                return 5
            elif p!="":
                return 6
            elif sF!="":
                return 7
            else:
                return 0

        def deleteAllValues():
            firstSideInput.delete(0, tk.END)
            perimeterInput.delete(0, tk.END)
            volumeInput.delete(0, tk.END)
            areaInput.delete(0, tk.END)
            areaFaceInput.delete(0, tk.END)
            diagonalInput.delete(0, tk.END)
            faceDiagonalInput.delete(0, tk.END)


        buttonBack = tk.Button(frameMenu,
                               text="Go back",
                               font=(fontName, 15),
                               command=lambda: chooseShape(3)
                               )
        buttonCalc = tk.Button(frameMenu,
                               text="Calculate",
                               font=(fontName, 15),
                               command=lambda: calculateShape()
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
                                  text="Edge: ",
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

        diagonalLabel = tk.Label(frameOthers,
                                    text="Space diagonal: ",
                                    bd=5,
                                    bg='#DDDDDD',
                                    font=(fontName, 15),
                                    )
        diagonalInput = tk.Entry(frameOthers,
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 15),
                                    )
        faceDiagonalLabel = tk.Label(frameOthers,
                                    text="Face diagonal: ",
                                    bd=5,
                                    bg='#DDDDDD',
                                    font=(fontName, 15),
                                    )
        faceDiagonalInput = tk.Entry(frameOthers,
                                    bd=5,
                                    bg="#FFFFFF",
                                    font=(fontName, 15),
                                    )



        diagonalLabel.grid(column=0, row=0, pady=15)
        diagonalInput.grid(column=1, row=0, padx=5, pady=15)
        faceDiagonalLabel.grid(column=0, row=1, pady=15)
        faceDiagonalInput.grid(column=1, row=1, padx=5, pady=15)

        volumeLabel = tk.Label(frameAreas,
                             text="Volume: ",
                             bd=5,
                             bg='#DDDDDD',
                             font=(fontName, 15),
                             )
        volumeInput = tk.Entry(frameAreas,
                             bd=5,
                             bg="#FFFFFF",
                             font=(fontName, 15),
                             )

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
        areaFaceLabel = tk.Label(frameAreas,
                             text="Area of a face: ",
                             bd=5,
                             bg='#DDDDDD',
                             font=(fontName, 15),
                             )
        areaFaceInput = tk.Entry(frameAreas,
                             bd=5,
                             bg="#FFFFFF",
                             font=(fontName, 15),
                             )

        perimeterLabel = tk.Label(frameAreas,
                                  text="Perimeter of face: ",
                                  bd=5,
                                  bg='#DDDDDD',
                                  font=(fontName, 15),
                                  )
        perimeterInput = tk.Entry(frameAreas,
                                  bd=5,
                                  bg="#FFFFFF",
                                  font=(fontName, 15),
                                  )

        volumeLabel.grid(column=0, row=0, pady=15)
        volumeInput.grid(column=1, row=0, padx=5, pady=15)
        areaLabel.grid(column=0, row=1, pady=15)
        areaInput.grid(column=1, row=1, padx=5, pady=15)
        areaFaceLabel.grid(column=0, row=2, pady=15)
        areaFaceInput.grid(column=1, row=2, padx=5, pady=15)
        perimeterLabel.grid(column=0, row=3, pady=15)
        perimeterInput.grid(column=1, row=3, padx=5, pady=15)

dimensions()
window.mainloop()