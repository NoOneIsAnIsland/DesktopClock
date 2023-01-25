from tkinter import *
from tkinter.ttk import *
 
from time import strftime
# import psutil

def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()
    
def close_app():
    root.destroy()
    
def time():
    string = strftime('%H:%M:%S %p')
    # string = string + f' {psutil.cpu_percent(4)}'
    lbl.config(text=string)
    lbl.after(1000, time)
    
def move(event):
    x, y = root.winfo_pointerxy()
    root.geometry(f"+{x}+{y}")
    
if __name__ == '__main__':    
    CENTERED = True
    
    root = Tk()
    root.configure(background='black')
    root.title('Clock')
    root.iconbitmap("clock.ico")
    
    fsize = 28
    # Remove title bar
    root.overrideredirect(True)
    # Set transparency
    root.attributes('-alpha', 0.5)
    #Make the window jump above all
    root.attributes('-topmost',True)
    
    # Set the dimension and position
    w = fsize*8.0 # Wdth for the Tk root
    h = fsize*1.8 # Height for the Tk root
    ws = root.winfo_screenwidth() # Width of the screen
    hs = root.winfo_screenheight() # Height of the screen
    if CENTERED:
        x = ws/2 - w/2
    else:
        x = ws - w/2 - 150
    y = hs - h/2 - 70
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    m = Menu(root, tearoff=0)
    m.add_command(label="Close", command=close_app)
    
    lbl = Label(root, font=('calibri', fsize, 'bold'),
                background='black',
                foreground='yellow')
     
    # Placing clock at the centre of the tkinter window
    lbl.pack(anchor="center")
    time()
    
    lbl.bind("<Button-3>", do_popup)
    root.bind('<B1-Motion>', move)

    root.mainloop()