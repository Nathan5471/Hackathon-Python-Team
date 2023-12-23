import tkinter as tk
import accountSystem as asys
import courseSystem as csys
from PIL import Image, ImageTk

username = ""
password = ""


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


def loop_check_password(password, password_entry, image_list):
    if password_entry.winfo_ismapped():
        if password == password_entry.get():
            pass
        else:
            password = password_entry.get()
            result = asys.checkPassword(password)
            # for i in range(5):
            # image =  if result[i] else
            # image_list[i].configure(image=image)
        # window.after(
        # 100,
        # lambda password=password, password_entry=password_entry, image_list=image_list: loop_check_password(
        # password, password_entry, image_list
        # ),
        # )


def userSignup():
    asys.createAccount()


def userLogin():
    username = usernameEntryLogin.get()
    password = passwordEntryLogin.get()
    loginStatus = asys.login(username, password)
    if loginStatus == True:
        loginMenu.place_forget()
        usernameMenu.place_forget()
        usernameButton.config(text=username)
        usernameButton.place(x=5, y=7)


def usernameButtonPressed():
    if usernameMenu.winfo_ismapped():
        usernameMenu.place_forget()
    else:
        usernameMenu.place(x=2, y=50)


def signupButtonPressed():
    usernameMenu.place_forget()
    canvas.place_forget()
    signupMenu.place(x=0, y=0)
    gradient(signupMenu, "#D8B5FF", "#1EAE98", 600)


def loginButtonPressed():
    usernameMenu.place_forget()
    loginMenu.place(x=2, y=50)


window = tk.Tk()
window.title("Elearning")
window.geometry("600x400")

# Creates the main page for the application
canvas = tk.Canvas(window, width=600, height=400)
canvas.place(x=0, y=0)

xImage = ImageTk.PhotoImage(Image.open("assets/xIcon.png").resize((10, 10)))
checkImage = ImageTk.PhotoImage(Image.open("assets/checkIcon.png").resize((10, 10)))

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
    foreground="white",
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
usernameMenu = tk.Canvas(window, width=100, height=100, background="#72b1c7")
loginButton = tk.Button(
    usernameMenu,
    text="Login",
    relief=tk.FLAT,
    width=10,
    height=1,
    background="#72b1c7",
    foreground="white",
    command=loginButtonPressed,
)
loginButton.configure(activebackground="#88bccf", activeforeground="white")
loginButton.bind("<Enter>", lambda event: buttonColor(event, loginButton, "#88bccf"))
loginButton.bind("<Leave>", lambda event: buttonColor(event, loginButton, "#72b1c7"))
loginButton.place(x=10, y=15)
signupButton = tk.Button(
    usernameMenu,
    text="Signup",
    relief=tk.FLAT,
    width=10,
    height=1,
    background="#72b1c7",
    foreground="white",
    command=signupButtonPressed,
)
signupButton.configure(activebackground="#88bccf", activeforeground="white")
signupButton.bind("<Enter>", lambda event: buttonColor(event, signupButton, "#88bccf"))
signupButton.bind("<Leave>", lambda event: buttonColor(event, signupButton, "#72b1c7"))
signupButton.place(x=10, y=55)

# The signup menu
# Accessed by pressing the signup button
signupMenu = tk.Canvas(window, width=600, height=400, background="#72b1c7")
usernameLabelCreate = tk.Label(
    signupMenu, text="Username", background="#72b1c7", font=("Arial", 20)
)
usernameLabelCreate.place(x=245, y=25)
usernameEntryCreate = tk.Entry(
    signupMenu, background="#88bccf", width=15, font=("Arial", 14)
)
usernameEntryCreate.place(x=225, y=65)
emailLabelCreate = tk.Label(
    signupMenu, text="Email", background="#72b1c7", font=("Arial", 20)
)
emailLabelCreate.place(x=265, y=100)
emailEntryCreate = tk.Entry(
    signupMenu, background="#88bccf", width=15, font=("Arial", 14)
)
emailEntryCreate.place(x=225, y=140)
passwordLabelCreate = tk.Label(
    signupMenu, text="Password", background="#72b1c7", font=("Arial", 20)
)
passwordLabelCreate.place(x=245, y=175)
passwordEntryCreate = tk.Entry(
    signupMenu, background="#88bccf", width=15, font=("Arial", 14)
)
passwordEntryCreate.place(x=225, y=215)
passwordRequirements = [
    "Minimum 8 characters",
    "At least 1 number",
    "At least 1 lowercase letter",
    "At least 1 uppercase letter",
    "At least 1 special character",
]
previousY = 250
passwordRequirementImageLabelList = []
for passwordRequirement in passwordRequirements:
    passwordRequirementLabel = tk.Label(
        signupMenu, text=passwordRequirement, background="#72b1c7", font=("Arial", 10)
    )
    passwordRequirementLabel.place(x=250, y=previousY)
    passwordRequirementImageLabel = tk.Label(signupMenu, image=xImage, background="#72b1c7")
    passwordRequirementImageLabelList.append(passwordRequirementImageLabel)
    i = len(passwordRequirementImageLabelList) - 1
    passwordRequirementImageLabelList[i].place(x=225, y=previousY)
    previousY += 20
userCreateButton = tk.Button(
    signupMenu,
    text="Create",
    relief=tk.FLAT,
    width=20,
    height=1,
    background="#72b1c7",
    foreground="white",
    font=("Arial", 10),
)
userCreateButton.configure(activebackground="#88bccf", activeforeground="white")
userCreateButton.bind(
    "<Enter>", lambda event: buttonColor(event, userCreateButton, "#88bccf")
)
userCreateButton.bind(
    "<Leave>", lambda event: buttonColor(event, userCreateButton, "#72b1c7")
)
userCreateButton.place(x=225, y=360)


# The login menu
# Accessed by pressing the login button
loginMenu = tk.Canvas(canvas, width=100, height=120, background="#72b1c7")
usernameLabelLogin = tk.Label(
    loginMenu,
    text="Username",
    background="#72b1c7",
    foreground="white",
)
usernameLabelLogin.place(x=5, y=3)
usernameEntryLogin = tk.Entry(loginMenu, background="#88bccf", width=15)
usernameEntryLogin.place(x=5, y=23)
passwordLabelLogin = tk.Label(
    loginMenu, text="Password", background="#72b1c7", foreground="white"
)
passwordLabelLogin.place(x=5, y=50)
passwordEntryLogin = tk.Entry(loginMenu, background="#88bccf", width=15)
passwordEntryLogin.place(x=5, y=70)
userLoginButtonLogin = tk.Button(
    loginMenu,
    text="Login",
    relief=tk.FLAT,
    width=10,
    height=1,
    background="#72b1c7",
    foreground="white",
)
userLoginButtonLogin.configure(activebackground="#88bccf", activeforeground="white")
userLoginButtonLogin.bind(
    "<Enter>", lambda event: buttonColor(event, userLoginButtonLogin, "#88bccf")
)
userLoginButtonLogin.bind(
    "<Leave>", lambda event: buttonColor(event, userLoginButtonLogin, "#72b1c7")
)
userLoginButtonLogin.place(x=12, y=93)

# Manages the gradients
window.update()  # needed for winfo_height() to work
gradient(canvas, "#D8B5FF", "#1EAE98", 600)
gradient(topBar, "#D8B5FF", "#c1b4f2", 600)


window.mainloop()
