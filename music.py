import mudopy
import base64
import tkinter as tk 
from tkinter import PhotoImage


def download(song,artist):
    
    if artist!="":
        mudopy.set_path("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        mudopy.download(song,artist,None)
    else:
        mudopy.set_path(".\chromedriver.exe")
        mudopy.download(song,None,None)
    

        




root=tk.Tk()
root.configure(bg='#0c1620')
root.resizable(False, False)

str1=b'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'
#photo= PhotoImage(file="logo.png")
photo=PhotoImage(data=str1)
buttonExample5 = tk.Label(root, bg='#0c1620', bd=0, text="asdfasdf", image=photo)
buttonExample5.place(x=280, y=110)
song = tk.Entry(root)
song = tk.Entry(root, justify='center', width=34, font=200,  bg='#000000', insertbackground='white', bd=0, fg='#01ada0')
song.place(x=215, y=252)

artist = tk.Entry(root)
artist = tk.Entry(root, justify='center', width=34, font=200,  bg='#000000', insertbackground='white',
                         bd=0, fg='#01ada0')
artist.place(x=215, y=325)
labelExample1 = tk.Label(root, text="Artist name (optional)", bg='#0c1620', width=20, fg='#0e5152')
labelExample1.place(x=226, y=355)

labelExample2 = tk.Label(root, text="song", bg='#0c1620', width=15, fg='#0e5152')
labelExample2.place(x=207, y=280)

button=tk.Button(root)
button_wer = tk.Button(root, bg='#0c1620', fg='#0e5152', text="$ownload", command= lambda:download(song.get(),artist.get()))
button_wer.place(x=248, y=415)



root.geometry("738x470")
root.title("so^g")
root.wm_iconphoto(True, photo)

root.mainloop()