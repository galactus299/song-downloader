import mudopy
import tkinter as tk 


def download(song,artist):
    
    if artist!="":
        mudopy.set_path("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        mudopy.download(song,artist,None)
    else:
        mudopy.set_path("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        mudopy.download(song,None,None)
    

        



root=tk.Tk()
root.configure(bg='#0c1620')
root.resizable(False, False)
song = tk.Entry(root)
song = tk.Entry(root, justify='center', width=34, font=200,  bg='#000000', insertbackground='white',
                         bd=0, fg='#01ada0')
song.place(x=315, y=352)

artist = tk.Entry(root)
artist = tk.Entry(root, justify='center', width=34, font=200,  bg='#000000', insertbackground='white',
                         bd=0, fg='#01ada0')
artist.place(x=315, y=425)
labelExample1 = tk.Label(root, text="Artist name (optional)", bg='#0c1620', width=20, fg='#0e5152')
labelExample1.place(x=326, y=455)

labelExample2 = tk.Label(root, text="song", bg='#0c1620', width=15, fg='#0e5152')
labelExample2.place(x=307, y=380)

button=tk.Button(root)
button_wer = tk.Button(root, bg='#0c1620', fg='#0e5152', text="$ownload", command= lambda:download(song.get(),artist.get()))
button_wer.place(x=348, y=615)



root.geometry("938x670+500+200")
root.title("$oice")


root.mainloop()