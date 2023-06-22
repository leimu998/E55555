import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

root = tk.Tk()
root.title("动态时钟")

clock_label = tk.Label(root, font=("Arial", 80), fg="black", bg="white")
clock_label.pack(padx=50, pady=50)

update_clock()

root.mainloop()
