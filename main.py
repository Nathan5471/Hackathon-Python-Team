import tkinter as tk

def gradient(canvas, color1, color2, width):
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
    canvasHeight = canvas.winfo_height()
    for i in range(canvasHeight):
        r = r1 * (1 - (i / canvasHeight)) + r2 * (i / canvasHeight)
        g = g1 * (1 - (i / canvasHeight)) + g2 * (i / canvasHeight)
        b = b1 * (1 - (i / canvasHeight)) + b2 * (i / canvasHeight)
        color = '#%02x%02x%02x' % (round(r), round(g), round(b))
        canvas.create_line(0, i, width, i, fill=color)

def buttonColor(event, button, color):
    button.config(bg=color)
    
def usernameButtonPressed():
    if usernameMenu.winfo_ismapped():
        usernameMenu.place_forget()
    else:
        usernameMenu.place(x=0, y=50)

window = tk.Tk()
window.title("Elearning")
window.geometry("600x400")

#Creates the main page for the application
canvas = tk.Canvas(window, width=600, height=400)
canvas.place(x=0, y=0)

#The top bar for the application
topBar = tk.Canvas(window, width=600, height=50)
topBar.place(x=0, y=0)
usernameButton = tk.Button(topBar, text="Username", relief=tk.FLAT, width=10, height=1, background="#c1b4f2")
usernameButton.configure(activebackground="#c1b4f2", activeforeground="white")
usernameButton.bind("<Enter>", lambda event: buttonColor(event, usernameButton, "#dbd4f7"))
usernameButton.bind("<Leave>", lambda event: buttonColor(event, usernameButton, "#c1b4f2"))
usernameButton.place(x=0, y=0)

#The account management menu
#Accesed by pressing the username button
usernameMenu = tk.Canvas(window, width=100, height=100)
usernameMenu.place(x=0, y=50)

#Manages the gradients
window.update()  # needed for winfo_height() to work
gradient(canvas, '#D8B5FF', '#1EAE98', 600)
gradient(topBar, '#D8B5FF', '#c1b4f2', 600)

window.mainloop()