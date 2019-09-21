from tkinter import *
from tkinter import ttk
from PIL import Image
import rvgl_get


#rvgl_get.get_category('tracks/43467/Rooftops 1', '43467', 'Rooftops 1')

#basic initialization
window = Tk()
window.title("RVZ parser")

#notebook tab initialization
tab_control=ttk.Notebook(window)
tabRand=ttk.Frame(tab_control)
tabID=ttk.Frame(tab_control)
tab_control.add(tabRand, text='Random picker')
tab_control.pack(expand=1, fill='both')
tab_control.add(tabID, text='ID based downloader')
tab_control.pack(expand=1, fill='both')

labelAppname=Label(tabRand, text="Re-Volt Randomizer App")
labelAppname.place(anchor = NW, relx=0.2, rely=0.03, relwidth=0.6)

labeltítel=Label(tabRand, text="Track")
labeltítel.place(anchor=NW, relx=0.1,rely=0.23)

labelName=Label(tabRand, text="Name: ")
labelName.place(anchor=NW, relx=0.1,rely=0.3)

labelCategory=Label(tabRand, text="Category: ")
labelCategory.place(anchor=NW, relx=0.1,rely=0.35)

labelLength=Label(tabRand, text="Length: ")
labelLength.place(anchor=NW, relx=0.1,rely=0.4)

gfxTrack = PhotoImage(file = 'startup.png')
labelTrackimage = Label(tabRand, image=gfxTrack)
labelTrackimage.place(anchor= NW, relx=0.1, rely=0.55)

labelTrackDL=Label(tabRand, text="")
labelTrackDL.place(anchor=NW, relx=0.1,rely=0.48)

bötön = Button(tabRand,text="Meg ne nyomd", command=lambda:[
        rvgl_get.randomize(),
        labelLength.config(text="Length: " + rvgl_get.tracklength + ' Meters'),
        labelCategory.config(text='Category: ' + rvgl_get.trackType),
        labelName.config(text='Name: ' + rvgl_get.trackname),
        labelCarName.config(text="Name: " + rvgl_get.carname),
        labelCarCategory.config(text='Rating: ' + rvgl_get.carrating),
        gfxCar.config(file = rvgl_get.getCarImgURL(rvgl_get.carURL)),
        gfxTrack.config(file = rvgl_get.getTrackImgURL(rvgl_get.trackURL))])
bötön.place(anchor=NW, relx=0.35, rely=0.1, relwidth=0.3)

dlbötön = Button(tabRand,text='D0wnl04d', command=lambda:[
        rvgl_get.dl_content(rvgl_get.carID),
        labelCarDL.config(text='Car Downloaded'),
        rvgl_get.dl_content(rvgl_get.trackID),
        labelTrackDL.config(text='Track Downloaded'),
    ])
dlbötön.place(anchor=NW, relx=0.35, rely=0.8, relwidth=0.3)


labeltíte=Label(tabRand, text="Car")
labeltíte.place(anchor=NW, relx=0.6,rely=0.23)

labelCarName=Label(tabRand, text="Name: ")
labelCarName.place(anchor=NW, relx=0.6,rely=0.3)

labelCarCategory=Label(tabRand, text="Category: ")
labelCarCategory.place(anchor=NW, relx=0.6,rely=0.35)

gfxCar = PhotoImage(file = 'startup.png')
labelCarimage = Label(tabRand, image=gfxCar)
labelCarimage.place(anchor= NW, relx=0.6, rely=0.55)

labelCarDL=Label(tabRand, text="")
labelCarDL.place(anchor=NW, relx=0.6,rely=0.48)


#image.show()
#image=Image.open(filename)
#imagesprite = window.create_image(400,400,image=image)
#rvgl_get.get_length(trackid = input)

window.geometry('400x400')
window.mainloop()
