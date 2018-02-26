# -*- coding: utf-8 -*-
import pymongo
import json
import requests


"""
/r/deepfriedmemes
dataset of /r/deepfriedmemes' posts. 

Link:https://www.reddit.com/r/deepfriedmemes.json

Import:
    1) import json; requests
    2) store Json in var
    3) Use requests to get the json file from the URL + decode it
    4) use json to decode webpage to json 
    5) insert into db
"""
connection = pymongo.MongoClient("149.89.150.100")
db = connection["XD"]
db.drop_collection("deepfried")
collection = db["deepfried"]
url = "https://www.reddit.com/r/deepfriedmemes.json"
dictc = requests.get(url, headers = {"User-agent": "XD"})

d = dictc.json()
posts = d["data"]["children"]

for each in posts:
    collection.insert_one(each)

def stickied():
    x = collection.find({"data.stickied" : True})
    for each in x:
        print each
        print "###################"
    return x

def notstickied():
    x = collection.find({"data.stickied" : False})
    for each in x:
        print each
        print "###################"
    return x

def score(x):
    x = collection.find({"data.score" : {"$gt" : x}})
    for each in x:
        print each
        print "###################"
    return x

def upvotes(x):
    x = collection.find({"data.ups" : {"$gt" : x}})
    for each in x:
        print each
        print "###################"
    return x

def author(x):
    x = collection.find({"data.author" : x})
    for each in x:
        print each
        print "###################"
    return x


def bemoji():
    x = collection.find({"data.title" : {"$regex" : ".*🅱️.*i"}})
    for each in x:
        print (each["data"]["title"].encode("utf-8"))
        print "%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    return x
