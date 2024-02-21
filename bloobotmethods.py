import bloobotclasses
import random
import json

def init_moons():
    itemlize = []
    file = open('moons.json')
    moondex = json.load(file)
    for i in moondex:
        moon = bloobotclasses.Moon()
        moon.fullname = moondex[i]['fullname']
        moon.difficulty = moondex[i]['difficulty']
        moon.risk = moondex[i]['risk']
        moon.cost = moondex[i]['cost']
        moon.minscrap = moondex[i]['minscrap']
        moon.maxscrap = moondex[i]['maxscrap']
        if moon.fullname == "71-Gordion":
            moon.weather = "Mild"
        else:
            moon.weather = weather_select()
        itemlize.append(moon)
    return itemlize

def init_store():
    storelize = []
    file = open('store.json')
    storedex = json.load(file)
    for i in storedex:
        equip = bloobotclasses.Item()
        equip.fullname = storedex[i]['fullname']
        equip.price = storedex[i]['price']
        storelize.append(equip)
    return storelize

def init_scrap():
    droptable = []
    file = open('scrap.json')
    scrapdex = json.load(file)
    for i in scrapdex:
        scrap = bloobotclasses.Scrap()
        scrap.fullname = scrapdex[i]['fullname']
        scrap.maxval = scrapdex[i]['maxval']
        scrap.minval = scrapdex[i]['minval']
        droptable.append(scrap)
    return droptable

def lookupdex(name,lister):
    for i in lister:
        if i.fullname == name:
            return i
    return None

def weather_select():
    roll = random.randint(1, 6)
    if roll == 1:
        return "Mild"
    elif roll == 2:
        return "Rainy"
    elif roll == 3:
        return "Stormy"
    elif roll == 4:
        return "Foggy"
    elif roll == 5:
        return "Flooded"
    elif roll == 6:
        return "Eclipsed"
        
def loot_percent():
    dropsdex = []
    file = open('moondrops.json')
    gendex = json.load(file)
    currentindex = 0
    #10,000 | * by 100
    for i in gendex:
        drops = []
        for y in gendex[i]:
            drop = bloobotclasses.Drop
            drop.fullname = y
            drop.prev = currentindex
            drop.curr = gendex[i][y] * 100 - 1
            currentindex = drop.curr + 1
            drops.append(drop)
        dropsdex.append(drops)
    return drops
