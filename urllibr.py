# -*- coding: utf-8 -*-
# une documentation sur urllib
import codecs
import json
import urllib.request
import urllib.parse
        
# v1.4/summoner/by-name/
key = "0fc699fb-4dbf-4cee-93d7-9317c8e35c22"
# riot api v1.4
url = "https://euw.api.pvp.net/"
url2 = "https://global.api.pvp.net/"
url3 = "http://ddragon.leagueoflegends.com/cdn/img"
url4 = "http://ddragon.leagueoflegends.com/cdn/5.24.2/img"
list_images = ["/champion/splash/","/champion/loading/"]
# list_images[0] = wallpaper
# list_images[1] = loadingscreen
vertion = {
            "observer-mode/rest/featured/": [],
            
            "api/lol/static-data/euw/v1.2/": [
                                  # problémme apres le ?
                                  "champion", # EX: /champion/{id}
                                  "item" ,
                                  "map",
                                  "mastery",
                                  "rune",
                                  "summoner-spell"],
            
            "api/lol/euw/v1.3/": [
                                "game/by-summoner/id/recent",   
                                "stats/by-summoner/id/ranked?",
                                "stats/by-summoner/id/summary?"
                                ], 
                                            
            "api/lol/euw/v1.4/summoner/":[ 
                                "by-name/summoner-name",
                                "id", 
                                "id/masteries?",
                                "id/name?",
                                "id/runes?"]}

# arg for static data fanctions
static_data = {
            "?champData=":[
                          "all&","allytips&","altimages&",
                          "blurb&","enemytips&","image&",
                          "info&","lore&","partype&",
                          "passive&","recommended&","skins&",
                          "spells&","stats&","tags&"
                         ],
            
            "?itemListData=":[
                            "all&","colloq&","consumeOnFull&",
                            "consumed&","depth&","effect&",
                            "from&","gold&","hideFromAll&",
                            "image&","inStore&","into&",
                            "maps&","requiredChampion&","sanitizedDescription&",
                            "specialRecipe&","stacks&","stats&","tree&"
                             ],
            
            "?masteryListData=":[
                                "all&","image&","masteryTree&",
                                "prereq&","ranks&","sanitizedDescription&",
                                "tree&"
                                ],
            
            "?runeListData=":[
                             "all&","basic&","colloq&",
                             "consumeOnFull&","consumed&","depth&",
                             "from&","gold&","hideFromAll&","image&",
                             "inStore&","into&","maps&","requiredChampion&",
                             "sanitizedDescription&","specialRecipe&",
                             "stacks&","stats&","tags&"
                             ],
            
            "?spellData=":[
                          "all&","cooldown&","cooldownBurn&",
                          "cost&","costBurn&","costType&","effect&",
                          "effectBurn&","image&","key&","leveltip&",
                          "maxrank&","modes&","range&","rangeBurn&",
                          "resource&","sanitizedDescription&",
                          "sanitizedTooltip&","tooltip&","vars&"
                          ],}


#-----------------------------------------------------
urls = {}
#-----------------------------------------------------
# params for champ played ranked & champ played normal
season = ["SEASON2014","SEASON2015"]
#---------------------------------------------------

class data :
    def __init__(self,summoners_name = None):
        self.summoners_name = summoners_name

#----------------------------------------V1.4---------------------------- 
    def get_summoner_info(self):
        name = vertion["api/lol/euw/v1.4/summoner/"][0]
        # index of "api/lol/euw/v1.4/summoner/" is unknown becos vertion is a dictionary
        
        self.vertion_url = list(
                vertion.keys())[list(
                    vertion.keys()).index("api/lol/euw/v1.4/summoner/")]
        
        name = name.replace("summoner-name",self.summoners_name)
        final_url = url + self.vertion_url + name + "?locale=fr_FR&api_key=" + key
        urls["info"] = final_url
        respens = urllib.request.urlopen(final_url)
        json_object = respens.readall().decode("utf-8")
        self.read = json.loads(json_object)
        return self.read

    def get_summoner_masteries (self):

        self.get_summoner_info()
        
        self.masteries_url = url + self.vertion_url +str(
                self.read[self.summoners_name]["id"]
                ) +"/masteries?locale=fr_FR&api_key="+key

        urls["mesteries"] = self.masteries_url
        respens = urllib.request.urlopen(self.masteries_url)
        json_object = respens.readall().decode("utf-8")
        read = json.loads(json_object)
        return read
    def get_summoner_by_id (self):
        vertion_url = list(
                vertion.keys())[list(vertion.keys()
                    ).index("api/lol/euw/v1.4/summoner/")]     
            
        # summoners_name = id
        final_url = url+vertion_url+str(self.summoners_name)+"?locale=fr_FR&api_key="+key
        urls["summoner_by_id"] = final_url
        respens = urllib.request.urlopen(final_url)
        json_object = respens.readall().decode("utf-8")
        read = json.loads(json_object)
        return read
    
    def get_summoner_name(self) :
        self.get_summoner_masteries()
        name_url = self.masteries_url
        name_url = name_url.replace("masteries","name")
        urls["summoner_name"] = name_url
        respens = urllib.request.urlopen(name_url)
        json_object = respens.readall().decode("utf-8")
        read = json.loads(json_object)
        return read
    
    def get_summoner_runes (self):
        self.get_summoner_masteries()
        runes_url = self.masteries_url
        runes_url = runes_url.replace("masteries","runes")
        urls["runes_url"] = runes_url
        respens = urllib.request.urlopen(runes_url)
        json_object = respens.readall().decode("utf-8")
        read = json.loads(json_object)
        return read
#-------------------------V1.3-----------------------------------
    def get_recent_historique(self):
        path = vertion["api/lol/euw/v1.3/"][0]
        vertion_url = list(
                vertion.keys())[list(
                    vertion.keys()).index("api/lol/euw/v1.3/")]
        ID = self.summoners_name
        path = path.replace("id",ID)
        final_url = url + vertion_url+ path + "?locale=fr_FR&api_key="+key
        urls["historique"] = final_url
        respens = urllib.request.urlopen(final_url)
        json_object = respens.readall().decode("utf-8")
        read = json.loads(json_object)
        return read

    def champ_played_ranked (self,season_played):
        # 1 parameter to __init__   :the ID
        # 1 parameter to the fanction    : the season
        self.season = season_played
        path = vertion["api/lol/euw/v1.3/"][1] 
        vertion_url = list(
                vertion.keys())[list(
                    vertion.keys()).index("api/lol/euw/v1.3/")]

        ID = self.summoners_name
        path = path.replace("id",ID)
        final_url = url+vertion_url+path+"?locale=fr_FR&season="+self.season+"&api_key="+key
        urls["played_ranked"] = final_url
        respens = urllib.request.urlopen(final_url)
        json_object = respens.readall().decode("utf-8")
        read = json.loads(json_object)
        return read

    def champ_played_normal (self,season_played):
        self.season = season_played
        path = vertion["api/lol/euw/v1.3/"][2]
        vertion_url = list(
                vertion.keys())[list(
                    vertion.keys()).index("api/lol/euw/v1.3/")]
        
        ID = self.summoners_name
        path = path.replace("id",ID)
        final_url = url+vertion_url+path+"?locale=fr_FR&season="+self+season+"&api_key="+key
        urls["played_normal"] = final_url
        respens = urllib.request.urlopen(final_url)
        json_object = respens.readall().decode("utf-8")
        read = json.loads(json_object)
        return read
#-----------------------------V1.2-------------------------------------------------
    def static_data_champion (self,champ_data = None,ID = None):
        # champ_data = static_data[index]  default = None
        self.champ_data = champ_data
        # path = champion
        path = vertion["api/lol/static-data/euw/v1.2/"][0]
        # vertion_url =  "api/lol/static-data/euw/v1.2/"
        vertion_url = list(
                vertion.keys())[list(
                    vertion.keys()).index("api/lol/static-data/euw/v1.2/")]
    
        if champ_data == None :
            if ID == None:
                final_url = url2+vertion_url+path+"?locale=fr_FR&api_key="+key
            else :
                final_url = url2+vertion_url+path+"/"+ID+"?locale=fr_FR&api_key="+key
        else :
            if ID == None :
                final_url =url2+vertion_url+path+"?locale=fr_FR&champData="+self.champ_data+"&api_key="+key
            else :
                final_url =url2+vertion_url+path+"/"+str(ID)+"?locale=fr_FR&champData="+self.champ_data+"&api_key="+key
        urls["data_champion"] = final_url
        respens = urllib.request.urlopen(final_url)
        json_object = respens.readall().decode("utf-8")
        read = json.loads(json_object)
        return read
    
    def static_data_item (self,item_data = None,ID = None):
        self.item_data = item_data
        path = vertion["api/lol/static-data/euw/v1.2/"][1]
        vertion_url = list(
                vertion.keys())[list(
                    vertion.keys()).index("api/lol/static-data/euw/v1.2/")]
        
        if item_data == None :
            if ID == None :
                final_url = url2+vertion_url+path+"?locale=fr_FR&api_key="+key
            else :
                final_url = url2+vertion_url+path+"/"+str(ID)+"?locale=fr_FR&api_key"+key
        else :
            if ID == None :
                final_url = url2+vertion_url+path+"?locale=fr_FR&itemData="+self.item_data+"&api_key="+key
            else:
                final_url = url2+vertion_url+path+"/"+str(ID)+"?locale=fr_FR&itemData="+self.item_data+"&api_key="+key
        urls["data_item"] = final_url
        respens = urllib.request.urlopen(final_url) 
        json_object = respens.readall().decode("utf-8")
        read = json.loads(json_object)
        return read

    def static_data_map (self) :
        path = vertion["api/lol/static-data/euw/v1.2/"][2]
        vertion_url = list(
                vertion.keys())[list(
                    vertion.keys()).index("api/lol/static-data/euw/v1.2/")]    

        final_url = url2+vertion_url+path+"?locale=fr_FR&api_key="+key
        urls["data_map"] = final_url
        respens = urllib.request.urlopen(final_url)
        json_object = respens.readall().decode("utf-8")
        read = json.loads(json_object)
        return read

    def static_data_masteries (self,masteries_data=None,ID=None):
        self.masteries_data = masteries_data
        path = vertion["api/lol/static-data/euw/v1.2/"][3]
        vertion_url = list(
                vertion.keys())[list(
                    vertion.keys()).index("api/lol/static-data/euw/v1.2/")]

        if masteries_data == None :
            if ID == None :
                final_url = url2+vertion_url+path+"?locale=fr_FR&api_key="+key
            else :
                final_url = url2+vertion_url+path+"/"+str(ID)+"?locale=fr_FR&api_key="+key
        else :
            if ID == None :
                final_url = url2+vertion_url+path+"?locale=fr_FR&masteryListData="+masteries_data+"&api_key="+key
            else :
                final_url=url2+vertion_url+path+"/"+str(ID)+"?locale=fr_FR&masteryListData="+masteries_data+"&api_key="+key
        urls["data_masteries"] = final_url
        respens = urllib.request.urlopen(final_url)
        json_object = respens.readall().decode("utf-8")
        read = json.loads(json_object)
        return read


    def static_data_runes (self,runes_data=None,ID=None):
        self.runes_data = runes_data
        path = vertion["api/lol/static-data/euw/v1.2/"][4]
        vertion_url = list(
                vertion.keys())[list(
                    vertion.keys()).index("api/lol/static-data/euw/v1.2/")]

        if runes_data == None :
            if ID == None :
                final_url = url2+vertion_url+path+"?locale=fr_FR&api_key="+key
            else :
                final_url = url2+vertion_url+path+"/"+str(ID)+"?locale=fr_FR&api_key="+key
        else :
            if ID == None :
                final_url = url2+vertion_url+path+"?locale=fr_FR&runeData="+runes_data+"&api_key="+key
            else :
                final_url = url2+vertion_url+path+"/"+str(ID)+"?locale=fr_FR&runeData="+runes_data+"&api_key="+key

        urls["data_runes"] = final_url
        respens = urllib.request.urlopen(final_url)
        json_object = respens.readall().decode("utf-8")
        read = json.loads(json_object)
        return read

    def static_summoner_spell (self,spell_data=None,ID=None):
        self.spell_data = spell_data
        path = vertion["api/lol/static-data/euw/v1.2/"][5]
        vertion_url = list(
                vertion.keys())[list(
                    vertion.keys()).index("api/lol/static-data/euw/v1.2/")]

        if spell_data == None :
            if ID == None :
                final_url = url2+vertion_url+path+"?locale=fr_FR&api_key="+key
            else :
                final_url = url2+vertion_url+path+"/"+ID+"?locale=fr_FR&api_key="+key
        else :
            if ID == None :
                final_url = url2+vertion_url+path+"?locale=fr_FR&spellData="+spell_data+"&api_key="+key
            else :
                final_url = url2+vertion_url+path+"/"+ID+"?locale=fr_FR&spellData="+spell_data+"&api_key="+key

        urls["summoner_spell"] = final_url
        respens = urllib.request.urlopen(final_url)
        json_onject = respens.readall().decode("utf-8")
        read = json.loads(json_onject)
        return read
#-------------------------------V1.0-----------------------------------
    def observer_mod (self):
        final_url = url+"observer-mode/rest/featured?"+"api_key="+key
        urls["observer_mod"] = final_url
        respens = urllib.request.urlopen(final_url)
        json_object = respens.readall().decode("utf-8")
        read = json.loads(json_object)
        return read
#----------------------------------------------------------------------
    def get_loading_screen (self,champion_object,num=0):
        a = champion_object
        skin = a["skins"]
        name = self.static_data_champion(static_data["?champData="][6])
        name = a["name"]+"_{}.jpg".format(num)
        final_url = url3+list_images[1]+name
        return final_url
    
    def get_wallpaper (self,champion_object,num=0):
        a = champion_object
        skin = a["skins"]
        
        name = self.static_data_champion(static_data["?champData="][6])
        name = a["name"]+"_{}.jpg".format(num)
        final_url = url3+list_images[0]+name
        return final_url
    
    def champ_icons (self,champion_object):
        a = champion_object
        final_url=url4+"/champion/"+a["image"]["full"] 
        return final_url
   
    def itemes_icons (self,icon_object):
        a = icon_object
        final_url = url4+"/item/"+a["image"]["full"]
        return final_url
    
    def masteries_icon (self,masteries_object):
        a = masteries_object
        final_url = url4+"/mastery/"+"{}.png".format(str(a["id"]))
        return final_url
    
    def runes_icon (self,runes_object):
        a = runes_object
        final_url = url4+"/rune/"+a["image"]["full"]
        return final_url
    
    def passives_icon(self,passives_object):
        a = passives_object
        final_url = url4+"/passive/"+a["passive"]["image"]["full"]
        return final_url
    
    def spells_icon(self,spells_object,key): # key == la touche du clavier
        a = spells_object 
        final_url = "{}/spell/{}".format(url4,a["spells"][key]["image"]["full"])
        return final_url

    def map_image (self,map_object,key): # key == the number of the map
        a = map_object 
        final_url = "{}/map/{}".format(url4,a["data"][str(key)]["image"]["full"])
        return final_url

# {name:id}
dict_champ = {}
dict_item = {}
dict_masterie = {}
dict_runes = {}
dict_spell = {"A":0,"Z":1,"E":2,"R":3}
map_key = {"1":1,"2":10,"3":8,"4":11,"5":12}
riot_object = data("gosim25")

# {champ : id}
#--------------------------------------------------------------------------
"""
all_champ = riot_object.static_data_champion(static_data["?champData="][6])
all_champ = all_champ["data"]
for i in all_champ.keys() :
    dict_champ[i]=all_champ[i]["id"]
# write -- champ : id -- in a file 
with open('data_champ.json', 'w') as outfile:
        json.dump(dict_champ, outfile)
"""
#--------------------------------------------------------------------------
"""
all_item = riot_object.static_data_item(static_data["?itemListData="][0])["data"]
for i in all_item.keys():
    dict_item[all_item[i]["name"]] = int(i)
with codecs.open("data_item.json","w",encoding="utf-8") as outfile :
    json.dump(dict_item,outfile)
"""
#------------------------------------------------------------------------------
"""
all_masteries = riot_object.static_data_masteries(static_data["?masteryListData="][0])["data"]
for i in all_masteries.keys():
    dict_masterie[all_masteries[i]["name"]] = int(i)
with codecs.open("data_masteries.json","w",encoding="utf-8") as outfile :
    json.dump(dict_masterie,outfile)
"""
#---------------------------------------------------------------------------------
"""
all_runes = riot_object.static_data_runes(static_data["?runeListData="][0])["data"]
for i in all_runes.keys():
    dict_runes[all_runes[i]["name"]]=int(i)
with codecs.open("data_runes.json","w",encoding="utf-8") as outfile:
    json.dump(dict_runes,outfile)
"""
#--------------------------------item-------------------------------------------------
file_item = codecs.open("data_item.json","r",encoding="utf-8")
json_item = file_item.read()
data_item = json.loads(json_item)
#------------------------------champ-------------------------------------------
file_champ = codecs.open("data_champ.json","r",encoding="utf-8")
json_champ = file_champ.read()
data_champ = json.loads(json_champ)
#-------------------------masteries-------------------------------------------
file_masterie = codecs.open("data_masteries.json","r",encoding="utf-8")
json_masteries = file_masterie.read()
data_masterie = json.loads(json_masteries)
#-------------------------runes----------------------------------------------
file_rune= codecs.open("data_runes.json","r",encoding="utf-8")
json_runes = file_rune.read()
data_rune = json.loads(json_runes)
#-----------------------------------------------------------------------
champ =  riot_object.static_data_champion(static_data["?champData="][0],data_champ["Thresh"])
champ_icon = riot_object.champ_icons(champ)
champ_passive_icon = riot_object.passives_icon(champ)
champ_spell_icon = riot_object.spells_icon(champ,dict_spell["R"])
#---------------------------------------------------------------------------
item = riot_object.static_data_item(static_data["?itemListData="][9],
        data_item["Enchantement : Dévoreur"])
item_icon = riot_object.itemes_icons(item)
#-----------------------------------------------------------------------------
masterie = riot_object.static_data_masteries(static_data["?masteryListData="][1],
        data_masterie["Épée à double tranchant"])
masterie_icon = riot_object.masteries_icon(masterie)
#-------------------------------------------------------------------------------
rune = riot_object.static_data_runes(static_data["?runeListData="][9],
        data_rune["Quintessence de puissance"])
rune_icon = riot_object.runes_icon(rune)
#------------------------------------------------------------------------------
mapp = riot_object.static_data_map()
map_icon = riot_object.map_image(mapp,map_key["1"])


print(item_icon)
print(champ_icon)
print(masterie_icon)
print(rune_icon)
print(champ_passive_icon)
print(champ_spell_icon)
print(map_icon)
file_champ.close()
file_item.close()
file_masterie.close()



"""
-------------------------------------------------------------------

riot_object = data()
a = riot_object.static_data_champion()
b = riot_object.static_data_champion(static_data["?champData="][0],"121")
print(b) 
-------------------------------------------------------------------
--------- to get the games played with the champions in a season---
riot_object = data("43992962")
a = riot_object.champ_played_ranked(season[0])
print(a)
------------------------------------------------------------------
----------to get summoner by id ----------------------------------

riot_object = data("43992962") 
a = riot_object.get_summoner_by_id()
print(a)
----------to get images------------------------------------------
wallpaper = riot_object.get_wallpaper(champ,1)
loading = riot_object.get_loading_screen(champ,4)
------------------------------------------------------------------
"""


