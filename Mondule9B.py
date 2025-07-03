import math
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

window = tk.Tk()
window.title("Learn Python GUI!")
window.geometry("800x600")

label = tk.Label(window, text="Welcome to Python", font=('Arial', 25))
label.pack(pady=20)

fig = Figure(figsize=(5, 5), dpi=100)

y = [math.sin(i / 4) for i in range(101)]

sub_plot = fig.add_subplot(111)
sub_plot.plot(y)

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas.get_tk_widget().pack


window.mainloop()

