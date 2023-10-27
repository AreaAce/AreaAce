import tkinter as tk

window = tk.Tk()

fontName = "Arial"


def dimensions():
    for widget in window.winfo_children():
        widget.destroy()

    window.columnconfigure(0, weight=2)
    window.rowconfigure(1, weight=3)

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
        bg = "#FFFFFF",
        font = (fontName, 25, "bold"),
        command = lambda:chooseShape(2)
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
    threeDButton.grid(column=1,  row=2, padx=5, pady=5)


def chooseShape(n):
    print(n)


dimensions()
window.mainloop()
