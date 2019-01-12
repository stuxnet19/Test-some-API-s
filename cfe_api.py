import json
from urllib.request import *

# création d'une api qui donne tout les réstaurent
# présent dans un pays ou une ville

locu_api = 'fd179221f9c69f13a27ecbfef6fd1e2c03ce50f1'

url = 'https://api.locu.com/v1_0/venue/search/?locality=NEW%20YORK&api_key=fd179221f9c69f13a27ecbfef6fd1e2c03ce50f1'
# ouvrire l'url
respens =  urlopen(url)
# transform it so str obj
json_object = respens.read  ().decode('utf-8')
# loads : arg = str_obj
# load : arg = file_stream_obj
data = json.loads(json_object)
# print (data['objects'])
# to print all objects == restorent in data
for restorent in data['objects']:
    print (restorent)
print("---------------------------------------------------------------------")

for restorent in data['objects']:
    print ("{} \n{} : {} ".format(
        restorent['locality'],restorent['name'],restorent['phone'])
        )

def locu_search(region,country):
    api_key = locu_api
    addr ='https://api.locu.com/v1_0/venue/search/?'
    if country == None :
        try:
            locality = region.replace(' ',"%20")
            final_addr = addr +"locality="+ locality + "&api_key="+api_key
            respens = urlopen(final_addr)
            json_object = respens.readall().decode('utf-8')
            data = json.loads(json_object)
        except AttributeError :
            pass
    if region == None :
        try :
            locality = country.replace(' ',"%20")
            final_addr = addr +"country=" +locality + "&api_key="+api_key
            respens = urlopen(final_addr)
            json_object = respens.readall().decode('utf-8')
            data = json.loads(json_object)
        except AttributeError :
            pass

    for element in data['objects']:
        print ("---------{}---------\n{} : {} ".format(
            element['locality'],element['name'],element['phone'])
            )

while True:
    pressiser =int(input(" tapez 1 pour préssiser le pays 2 pour la ville : "))
    if pressiser == 2 :
        print("---------------------------------------------------------------------")
        location = input("veillez taper le nom de la ville : ")
        location = location.upper()
        locu_search(location,None)
        fin = input("tapez fin pour quiter le programme :  ")
        if fin == 'fin':
            break
        else :
            pass
    if pressiser == 1 :
        print ("--------------------------------------------------------------------")
        location = input("veillez taper le nom du pays : ")
        location.upper()
        locu_search(None,location)
        fin = input("tapez -- fin -- pour quiter le programme :  ")

        if fin == 'fin':
            break
        else :
            pass
    else :
        print ("veillez recomencer SVP ")
