import tkinter as tk
import math

points = [
    [-100, -75, -50], [100, -75, -50], [100, 75, -50], [-100, 75, -50],
    [-100, -75, 100], [100, -75, 100], [100, 75, 100], [-100, 75, 100],
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

angle_x = 0
angle_y = 0

def rotate_x(p, angle):
    x, y, z = p
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    y, z = y * cos_a - z * sin_a, y * sin_a + z * cos_a
    return [x, y, z]

def rotate_y(p, angle):
    x, y, z = p
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    x, z = x * cos_a + z * sin_a, -x * sin_a + z * cos_a
    return [x, y, z]

def project(p):
    """Proyeksi ortografik (tanpa perspektif) ke canvas"""
    x, y, z = p
    return x + 400, y + 300

def draw():
    canvas.delete("all")
    rotated = [rotate_y(rotate_x(p, angle_x), angle_y) for p in points]
    projected = [project(p) for p in rotated]
    for edge in edges:
        x0, y0 = projected[edge[0]]
        x1, y1 = projected[edge[1]]
        canvas.create_line(x0, y0, x1, y1, fill="purple", width=2)

def update():
    draw()
    root.after(30, update)

def key(event):
    global angle_x, angle_y
    if event.char == 'w':
        angle_x -= 0.1
    elif event.char == 's':
        angle_x += 0.1
    elif event.char == 'a':
        angle_y -= 0.1
    elif event.char == 'd':
        angle_y += 0.1

root = tk.Tk()
root.title("3D Wireframe Tanpa Library")
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()
root.bind("<Key>", key)

update()
root.mainloop()
