from customtkinter import *
import tkinter as tk 
from tkinter import ttk 
from PIL import Image 
from tkinter import filedialog
import pytube as pt
#the main app window 

root = CTk()
root.title('Youtube Downloader')
root.geometry('700x450')
root.resizable(False , False)
#set_appearance_mode('light')


#functions 

#frames
# logo frame
LogoFrame = CTkFrame(root ,fg_color='transparent'  , width=600 , height=150)
LogoFrame.pack(fill = X , pady = 30)

# link frame 

linkFrame = CTkFrame(root , fg_color = 'transparent')
linkFrame.place(relx = 0.5 , rely = 0.4 , anchor = 'center' , relwidth = 1 ,relheight =  0.1)

#save vedeo path 
SavePath =  CTkFrame(root , fg_color = 'transparent')
SavePath.place(relx = 0.5 , rely = 0.55 , anchor = 'center' , relwidth = 1 ,relheight =  0.1)

# quality of video 
Quality = CTkFrame(root, fg_color = 'transparent')
Quality.place(relx = 0.5 , rely = 0.7 , anchor = 'center' , relwidth = 1 ,relheight =  0.1)


#---------------------- functions ----------------------------

#choose the path 
def choose():
    PathOfFolder = filedialog.askdirectory()
    DownloadVar.set(PathOfFolder)


def DOWNLOAD():
    DownloadBvar = StringVar(value = ' ')
    link = link_enter.get()
    folder = DownloadFolder_entry.get()
    yt = pt.YouTube(link)
    
    if Quality_entry.get() == 'Hight Quality' : 
        try:
            DownloadBvar.set(value = 'Done')
            DownloadLabel = CTkLabel(Download , text = '' ,textvariable = DownloadBvar, font = ('times' , 15 , 'bold') , text_color='green2')
            DownloadLabel.pack(pady = 5)

            video = yt.streams.filter(file_extension='mp4').get_highest_resolution()
            video.download(folder)
            #DownloadLabel.pack_forget() 
        
        except Exception as e:
            DownloadBvar.set(value = 'Error')
            DownloadLabel = CTkLabel(Download , text = '' ,textvariable = DownloadBvar, font = ('times' , 15 , 'bold') , text_color='red')
            DownloadLabel.pack(pady = 5)
    elif Quality_entry.get() == 'medium Quality': 
        try:
            DownloadBvar.set(value = 'Done')
            DownloadLabel = CTkLabel(Download , text = '' ,textvariable = DownloadBvar, font = ('times' , 15 , 'bold') , text_color='green2')
            DownloadLabel.pack(pady = 5)

            video = yt.streams.filter(file_extension='mp4').get_by_resolution(resolution='480p')
            video.download(folder)
            #DownloadLabel.pack_forget() 
        
        except Exception as e:
            DownloadBvar.set(value = 'Error')
            DownloadLabel = CTkLabel(Download , text = '' ,textvariable = DownloadBvar, font = ('times' , 15 , 'bold') , text_color='red')
            DownloadLabel.pack(pady = 5)
    elif Quality_entry.get() == 'Low Quality':
        try:
            DownloadBvar.set(value = 'Done')
            DownloadLabel = CTkLabel(Download , text = '' ,textvariable = DownloadBvar, font = ('times' , 15 , 'bold') , text_color='green2')
            DownloadLabel.pack(pady = 5)

            video = yt.streams.filter(file_extension='mp4').get_lowest_resolution()
            video.download(folder)        
        except Exception as e:
            DownloadBvar.set(value = 'Error')
            DownloadLabel = CTkLabel(Download , text = '' ,textvariable = DownloadBvar, font = ('times' , 15 , 'bold') , text_color='red')
            DownloadLabel.pack(pady = 5)
    else :         
        DownloadBvar.set(value = 'Error')
        DownloadLabel = CTkLabel(Download , text = '' ,textvariable = DownloadBvar, font = ('times' , 15 , 'bold') , text_color='red')
        DownloadLabel.pack(pady = 5)
    
    #delete entryes
    DownloadFolder_entry.delete(0,END)
    link_enter.delete(0,END)



    #download button 

Download = CTkFrame(root, fg_color = 'transparent' )
Download.place(relx = 0.5 , rely = 0.85 , anchor = 'center' , relwidth = 0.5 ,relheight =  0.12)



#the Title logo of the application
logo = CTkImage(dark_image=Image.open('Youtube-Logo-PNG.png'), size=(320 , 100))
LogoImage = CTkLabel(LogoFrame , image=logo, text=' ').pack()

#widgets 
# of linkFrame

youtubelink = CTkLabel(linkFrame , text='Youtube Link' , font = ('times' , 20 , 'bold') , text_color='white')
youtubelink.pack(side = 'left' ,padx = 35)
link_enter = CTkEntry(linkFrame ,width = 450 , font = ('times' , 20 , 'italic') , justify = 'left')
link_enter.pack(side = 'left')

# of path 

DownloadVar = StringVar()
DownloadFolder = CTkLabel(SavePath , text='Download Folder' , font = ('times' , 20 , 'bold') , text_color='white')
DownloadFolder.pack(side = 'left' , padx = 20)
DownloadFolder_entry = CTkEntry(SavePath, width = 430 ,font = ('times' , 20 , 'italic') , textvariable=DownloadVar )
DownloadFolder_entry.pack(side = 'left')
DownloadFolderButton = CTkButton(SavePath , text='+' , width=10, text_color='white' , fg_color='#ff1717' , hover_color='#9e0000' , cursor = 'hand2'  , command=choose).pack(side = 'left')


#quality 

QualityLabel = CTkLabel(Quality , text='Quality' , font = ('times' , 20 , 'bold') , text_color='white')
QualityLabel.pack(side = 'left' , padx = 62)
Quality_entry = CTkComboBox(Quality,values=['Hight Quality' , 'medium Quality' , 'Low Quality']  , width = 450 ,font = ('times' , 20 , 'italic')  , justify='center' , dropdown_font=('times' , 20 , 'italic') , text_color='white')
Quality_entry.pack(side = 'left')


#download button
DownloadButton = CTkButton(Download , text='Download' , font = ('times' , 20 , 'bold') , text_color='white' , fg_color='#ff1717' , hover_color='#9e0000' , cursor = 'hand2' , command=DOWNLOAD).pack()

#run
set_appearance_mode('dark')
root.mainloop()

