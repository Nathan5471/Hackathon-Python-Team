import tkinter as tk

def gradient(canvas, color1, color2, width):
    for i in range(canvas.winfo_height()):
        color = (int(color1[1:3], 16) * (1 - (i / canvas.winfo_height())) + int(color2[1:3], 16) * (i / canvas.winfo_height()))
        color = round(color)
        color = '#%02x%02x%02x' % (color, color, color)
        canvas.create_line(0, i, width, i, fill=color)

window = tk.Tk()
window.title("Elearning")
window.geometry("600x400")

canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()

window.update()  # needed for winfo_height() to work
gradient(canvas, '#D8B5FF', '#1EAE98', 600)

window.mainloop()