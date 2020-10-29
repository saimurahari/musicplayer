#!/usr/bin/env python
# coding: utf-8

# In[58]:


from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from pygame import mixer

def resumemusic():
    root.resume_button.grid_remove()
    root.pause_button.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text="playing...")
    
def volumeup():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)
    AudioStatusLabel.configure(text="Volume Up...")

def volumedown():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol-0.1)
    AudioStatusLabel.configure(text="Volume down...")

def pausemusic():
    mixer.music.pause()
    root.pause_button.grid_remove()
    root.resume_button.grid()
    AudioStatusLabel.configure(text="paused")
    
def musicurl():
    try:
        dd = filedialog.askopenfilename(initialdir = 'C:', title="Select Audio File",filetype=(("MP3","*.mp3"),
                                                                                               ("WAV","*.wav")))
        
    except:
        dd = filedialog.askopenfilename(title="Select Audion File",filetype = (("MP3","*.mp3"),("WAV","*.wav")))
    audiotrack.set(dd)

def playmusic():
    ad=audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()
    AudioStatusLabel.configure(text="playing...")



root = Tk()
#creating menu bar
menubar = Menu(root)

#Adding file menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File',menu=file)
file.add_command(label="New Music", command=musicurl)
file.add_command(label="save")
file.add_separator()
file.add_command(label="exit", command = root.destroy)

#Adding play menu and commands
play=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Play', menu=play)
play.add_command(label="resume", command=resumemusic)
play.add_command(label = "Play", command=playmusic)
play.add_separator()



music_lable = Label(root,text="Welcome to Music Player", font = ("arial",20,"bold"), fg="black" )
music_lable.grid(row=0,column=1,pady=5,padx=90)

tracklable = Label(root,text = "Select Audio Track: ", fg="black",font = ('arial',18,'bold'))
tracklable.grid(row=1,column=0,padx=20,pady=20)



AudioStatusLabel = Label(root, text = "",fg="black", font = ('arial',13,'bold'))
AudioStatusLabel.grid(row=3,column=1)

Browse_Button = Button(root,text="search", fg='black',font=('arial',18,"bold"),activeforeground= 'blue',command=musicurl,
                       width=10,bd=5)
Browse_Button.grid(row=1,column=1,padx=20,pady=20)
Browse_Button.config(highlightbackground="red", highlightcolor="black", highlightthickness=10, relief=SOLID)

Play_button = Button(root, text="play",fg="black",font=('arial',13,'bold'),command=playmusic,width=10,bd=5)
Play_button.config(highlightbackground="red", highlightcolor="black", highlightthickness=10, relief=SOLID)
Play_button.grid(row=2,column=0,padx=20,pady=20)

root.pause_button = Button(root, text="Pause",  fg='black',font=('arial',13,'bold'),command=pausemusic,width=10,bd=5)
root.pause_button.config(highlightbackground="red", highlightcolor="black", highlightthickness=10, relief=SOLID)
root.pause_button.grid(row=3,column=0,padx=20,pady=20)

root.resume_button = Button(root, text="Resume", fg="black", font=('arial',13,'bold'),bd=5,activebackground="cyan",width=10,
                            compound=RIGHT,command=resumemusic)
root.resume_button.config(highlightbackground="red", highlightcolor="black", highlightthickness=10, relief=SOLID)
root.resume_button.grid(row=2,column=1,padx=20,pady=20)
root.resume_button.grid_remove()

Volume_Up_Button = Button(root, text="VolumeUp", fg="black", font=('arial',13,'bold'),bd=5, width=10,activebackground="cyan",
                          compound=RIGHT,command=volumeup)
Volume_Up_Button.config(highlightbackground="red", highlightcolor="black", highlightthickness=10, relief=SOLID)
Volume_Up_Button.grid(row=2,column=2,padx=20,pady=20)


Volume_Down_Button = Button(root, text="VolumeDown",fg="black", font=('arial',13,'bold'),bd=5,width=10,
                            activebackground="cyan",compound=RIGHT,command=volumedown)
Volume_Down_Button.config(highlightbackground="red", highlightcolor="black", highlightthickness=10, relief=SOLID)
Volume_Down_Button.grid(row=3,column=2,padx=20,pady=20)

audiotrack = StringVar()

label=Label(root,background="white")
label.place(x=0,y=0)

ss="Developed by Sai Murahari, Tejeswar kumar and Gopichand"
count=0
text=""

Slider_Lable = Label(root,text=ss,bg="blue", fg="white", font=('arial',16,'bold'))
Slider_Lable.grid(row=4,column=0,padx=20,pady=20, columnspan=3)

def IntroLabelTrick():
    global count, text
    if(count>=len(ss)):
        count = -1
        text = ""
        Slider_Lable.configure(text = text)
    else:
        text = text+ss[count]
        Slider_Lable.configure(text=text)
    count +=1
    Slider_Lable.after(200,IntroLabelTrick)

IntroLabelTrick()
mixer.init()
root.geometry("980x450")
root.title("Music Player")
root.resizable(False,False)
root.config(menu=menubar)
root.config(background="red")
root.mainloop()



# In[ ]:




