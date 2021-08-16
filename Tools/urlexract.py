import re
from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup, dammit
from firebase import firebase
from requests.api import post
from requests.models import Response
import os


def extractTableNames(firebase):

    firebase = firebase.FirebaseApplication(
        "https://telelinking-techfarm-default-rtdb.firebaseio.com/", None)
    ResultSet = firebase.get(
        "https://telelinking-techfarm-default-rtdb.firebaseio.com/", None)
    return ResultSet.keys()


def addTableNameIntotxt():
    tableNames = extractTableNames(firebase)

    fileallurl = open("data/allurl.txt", "w", encoding="UTF-8")
    try:
        fileposted = open("data/posted.txt", "r")
    except:
        open("data/posted.txt", "w").close()
        fileposted = open("data/posted.txt", "r")

    filetopost = open("data/topost.txt", "w", encoding="UTF-8")
    postedtitle = fileposted.readlines()
    print(postedtitle)
    for i in tableNames:
        fileallurl.write(i+"\n")
        try:
            postedtitle.index(i+"\n")
            print(i)
        except:
            filetopost.write(i+"\n")
    fileallurl.close()


if __name__ == "__main__":
    try:
        os.mkdir("data")
    except:
        pass
    addTableNameIntotxt()

    # filetest=open("test.txt","w",encoding="UTF-8")
    # filetest.write("😋")
