import tkinter as tk

window = tk.Tk()

window.title("Learn Python GUI")
window.geometry("800x600")

label = tk.Label(window, text="Welcome to Python", font=('Arial', 25))
label.pack(pady=20)

input = tk.Entry(window)
input.pack(padx=100)


def print_message():
    print("Button Clicked!")


button = tk.Button(window, text="Clickable Button!", command=print_message)
button.pack(pady=25)

window.mainloop()


