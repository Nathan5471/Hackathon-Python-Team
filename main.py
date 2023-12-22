import tkinter as tk

def gradient(canvas, color1, color2, width):
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
    for i in range(canvas.winfo_height()):
        r = r1 * (1 - (i / canvas.winfo_height())) + r2 * (i / canvas.winfo_height())
        g = g1 * (1 - (i / canvas.winfo_height())) + g2 * (i / canvas.winfo_height())
        b = b1 * (1 - (i / canvas.winfo_height())) + b2 * (i / canvas.winfo_height())
        color = '#%02x%02x%02x' % (round(r), round(g), round(b))
        canvas.create_line(0, i, width, i, fill=color)

window = tk.Tk()
window.title("Elearning")
window.geometry("600x400")

canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()

window.update()  # needed for winfo_height() to work
gradient(canvas, '#D8B5FF', '#1EAE98', 600)

window.mainloop()