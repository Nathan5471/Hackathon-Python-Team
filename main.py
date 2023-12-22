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

window = tk.Tk()
window.title("Elearning")
window.geometry("600x400")

canvas = tk.Canvas(window, width=600, height=400)
canvas.place(x=0, y=0)

topBar = tk.Frame(window, bg='#1EAE98', width=600, height=50)
topBar.place(x=0, y=0)

window.update()  # needed for winfo_height() to work
gradient(canvas, '#D8B5FF', '#1EAE98', 600)

window.mainloop()