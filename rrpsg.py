import Tkinter as tk
from math import pi, cos, sin


class Rrpsg(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.vertex_number = 5
        self.recursion_ratio = 0.75 # Part of master segments where new points (for new polygons) shall be drawn

        # Establishes drawing canvas at the top of the window with default dimensions
        self.c = tk.Canvas(root, height=500, width=501)
        self.c.pack(anchor=tk.N)

        # Labels packed in entries, entries packed in options
        self.options = tk.Frame(root)
        self.options.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        self.entries = tk.Frame(self.options)
        self.entries.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.labels = tk.Frame(self.entries)
        self.labels.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Individual entries and labels packed to the top and bottom of their respective frames
        self.l1 = tk.Label(self.labels, text="Number of Verticies:")
        self.l1.pack(side=tk.TOP, fill=tk.X, expand=1, padx=10, pady=10)
        self.e1 = tk.Entry(self.entries, width=20, fg="black")
        self.e1.pack(side=tk.TOP, fill=tk.X, expand=1, padx=10, pady=10)
        self.e1.insert(0, "5")

        self.l2 = tk.Label(self.labels, text="Recursion Ratio:")
        self.l2.pack(side=tk.BOTTOM, fill=tk.X, expand=1, padx=10, pady=10)
        self.e2 = tk.Entry(self.entries, width=20, fg="black")
        self.e2.pack(side=tk.BOTTOM, fill=tk.X, expand=1, padx=10, pady=10)
        self.e2.insert(0, "0.75")

        # Button packed in options, outside of entries/labels frames
        self.b = tk.Button(self.options, text="RENDER", height=2, width=15, command=self.draw)
        self.b.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1, padx=10, pady=10)

        self.draw() # Draws default image

    def draw(self):
        self.c.delete("all")
        self.vertex_number = int(self.e1.get())
        self.recursion_ratio = float(self.e2.get())
        verticies = []

        for vertex in range(self.vertex_number):
            verticies.append((
                250*cos( (vertex*2*pi)/self.vertex_number) +252,
                250*sin( (vertex*2*pi)/self.vertex_number) +250))
        verticies.append((502,250))
        # Slight deviations in dimensions every once in a while, to ensure the drawing fits well
        
        for iteration in range(500):  
            for coords in verticies[:-1]:
                self.c.create_line(coords, verticies[verticies.index(coords)+1])
            for coords in verticies[:-1]:
                verticies[verticies.index(coords)] = (
                    coords[0]-(self.recursion_ratio*(coords[0]-verticies[verticies.index(coords)+1][0])),
                    coords[1]-(self.recursion_ratio*(coords[1]-verticies[verticies.index(coords)+1][1])))
            verticies[len(verticies)-1] = verticies[0]
          

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Recursive Regular Polygon Spiral Generator")
    Rrpsg(root).pack()
    root.mainloop()