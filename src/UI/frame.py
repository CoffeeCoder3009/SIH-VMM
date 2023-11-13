import tkinter as tk

def play_video():
    
    print("Playing video")

def pause_video():
    
    print("Pausing video")

root = tk.Tk()
root.title("Hawk")

# logo_image = tk.PhotoImage(file="C:\\Users\\h5cd2\\OneDrive\\Desktop\\sih\\SIH-VMM\\src\\UI\\Sih_logo.jpg")

title_label = tk.Label(root,text="Hawk",compound=tk.LEFT)
title_label.pack(anchor="w",padx=10)

# Screen to display video
video_canvas = tk.Canvas(root, width=400, height=300, bg="black")
video_canvas.pack(pady=10)

# Play and Pause buttons
play_button = tk.Button(root, text="Play",command=play_video)
play_button.pack(side=tk.LEFT,padx=10)

pause_button = tk.Button(root, text="Pause",command=pause_video)
pause_button.pack(side=tk.LEFT)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
vid_mag = tk.Menu(menu_bar)
vib_analysis = tk.Menu(menu_bar)
opt_flow = tk.Menu(menu_bar)
custom = tk.Menu(menu_bar)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Magnification", menu=vid_mag)
menu_bar.add_cascade(label="Analysis", menu=vib_analysis)
menu_bar.add_cascade(label="Flow", menu=opt_flow)
menu_bar.add_cascade(label="Auxiliary", menu=custom)

root.mainloop()
