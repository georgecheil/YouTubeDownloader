from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import os


Folder_Name = ""

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 0):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder",fg="red") 




def downloadFunction():
    user_choice = ytdChoices.get()
    url_get = ytdEntry.get()
    
    if(len(url_get) > 1):
        ytdError.config(text="")
        youtube  = YouTube(url_get)   #!!!

        if(user_choice == choices[0]):
            video = youtube .streams.get_highest_resolution()
            video.download(Folder_Name)

        elif(user_choice == choices[1]):
            audio = youtube .streams.filter(only_audio=True).first()
            audio_file = audio.download(output_path=str(Folder_Name))

            base, ext = os.path.splitext(audio_file) 
            new_file = base + '.mp3'
            os.rename(audio_file, new_file) 
  
    
        ytdError.config(text="Download Completed")

    else:
        ytdError.config(text="")
        ytdError.config(text="Please Enter URL")
    


root = Tk()
root.title("YouTube Downloader")
#root.iconbitmap('c:/Users/georg/OneDrive - unipi.gr/Pictures/YTD.ico')
root.geometry("400x450")    #window dimentions
root.columnconfigure(0, weight=1) #all in center
root.configure(bg="#c4e6ff")

#Logo Label
logoLabel = Label(root,text="YouTube Downloader", font=("jost",20,"bold"),fg="red", bg="#c4e6ff")
logoLabel.grid(pady=5)

#Link Label
ytdLabel = Label(root, text = "Enter the URL", font=("jost", 15,"bold"), bg="#c4e6ff")
ytdLabel.grid(pady=10)

#Entry Bar
ytdEntryVal = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVal)
ytdEntry.grid()

#Error
ytdError = Label(root,text="Error Message",fg="#cb2c31",font=("jost",10,"bold"), bg="#c4e6ff")
ytdError.grid()

#Path Label
saveLabel = Label(root,text="Save the Video File",font=("jost",15,"bold"), bg="#c4e6ff")
saveLabel.grid(pady=10)

#Choose Path Button
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path", font=("jost",10,"bold"), command=openLocation)
saveEntry.grid()

#Error
locationError = Label(root,text="Error Message of Path",fg="#cb2c31",font=("jost",10,"bold"), bg="#c4e6ff")
locationError.grid()

#Choose Type
ytdType = Label(root,text="Select Video or Audio",font=("jost",15,"bold"), bg="#c4e6ff")
ytdType.grid(pady=10)

#Combobox
choices = ["Video", "Audio"]
ytdChoices = ttk.Combobox(root,values=choices)
ytdChoices.grid(pady=5)



#Download Button
downloadButton = Button(root,bg="red",fg="white",text="Download ", font=("jost",10,"bold"), padx=20,pady=10,command=downloadFunction)
downloadButton.grid()


root.mainloop()
