import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file = "python_logo.gif")

w1 = tk.Label(root, image=logo).pack(side="right")

explanation = """At present, only GIF and PPM/PGM 
formats are supposed, but an interface
exists to allow addition image file
formats to be added easily."""

w2 = tk.Label(root, justify=tk.LEFT, padx = 10, text=explanation).pack(side="left")

root.mainloop()