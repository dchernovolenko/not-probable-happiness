import pymongo

connection = pymongo.MongoClient("149.89.150.100")
db = connection["test"]
collection = db["restaurants"]
def findborough(borough):
    rinbo = collection.find({"borough" : borough})
    l = list()
    for x in rinbo:
        l.append(x)
        #print x["name"]
    return l

def findzip(zipcd):
    rinbo = collection.find({"address.zipcode" : zipcd})
    l = list()
    for x in rinbo:
        l.append(x)
        #print x["name"]
    return l

def findzipgrade(zipcd, grade):
    rinbo = collection.find({"address.zipcode" : zipcd, "grades.grade" : grade})
    l = list()
    for x in rinbo:
        l.append(x)
        #print x["name"]
    return l

def findziplower(zipcd, score):
    rinbo = collection.find({"address.zipcode" : zipcd, "grades.score" : {"$lt" : score}})
    l = list()
    for x in rinbo:
        l.append(x)
        #print x["name"]
    return l

#finds restaurants of a certain cuisine in a zip with a grade greater than the input
def findcuisinezipscore(c, zipcd, score):
    rinbo = collection.find({"cuisine" : c, "address.zipcode" : zipcd, "grades.score" : {"$gt" : score}})
    l = list()
    for x in rinbo:
        l.append(x)
        #print x["name"]
    return l

#testing
"""
findborough("Staten Island")
print "===================="
findzip("10305")
print "===================="
findzipgrade("10305", "C")
print "===================="
findziplower("10305", 10)
print "===================="
findcuisinezipscore("American", "10305", 10)
"""

