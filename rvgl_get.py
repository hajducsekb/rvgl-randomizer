import os
from bs4 import BeautifulSoup
import requests
import urllib.request
import urllib.parse
import zipfile
from PIL import Image
import sys

if sys.platform == 'windows':
    execname = 'rvzparser.exe'
else:
    execname = 'rvzparser'


if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    workingpath = os.path.dirname(sys.executable)
else:
    workingpath = os.path.dirname(os.path.abspath(__file__))


trackname=""
tracklength=""
trackType=""
trackID=""
carname=""
carrating=""
carID=""
carURL=""
trackURL=""
trackgfx=""
cargfx=""
dlState=""

#workingpath = os.path.dirname(os.path.abspath(__file__))
os.chdir(workingpath)
print(workingpath)
if os.path.isfile('./rvglparser_config.txt') == False:
    with open('./rvglparser_config.txt', 'w') as configfile:
        rvglpath = ''

else:
    with open('./rvglparser_config.txt', 'r') as configfile:
        rvglpath = str(configfile.read())
        print('RVGL Path: ' + rvglpath)





def dl_content(idlist):
# Download the file from `url` and save it locally under `file_name`:
    listofdl = idlist.split(',')
    for listitem in listofdl:
        contid = listitem.replace(' ', '')
        print('Downloading...')
        global dlState
        try:
            urllib.request.urlretrieve('http://revoltzone.net/sitescripts/dload.php?id=' + contid, 'rvz' + contid + '_dl.zip')
            print('Content downloaded')
            '''with zipfile.ZipFile('./rvz' + contid + '_dl.zip' , 'r') as zip_ref:
                zip_elem = zip_ref.namelist()
                #print(zip_elem)
                overwriteFiles = 1
                for item in zip_elem:
                    print(str(item))
                    item_list = item.split('/')
                    filename = str(item_list[-1])
                    if os.path.isfile(rvglpath + '/' + str(item)) == False:
                        zip_ref.extract(member = str(item), path = rvglpath)
                        print('Extracting ' + str(item))
                    elif overwriteFiles == 0:
                        overwrite = input(filename + ' already exists. Overwrite?\ny: yes\nn: no\na: all\ns: skip all')
                        over_string = str(overwrite).replace(' ', '').lower()
                        if over_string == 'y':
                            zip_ref.extract(member = str(item), path = rvglpath)
                            print('Extracting ' + str(item))
                        elif over_string == 'n':
                            print (str(item) + 'not extracted')
                        elif over_string == 'a':
                            overwriteFiles = 1
                        elif over_string == 's':
                            print('No duplicates will be extracted or overwritten')
                            overwriteFiles = -1
                            print('Skipping ' + str(item))
                    elif overwriteFiles == 1:
                        zip_ref.extract(member = str(item), path = rvglpath)
                        print('Overwriting ' + str(item))
                    elif overwriteFiles == -1:
                        print('Skipping ' + str(item))
                print('files are unzipped')'''

            with zipfile.ZipFile('./rvz' + contid + '_dl.zip' , 'r') as zip_ref:
                zip_ref.extractall(rvglpath)
            os.remove('./rvz' + contid + '_dl.zip' )
            dlState = 'Downloaded'
        except urllib.error.HTTPError:
            print('ID does not exist')
            dlState = 'Content not found'


def randomize():
    html_doc = requests.get('http://revoltzone.net/randomizer.php').content
    soup = BeautifulSoup(html_doc, 'html.parser')
    nice = soup.prettify()
    #print(nice)
    proplist = nice.split('\r\n')
    a = 1
    #print(proplist)
    global trackname
    global trackID
    global trackURL
    global trackgfx
    global tracklength
    global trackType
    global carname
    global carID
    global carURL
    global cargfx
    global carrating
    for line in proplist:
        if a == 2:
            trackname = str(line)
        if a == 4:
            tracklength = str(line).replace(' Meters', '' )
        if a == 5:
            trackType = str(line)
        if a == 6:
            trackURL = str(line).replace('http://revoltzone.net/', '')
            trackID = trackURL.split('/')[1]
        if a == 7:
            trackgfx = str(line).replace('\n', '')
        if a == 11:
            carname = str(line)
        if a == 13:
            carrating = str(line)
        if a == 15:
            carURL = str(line).replace('http://revoltzone.net/', '')
            carID = carURL.split('/')[1]
        if a == 16:
            cargfx = str(line).replace('\n', '')
        a += 1
    print(trackname + ' ' + tracklength + ' ' + trackType + ' ' + trackURL + ' ' + trackID)
    print(carname + ' ' + carrating + ' ' + carURL + ' ' + carID + ' ' + cargfx)
    print(cargfx + 'sjfadfjskjdfsakj')

def getTrackImgURL(contenturl):
    global trackgfx
    t=urllib.parse.quote(trackgfx,safe=':/_')
    urllib.request.urlretrieve(t, 'track.png')
    return 'track.png'


def getCarImgURL(contenturl):
    global cargfx
    c=urllib.parse.quote(cargfx,safe=':/_')
    print(c)
    urllib.request.urlretrieve(c, '.carpng')
    return 'car.png'
       

#randomize()


def fixcases():
    os.chdir(rvglpath)
    os.system('./fix_cases')
    os.chdir(workingpath)



#for CLI use
#modequery = input('0: randomizer\n1: download based on ID\nWhich mode do you choose? ')
#if str(modequery) == '0':
    #randomize()
#elif str(modequery) == '1':
    #modids = str(input('What are the IDs of the tracks/cars')).replace(' ', '').split(',')
    #for item in modids:
        #dl_content(contid = item)

#get_length(9172)



#workingpath = os.path.dirname(os.path.abspath(__file__))
##print(workingpath)
#os.chdir(workingpath)

#trackid = input('What are the IDs of the tracks? (seperated by commas)').replace(' ', '').split(',')

#for item in trackid:
    #os.system('wget http://revoltzone.net/sitescripts/dload.php?id=' + str(item))
    #os.system('unzip dload.php?id=' + str(item))
    #os.remove('dload.php?id=' + str(item))
