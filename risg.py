from Tkinter import *
from math import pi, cos, sin

root = Tk()
root.title('Recursive Image Spiral Generator')

vertex_number = 5
recursion_ratio = 0.75 # Part of master segments where new points (for new images) shall be drawn

def draw():
    c.delete("all")
    vertex_number = int(e1.get())
    recursion_ratio = float(e2.get())
    verticies = []

    for vertex in range(vertex_number):
        verticies.append((
            250*cos((vertex*2*pi)/vertex_number)+252,
            250*sin((vertex*2*pi)/vertex_number)+250))
    verticies.append((502,250))
    # Slight deviations in dimensions every once in a while, to ensure the drawing fits well
    
    for iteration in range(500):  
        for coords in verticies[:-1]:
            c.create_line(coords, verticies[verticies.index(coords)+1])
        for coords in verticies[:-1]:
            verticies[verticies.index(coords)] = (
                coords[0]-(recursion_ratio*(coords[0]-verticies[verticies.index(coords)+1][0])),
                coords[1]-(recursion_ratio*(coords[1]-verticies[verticies.index(coords)+1][1])))
        verticies[len(verticies)-1] = verticies[0]

c = Canvas(root, height=500, width=501)
c.pack(anchor=N)

options = Frame(root)
options.pack(side=RIGHT, fill=BOTH, expand=1)
entries = Frame(options)
entries.pack(side=LEFT, fill=BOTH, expand=1)
labels = Frame(entries)
labels.pack(side=LEFT, fill=BOTH, expand=1)

e1 = Entry(entries, width=20, fg="black")
e1.pack(side=TOP, fill=X, expand=1, padx=10, pady=10)
e1.insert(0, "5")
e2 = Entry(entries, width=20, fg="black")
e2.pack(side=BOTTOM, fill=X, expand=1, padx=10, pady=10)
e2.insert(0, "0.75")

l1 = Label(labels, text="Number of Verticies:")
l1.pack(side=TOP, fill=X, expand=1, padx=10, pady=10)
l2 = Label(labels, text="Recursion Ratio:")
l2.pack(side=TOP, fill=X, expand=1, padx=10, pady=10)


b = Button(options, text="RENDER", height=2, width=15, command=draw)
b.pack(side=RIGHT, fill=BOTH, expand=1, padx=10, pady=10)

draw()
mainloop()