import os
from bs4 import BeautifulSoup
import requests
import urllib.request
import zipfile

rvglpath = '/rvgl/path/here'
global trackno
global carno

def dl_content(contid):
# Download the file from `url` and save it locally under `file_name`:
    print('Downloading...')
    workingpath = os.path.dirname(os.path.abspath(__file__))
    os.chdir(workingpath)
    urllib.request.urlretrieve('http://revoltzone.net/sitescripts/dload.php?id=' + contid, 'rvz' + contid + '_dl.zip')
    print('Content downloaded')
    with zipfile.ZipFile('./rvz' + contid + '_dl.zip' , 'r') as zip_ref:
        zip_ref.extractall(rvglpath)
    os.remove('./rvz' + contid + '_dl.zip' )

def get_length(trackurl, trackid, trackname):
    html_doc2 = requests.get('http://revoltzone.net/' + str(trackurl)).content
    soup2 = BeautifulSoup(html_doc2, 'html.parser')
    for link in soup2.find_all(id='right'):
        #print(link.get_text())
        if 'Meters' in str(link.get_text()):
            #print('Da length line')
            global tracklength
            tracklength = str(link.get_text()).replace(' ', '').replace('Meters', '')
            #print('Length: ' + tracklength)

def get_type(trackurl, trackid, trackname):
    html_doc2 = requests.get('http://revoltzone.net/' + str(trackurl)).content
    soup2 = BeautifulSoup(html_doc2, 'html.parser')
    for link in soup2.find_all(id='right'):
        #print(link.get_text())
        if 'Meters' in str(link.get_text()):
            #print('Da length line')
            global tracklength
            tracklength = str(link.get_text()).replace(' ', '').replace('Meters', '')
            #print('Length: ' + tracklength)


def randomize():
    html_doc = requests.get('http://revoltzone.net/').content
    soup = BeautifulSoup(html_doc, 'html.parser')
    foundings = soup.find(id='invisi2')
    #print(foundings)
    for link in foundings.find_all('a'):
        print('URL: ' + link.get('href'))
        contenturl = link.get('href')
        source = link.get('href').split('/')
        contentid = str(source[1])
        contentname = str(source[2])
        
        if str(source[0]) == 'tracks':
            print("It's a track!")
            get_length(trackurl = contenturl, trackid = contentid, trackname = contentname)
            print('Name: ' + contentname + '\nLength: ' + tracklength)
            dl_content(contid = contentid)
        
        if str(source[0]) == 'cars':
            print("It's a car!")
            print('Name: ' + contentname)
            dl_content(contid = contentid)


#for CLI use           
modequery = input('0: randomizer\n1: download based on ID\nWhich mode do you choose? ')
if str(modequery) == '0':
    randomize()
elif str(modequery) == '1':
    modids = str(input('What are the IDs of the tracks/cars')).replace(' ', '').split(',')
    for item in modids:
        dl_content(contid = item)

#get_length(9172)



#workingpath = os.path.dirname(os.path.abspath(__file__))
##print(workingpath)
#os.chdir(workingpath)

#trackid = input('What are the IDs of the tracks? (seperated by commas)').replace(' ', '').split(',')

#for item in trackid:
    #os.system('wget http://revoltzone.net/sitescripts/dload.php?id=' + str(item))
    #os.system('unzip dload.php?id=' + str(item))
    #os.remove('dload.php?id=' + str(item))
