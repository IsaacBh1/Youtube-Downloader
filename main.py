from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from pytube import YouTube


root = Tk()
root.geometry("800x450")
root.title("YOUTUBE DOWNLOADER")
root.resizable(False,False)
#logo
YoutubeLogo = PhotoImage(file ='YoutubeLogo').subsample(5)
yt = Label(root , image=YoutubeLogo)
yt.place(relx = 0.5 , rely = 0.25 ,anchor = 'center')

#functions

def select():
    directory = filedialog.askdirectory(title="save vedio")
    DownloadFolder_entry.delete(0,"end")
    DownloadFolder_entry.insert(0,directory)



def download():
    link = link_enter.get()
    folder = DownloadFolder_entry.get()
    print(f'the video has allready download')
    Allstreams = YouTube(link).streams.filter(progressive=False,file_extension='mp4')
    myvideo = Allstreams.get_by_resolution(my_Stream.get()).download(folder)
    print('downloading secces')

value = ["144p","360p","720p","1080p"]

#link 
youtubelink = Label(root , text='YouTube Link')
youtubelink.place(x = 20 , y = 170)


link_enter = Entry(root ,width = 70)
link_enter.place(x = 150 , y = 170 )

#download folder 

DownloadFolder = Label(root , text='Download Folder')
DownloadFolder.place(x = 20 , y = 210 )

DownloadFolder_entry = Entry(root , width = 60)
DownloadFolder_entry.place(x = 150 ,y = 210)

#select folder 

SelectFolder = Button(root, text = 'Select' , command=select)
SelectFolder.place(x = 642, y = 205)

# strems 
StreamLable = Label(root ,text='Stream')
StreamLable.place(x = 20 , y = 240)
my_Stream = ttk.Combobox(root , width = 60 , values = value)
my_Stream.place(x = 150 ,y = 240)
#download button

DownloadButton = Button(root , text='Download' , command=download)
DownloadButton.place(relx = 0.5, rely = 0.75 ,anchor='center')


root.mainloop()
