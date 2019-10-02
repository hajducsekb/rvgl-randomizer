from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
import rvgl_get

#basic initialization
window = Tk()
window.title("Re-Volt Randomizer App")

photoW=PhotoImage(file="bolt.gif")
window.iconphoto(False,photoW)

#notebook tab initialization
tab_control=ttk.Notebook(window)
tabRand=ttk.Frame(tab_control)
tabID=ttk.Frame(tab_control)
tab_control.add(tabRand, text='Random picker')
tab_control.pack(expand=1, fill='both')
tab_control.add(tabID, text='ID based downloader')
tab_control.pack(expand=1, fill='both')

if rvgl_get.rvglpath == '':
        rvgl_get.rvglpath = filedialog.askdirectory(initialdir=rvgl_get.workingpath, title='Select RVGL installation folder')
        print ('Your path is... ' + rvgl_get.rvglpath)
        with open('./rvglparser_config.txt', 'w') as configfile:
                configfile.write(rvgl_get.rvglpath)




labelAppname=Label(tabRand, text="Randomizer")
labelAppname.place(anchor = NW, relx=0.2, rely=0.03, relwidth=0.6)

labeltítel=Label(tabRand, text="Track:")
labeltítel.place(anchor=NW, relx=0.1,rely=0.23)

labelName=Label(tabRand, text="Name: ", underline=1)
labelName.place(anchor=NW, relx=0.1,rely=0.3)

labelCategory=Label(tabRand, text="Category: ")
labelCategory.place(anchor=NW, relx=0.1,rely=0.35)

labelLength=Label(tabRand, text="Length: ")
labelLength.place(anchor=NW, relx=0.1,rely=0.4)

gfxTrack = PhotoImage(file = 'startup.png')
labelTrackimage = Label(tabRand, image=gfxTrack)
labelTrackimage.place(anchor= NW, relx=0.1, rely=0.5)

labelTrackDL=Label(tabRand, text="")
labelTrackDL.place(anchor=NW, relx=0.1,rely=0.45)

bötön = Button(tabRand,text="Randomize", command=lambda:[
        labelCarDL.config(text=""),
        labelTrackDL.config(text=""),
        rvgl_get.randomize(),
        labelLength.config(text="Length: " + rvgl_get.tracklength + ' Meters'),
        labelCategory.config(text='Category: ' + rvgl_get.trackType),
        labelName.config(text='Name: ' + rvgl_get.trackname),
        labelCarName.config(text="Name: " + rvgl_get.carname),
        labelCarCategory.config(text='Rating: ' + rvgl_get.carrating),
        gfxCar.config(file = rvgl_get.getCarImgURL(rvgl_get.carURL)),
        gfxTrack.config(file = rvgl_get.getTrackImgURL(rvgl_get.trackURL))])
bötön.place(anchor=NW, relx=0.35, rely=0.1, relwidth=0.3)

def trackList():
        base = labelTracks.cget("text")
        labelTracks.config(text=base+rvgl_get.trackname+"\n")

def carList():
        base = labelCars.cget("text")
        labelCars.config(text=base+rvgl_get.carname+"\n")

dlbötönTrack = Button(tabRand,text='Download Track', command=lambda:[
        rvgl_get.dl_content(rvgl_get.trackID),
        labelTrackDL.config(text='Track Downloaded'),
        trackList(),
        window.clipboard_clear(),
        window.clipboard_append(rvgl_get.trackID)
    ])
dlbötönTrack.place(anchor=NW, relx=0.07, rely=0.69, relwidth=0.25)

dlbötönCar = Button(tabRand,text='Download Car', command=lambda:[
        rvgl_get.dl_content(rvgl_get.carID),
        labelCarDL.config(text='Car Downloaded'),
        carList(),
        window.clipboard_clear(),
        window.clipboard_append(rvgl_get.carID)
    ])
dlbötönCar.place(anchor=NW, relx=0.57, rely=0.69, relwidth=0.25)

dlbötön = Button(tabRand,text='Download and copy IDs', command=lambda:[
        rvgl_get.dl_content(rvgl_get.carID),
        labelCarDL.config(text='Car Downloaded'),
        carList(),
        rvgl_get.dl_content(rvgl_get.trackID),
        labelTrackDL.config(text='Track Downloaded'),
        trackList(),
        window.clipboard_clear(),
        window.clipboard_append(rvgl_get.trackID + ", " + rvgl_get.carID)
    ])
dlbötön.place(anchor=NW, relx=0.2, rely=0.8, relwidth=0.6)

caseButton = Button(tabRand,text='Fix Cases (Linux only)', command=lambda:[
        rvgl_get.fixcases()
])
caseButton.place(anchor=NW, relx=0.2, rely=0.9, relwidth=0.6)

labeltíte=Label(tabRand, text="Car:", underline=True)
labeltíte.place(anchor=NW, relx=0.6,rely=0.23)

labelCarName=Label(tabRand, text="Name: ")
labelCarName.place(anchor=NW, relx=0.6,rely=0.3)

labelCarCategory=Label(tabRand, text="Category: ")
labelCarCategory.place(anchor=NW, relx=0.6,rely=0.35)

gfxCar = PhotoImage(file = 'startup.png')
labelCarimage = Label(tabRand, image=gfxCar)
labelCarimage.place(anchor= NW, relx=0.6, rely=0.5)

labelCarDL=Label(tabRand, text="")
labelCarDL.place(anchor=NW, relx=0.6,rely=0.45)

labelAppname=Label(tabID, text="ID Downloader")
labelAppname.place(anchor = NW, relx=0.2, rely=0.03, relwidth=0.6)

IDEntry = Entry(tabID,width=10)
IDEntry.place(anchor=CENTER, relx=0.3, rely=0.2)

labelid = Label(tabID, text="ID:")
labelid.place(anchor=CENTER, relx=0.13, rely=0.2)

labelDL=Label(tabID, text="")
labelDL.place(anchor=CENTER, relx=0.5,rely=0.3)

labelTracks=Label(tabID,text="Tracks:\n")
labelTracks.place(anchor=NW, relx=0,rely=0.4)

labelCars=Label(tabID,text="Cars:\n")
labelCars.place(anchor=NE, relx=1,rely=0.4)

def splitAndDl(idnos):
        labelDL.config(text="")
        idk=idnos
        idks=idk.split(',')
        for ide in idks:
                rvgl_get.dl_content(ide)
                if rvgl_get.track==True:
                        base = labelTracks.cget("text")
                        labelTracks.config(text=base+rvgl_get.trackname+"\n")
                if rvgl_get.car==True:
                        base = labelCars.cget("text")
                        labelCars.config(text=base+rvgl_get.carname+"\n")
        labelDL.config(text=rvgl_get.dlState)

IDdlbötön= Button(tabID, text="Download by ID", command=lambda:[
        splitAndDl(IDEntry.get())
])
IDdlbötön.place(anchor=CENTER, relx=0.7, rely=0.2)

Törölbötön= Button(tabID, text="Delete track and carlist", command=lambda:[
        labelTracks.config(text="Tracks: \n"),
        labelCars.config(text="Cars: \n")
])
Törölbötön.place(anchor=CENTER, relx=0.5, rely=0.85)

window.geometry('400x400')
window.mainloop()
