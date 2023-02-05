from tkinter import *


splash_root = Tk()
splash_root.geometry("300x200")
#hide title bar
splash_root.overrideredirect(True)

root = Tk()

def main_window():
    splash_root.destroy()
    root = Tk()
    root.geometry("500x550")

#designate height and width of our app
app_width = 500
app_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
splash_label = Label(splash_root, text="Splash Screen!", font=("Helvetica", 18))
splash_label.pack(pady=20)

# my_label = Label(root, text=f'Width{screen_width} Height{screen_height}')
# my_label.pack(pady=20)



#splash screen timer
splash_root.after(3000, main_window)
mainloop()