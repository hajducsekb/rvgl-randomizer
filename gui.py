from tkinter import *
from tkinter import ttk
import rvgl_get


rvgl_get.get_category('tracks/43467/Rooftops 1', '43467', 'Rooftops 1')

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
labelAppname.place(anchor = NW, relx=0.2, rely=0.05, relwidth=0.6)

labelName=Label(tabRand, text="Name: ")
labelName.place(anchor=NW, relx=0.1,rely=0.3)

labelCategory=Label(tabRand, text="Category: ")
labelCategory.place(anchor=NW, relx=0.1,rely=0.35)

labelLength=Label(tabRand, text="Length: ")
labelLength.place(anchor=NW, relx=0.1,rely=0.4)

bötön = Button(tabRand,text="Meg ne nyomd", command=lambda:[
        labelLength.config(text="Length: " + rvgl_get.get_length('tracks/43467/Rooftops 1', '43467', 'Rooftops 1')),
        labelCategory.config(text='Category: ' + rvgl_get.get_category('tracks/43467/Rooftops 1', '43467', 'Rooftops 1'))])
bötön.place(anchor=NW, relx=0.35, rely=0.12, relwidth=0.3)



#rvgl_get.get_length(trackid = input)

window.geometry('400x400')
window.mainloop()
