import Tkinter
import subprocess
win = Tkinter.Tk()
win.title("pyLauncher 3.0")
win.geometry("400x400")

def mc():
    subprocess.call([r'data.bat'])

def mods():
    subprocess.call([r'mods.bat'])

def update():
    subprocess.call([r'update.bat'])

def about():
    about = Tkinter.Tk()
    about.title("About pyLauncher")
    la1 = Tkinter.Label(about,text="Maked by glowiak; github.com.glowiak")
    la1.pack()



def main():
    l1 = Tkinter.Label(win,text="pyLauncher - Python Minecraft Launcher")
    l1.pack()
    b1 = Tkinter.Button(win,text="Play!",command=mc)
    b1.pack()
    b2 = Tkinter.Button(win,text="Get mods",command=mods)
    b2.pack()
    b3 = Tkinter.Button(win,text="Update pyLauncher",command=update)
    b3.pack()
    b4 = Tkinter.Button(win,text="About pyLauncher",command=about)
    b4.pack()
    win.mainloop()

main()
    
