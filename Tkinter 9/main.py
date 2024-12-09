from tkinter import *
root = Tk()
root.title("Дом")

canvas = Canvas(root, width=200, height=200, bg='white')
canvas.pack()

# Крыша
canvas.create_polygon(100, 50, 50, 100, 150, 100, fill='lightblue', outline='black')
# Корпус 
canvas.create_rectangle(60, 100, 140, 160, fill='lightblue', outline='black')

# Солнце
canvas.create_oval(150, 10, 190, 50, fill='yellow', outline='yellow')

# Трава
for x in range(0, 200, 10):
    canvas.create_line(x, 200, x + 10, 160, fill='green', width=2)

root.mainloop()
