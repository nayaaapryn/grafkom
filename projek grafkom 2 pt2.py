import tkinter as tk
import math


points = [
    [-100, -75, -50], [100, -75, -50], [100, 75, -50], [-100, 75, -50],
    [-100, -75, 100], [100, -75, 100], [100, 75, 100], [-100, 75, 100],
]


faces = [
    [0, 1, 2, 3],  
    [4, 5, 6, 7],  
    [0, 1, 5, 4],  
    [2, 3, 7, 6],  
    [1, 2, 6, 5],  
    [0, 3, 7, 4],  
]

face_colors = ["red", "green", "blue", "yellow", "orange", "pink"]

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
    """ Proyeksi ortografik ke 2D """
    x, y, z = p
    return x + 400, y + 300

def average_z(face, rotated):
    """ Hitung rata-rata z dari 4 titik untuk z-sorting """
    return sum(rotated[i][2] for i in face) / 4

def draw():
    canvas.delete("all")
    rotated = [rotate_y(rotate_x(p, angle_x), angle_y) for p in points]
    projected = [project(p) for p in rotated]

    
    sorted_faces = sorted(
        enumerate(faces),
        key=lambda item: average_z(item[1], rotated),
        reverse=False  
    )

    for idx, face in sorted_faces:
        coords = []
        for i in face:
            x, y = projected[i]
            coords.extend([x, y])
        canvas.create_polygon(coords, fill=face_colors[idx], outline="black", width=1)

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
root.title("3D Balok - Hidden Surface + Z-Sorting")
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()
root.bind("<Key>", key)

update()
root.mainloop()
