import os
import re
from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup, dammit
from firebase import firebase
from requests.api import post
from requests.models import Response

try:
    os.mkdir("../data")
except:
    pass

databaseUrl = "https://telelinking-techfarm-default-rtdb.firebaseio.com/"

firebase = firebase.FirebaseApplication(databaseUrl, None)

def deleteTable(tableName,firebase):
    
    firebase.delete(
        databaseUrl+tableName, None)

def extractTableNames(firebase):
    
    ResultSet = firebase.get(databaseUrl, None)
    return ResultSet.keys()

   
def addTableNameIntotxt():

    tableNames=extractTableNames(firebase)
    try:fileallurl=open("../data/allurl.txt","a")
    except:
        open("../data/allurl.txt", "w").close()
        fileallurl = open("../data/allurl.txt", "a")
    try:
        fileposted=open("../data/posted.txt","r")
    except:
       open("../data/posted.txt", "w").close()
       fileposted = open("../data/posted.txt", "r")
    try:
        filetopost=open("../data/topost.txt","a")
    except:
        open("../data/topost.txt", "w").close()
        filetopost = open("../data/topost.txt", "a")
    postedtitle=fileposted.readlines()
    for i in tableNames:
        try:
            postedtitle.index(i+"\n")
        except:
            fileallurl.write(i+"\n")
            filetopost.write(i+"\n")
    fileallurl.close()

def checkDiff():
    fileallurl=open("data/allurl.txt","r")
    allTableNames=fileallurl.readlines()
    fileposted=open("data/posted.txt","r")
    allPostedName=fileposted.readlines()
    for i in allPostedName:
        try:allTableNames.index(i)
        except:print(i)


def exract(sitemapUrl):
    reqs = requests.get(sitemapUrl)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    postlinks = re.findall(r'<loc>(.+?)</loc>',
                          soup.prettify().replace("\n", "").replace(" ", ""))
    return postlinks

def findPostTitle():
    postLinks=[]
    fileposted=open("data/posted.txt","a")
    subsitemap = exract("https://www.walinking.link/sitemap.xml")
    for i in subsitemap:
        links=exract(i)
        postLinks=postLinks+links
    for t in postLinks:
        reqs = requests.get(t)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        title=soup.title.text
        print(title)
        fileposted.write(title+"\n")
    fileposted.close()


def extractUrlFormSites():

    url = "https://www.whatsapgrouplinks.com/sitemap_index.xml"
    sitemaps = exract(url)

    for i in sitemaps:
        postLinks=exract(i)
        for j in postLinks:
            reqs=requests.get(j)
            soup=BeautifulSoup(reqs.text,'html.parser')
            title=soup.title.text
            

addTableNameIntotxt()

# print("hell Whatsapp group".find("WhatsA"))
# deleteTable("18+ Adult WhatsApp Group Links")
