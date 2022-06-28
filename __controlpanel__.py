import tkinter as tk

def sendvals():
    global getgravvals
    def getgravvals(gravval):
        return gravval
    global getfricvals
    def getfricvals(fricval):
        return fricval
    return [getgravvals(), getfricvals()]

def run():

    window = tk.Tk()

    window.title("Control Panel!")

    val1 = tk.Label(text = "Gravity")
    val1.pack()
    global gravityslider
    gravityslider = tk.Scale(window, from_ = 0, to_ = 30, orient = tk.HORIZONTAL, command = getgravvals)
    gravityslider.pack()

    val3 = tk.Label(text = "Friction")
    val3.pack()
    global frictionslider
    frictionslider = tk.Scale(window, from_ = 0, to_ = 10, orient = tk.HORIZONTAL, command = getfricvals)
    frictionslider.pack()
    window.mainloop()

    donebutton = tk.Button(window, text = "Apply")
    donebutton.pack()



