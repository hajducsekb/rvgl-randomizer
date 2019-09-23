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





def dl_content(contid):
# Download the file from `url` and save it locally under `file_name`:
    print('Downloading...')
    global dlState
    try:
        urllib.request.urlretrieve('http://revoltzone.net/sitescripts/dload.php?id=' + contid, 'rvz' + contid + '_dl.zip')
        print('Content downloaded')
        with zipfile.ZipFile('./rvz' + contid + '_dl.zip' , 'r') as zip_ref:
            zip_elem = zip_ref.namelist()
            #print(zip_elem)
            overwriteFiles = 0
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
            print('files are unzipped')

        '''with zipfile.ZipFile('./rvz' + contid + '_dl.zip' , 'r') as zip_ref:
            zip_ref.extractall(rvglpath)'''
        os.remove('./rvz' + contid + '_dl.zip' )
        dlState = 'Downloaded'
    except urllib.error.HTTPError:
        print('ID does not exist')
        dlState = 'Content not found'

def get_length(trackurl, trackid, trackname):
    html_doc2 = requests.get('http://revoltzone.net/' + str(trackurl)).content
    soup2 = BeautifulSoup(html_doc2, 'html.parser')
    for link in soup2.find_all(id='right'):
        #print(link.get_text())
        if 'Meters' in str(link.get_text()):
            #print('Da length line')
            global tracklength
            tracklength = str(link.get_text()).replace(' ', '').replace('Meters', '')
            print('Length: ' + tracklength)
            return tracklength

def get_category(trackurl, trackid, trackname):
    html_doc2 = requests.get('http://revoltzone.net/' + str(trackurl)).content
    soup2 = BeautifulSoup(html_doc2, 'html.parser')
    lineno = 0
    for link in soup2.find_all(id='right'):
        #print(link.get_text())
        lineno += 1
        if lineno == 5:
            global trackType
            #print('Da length line')
            trackType = str(link.get_text()).replace(' ', '')
            #print('Length: ' + tracklength)
            print('Category: ' + trackType)
            return trackType

def get_rating(carurl, carid, carname):
    html_doc3 = requests.get('http://revoltzone.net/' + str(carurl)).content
    soup4 = BeautifulSoup(html_doc3, 'html.parser')
    lineno = 0
    for link in soup4.find_all(id='right'):
        #print(link.get_text())
        lineno += 1
        if lineno == 6:
            global carrating
            #print('Da length line')
            carrating = str(link.get_text()).replace(' ', '')
            #print('Length: ' + tracklength)
            print('Category: ' + carrating)
            return carrating

def randomize():
    html_doc = requests.get('http://revoltzone.net/').content
    soup = BeautifulSoup(html_doc, 'html.parser')
    foundings = soup.find(id='invisi2')
    #print(foundings)
    for link in foundings.find_all('a'):
        print('URL: ' + link.get('href'))
        contenturl = link.get('href')
        source = link.get('href').split('/')
        global contentid
        global contentname
        contentid = str(source[1])
        contentname = str(source[2])


        if str(source[0]) == 'tracks':
            print("It's a track!")
            get_length(trackurl = contenturl, trackid = contentid, trackname = contentname)
            get_category(trackurl = contenturl, trackid = contentid, trackname = contentname)
            global trackgfx
            trackgfx = str(link.find('img').get('src'))
            print('Name: ' + contentname + '\nLength: ' + tracklength)
            global trackname
            global trackID
            global trackURL
            trackname = contentname
            trackID=contentid
            trackURL=contenturl
            #dl_content(contid = contentid)

        if str(source[0]) == 'cars':
            get_rating(carurl = contenturl, carid = contentid, carname = contentname)
            global cargfx
            cargfx = str(link.find('img').get('src'))
            global carname
            global carID
            global carURL
            carname = contentname
            carID = contentid
            carURL= contenturl
            print("It's a car!")
            print('Name: ' + contentname)
            #dl_content(contid = contentid)

def getTrackImgURL(contenturl):
    global trackgfx
    t=urllib.parse.quote(trackgfx,safe=':/_')
    urllib.request.urlretrieve(t, 'track.png')
    return 'track.png'


def getCarImgURL(contenturl):
    global cargfx
    c=urllib.parse.quote(cargfx,safe=':/_')
    urllib.request.urlretrieve(c, 'car.png')
    return 'car.png'

def fixcases():
    os.chdir(rvglpath)
    os.system('./fix_cases')
    os.chdir(workingpath)

#getCarImgURL('cars/3142/ToyLamb')
#randomize()

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
