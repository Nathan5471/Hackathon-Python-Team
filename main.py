import tkinter as tk
import accountSystem as asys
import courseSystem as csys

def gradient(canvas, color1, color2, width):
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
    canvasHeight = canvas.winfo_height()
    for i in range(canvasHeight):
        r = r1 * (1 - (i / canvasHeight)) + r2 * (i / canvasHeight)
        g = g1 * (1 - (i / canvasHeight)) + g2 * (i / canvasHeight)
        b = b1 * (1 - (i / canvasHeight)) + b2 * (i / canvasHeight)
        color = "#%02x%02x%02x" % (round(r), round(g), round(b))
        canvas.create_line(0, i, width, i, fill=color)


def buttonColor(event, button, color):
    button.config(bg=color)

def userLogin():
    loginStatus = asys.login(usernameEntry.get(), passwordEntry.get())
    print(loginStatus)

def usernameButtonPressed():
    if usernameMenu.winfo_ismapped():
        usernameMenu.place_forget()
    else:
        usernameMenu.place(x=0, y=50)
        

def loginButtonPressed():
    usernameMenu.place_forget()
    loginMenu.place(x=0, y=50)


window = tk.Tk()
window.title("Elearning")
window.geometry("600x400")

# Creates the main page for the application
canvas = tk.Canvas(window, width=600, height=400)
canvas.place(x=0, y=0)

# The top bar for the application
topBar = tk.Canvas(window, width=600, height=35)
topBar.place(x=0, y=0)
usernameButton = tk.Button(
    topBar,
    text="Username",
    relief=tk.FLAT,
    width=10,
    height=1,
    background="#c1b4f2",
    command=usernameButtonPressed,
)
usernameButton.configure(activebackground="#c1b4f2", activeforeground="white")
usernameButton.bind(
    "<Enter>", lambda event: buttonColor(event, usernameButton, "#dbd4f7")
)
usernameButton.bind(
    "<Leave>", lambda event: buttonColor(event, usernameButton, "#c1b4f2")
)
usernameButton.place(x=5, y=7)

# The account management menu
# Accesed by pressing the username button
usernameMenu = tk.Canvas(window, width=100, height=100)
loginButton = tk.Button(
    usernameMenu, text="Login", relief=tk.FLAT, width=10, height=1, background="#c1b4f2", command=loginButtonPressed
)
loginButton.configure(activebackground="#c1b4f2", activeforeground="white")
loginButton.bind("<Enter>", lambda event: buttonColor(event, loginButton, "#dbd4f7"))
loginButton.bind("<Leave>", lambda event: buttonColor(event, loginButton, "#c1b4f2"))
loginButton.place(x=0, y=0)
signupButton = tk.Button(
    usernameMenu,
    text="Signup",
    relief=tk.FLAT,
    width=10,
    height=1,
    background="#c1b4f2",
)
signupButton.configure(activebackground="#c1b4f2", activeforeground="white")
signupButton.bind("<Enter>", lambda event: buttonColor(event, signupButton, "#dbd4f7"))
signupButton.bind("<Leave>", lambda event: buttonColor(event, signupButton, "#c1b4f2"))
signupButton.place(x=0, y=25)

# The login menu
# Accessed by pressing the login button
loginMenu = tk.Canvas(canvas, width=100, height=120, background="#72b1c7")
usernameLabel = tk.Label(loginMenu, text="Username", background="#72b1c7", foreground="white")
usernameLabel.place(x=0, y=0)
usernameEntry = tk.Entry(loginMenu, background="#88bccf")
usernameEntry.place(x=0, y=20)
passwordLabel = tk.Label(loginMenu, text="Password", background="#72b1c7", foreground="white")
passwordLabel.place(x=0, y=50)
passwordEntry = tk.Entry(loginMenu, background="#88bccf")
passwordEntry.place(x=0, y=70)
userLoginButton = tk.Button(
    loginMenu, text="Login", relief=tk.FLAT, width=10, height=1, background="#72b1c7", foreground="White"
)
userLoginButton.configure(activebackground="#88bccf", activeforeground="white")
userLoginButton.bind("<Enter>", lambda event: buttonColor(event, userLoginButton, "#88bccf"))
userLoginButton.bind("<Leave>", lambda event: buttonColor(event, userLoginButton, "#72b1c7"))
userLoginButton.place(x=0, y=100)

# Manages the gradients
window.update()  # needed for winfo_height() to work
gradient(canvas, "#D8B5FF", "#1EAE98", 600)
gradient(topBar, "#D8B5FF", "#c1b4f2", 600)

window.mainloop()
