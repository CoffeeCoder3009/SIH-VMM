import tkinter as tk




root = tk.Tk()
root.title("Hawk")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
vid_mag = tk.Menu(menu_bar)
vib_analysis = tk.Menu(menu_bar)
opt_flow = tk.Menu(menu_bar)
custom = tk.Menu(menu_bar)


menu_bar.add_cascade(label="File",menu=file_menu)
menu_bar.add_cascade(label="Magnification",menu=vid_mag)
menu_bar.add_cascade(label="Analysis",menu=vib_analysis)
menu_bar.add_cascade(label="Flow",menu=opt_flow)
menu_bar.add_cascade(label="Auxiliary",menu=custom)


root.mainloop()
