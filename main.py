from tkinter import *
import pytube

#functions"""  """
def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video   = youtube.streams.first()
        video.download("C:/")
        notif.config(fg="green",text="download complete")
    except Exception as e:
        print(e)
        notif.config(fg="red",text="video could not be download")
        

#main screen
master =Tk()
master.title("video youtube")

#labels
Label(master, text="Download youtube", fg="red", font=("calibri",15)).grid(sticky=N,padx=10,row=0)
Label(master,text="please enter link : ", font=("calibri",12)).grid(sticky=N,row=1, pady=15)
notif = Label(master,font=("calibri",12))
notif.grid(sticky=N,pady=1,row=4)
#vars
url = StringVar()
#entry
Entry(master,width=50,textvariable=url).grid(sticky=N,row=2)
#button
Button(master, width=20,text="download",font=("calibri",12),command=download).grid(stick=N,row=3,pady=15)
master.mainloop()
