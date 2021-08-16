import re
from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup, dammit
from firebase import firebase
import pyrebase
from requests.models import ReadTimeoutError
from firebase import firebase

databaseUrl = "https://telelinking-techfarm-default-rtdb.firebaseio.com/"
mainSitemapUrl = "https://telegrouplink.com/sitemap_index.xml"

def isdataexit(tableName, data,dataBase):
    ResultSet = dataBase.get(
        databaseUrl, tableName,)
    if(ResultSet == None):
        return 0
    groupLinksList=[]
    # print(ResultSet.values())
    for p_id, p_info in ResultSet.items():
        groupLinksList.append(p_info['groupLink'])
    try:
        groupLinksList.index(data['groupLink'])
        return 1
    except:
        return 0


def insertData(tableName, data, dataBase, format="post"):
    if(format == "patch"):
        result = dataBase.patch(tableName, data)
    else:
        result = dataBase.post(tableName, data)


def exract(sitemapUrl):
    reqs = requests.get(sitemapUrl)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    wa_links = re.findall(r'<loc>(.+?)</loc>',soup.prettify().replace("\n", "").replace(" ", ""))

    return wa_links


def check(url):  # return groupName,groupCount,groupLogo,groupDescri,groupType
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    try:
        groupName = soup.find_all('div', class_="tgme_page_title")[0].get_text().replace("\n", "")        
        groupType="Group"
        if(soup.find_all('div', class_="tgme_page_extra")[0].get_text().find("subscribers")>0):
            groupType = "Channel"
        
    except:
        return 0,0,0,0,0
    try:
        groupLogo = soup.find_all('img', class_="tgme_page_photo_image")[0]['src']
    except:
        groupLogo = "https://w7.pngwing.com/pngs/419/837/png-transparent-telegram-icon-telegram-logo-computer-icons-telegram-blue-angle-triangle-thumbnail.png"
    try:
        groupCount = soup.find_all('div', class_="tgme_page_extra")[
            0].get_text().split(" subscriber")[0].split(" member")[0]
    except:
        groupCount=0

    try:
        groupDescri = soup.find_all('div', class_="tgme_page_description")[
            0].get_text()
    except:
        groupDescri = groupName+ " help to find your wanted things"

    return groupName, groupCount, groupLogo, groupDescri, groupType
    # noOfMember = soup.find_all('div', class_="tgme_page_extra")[0].get_text()
    # imgUrl = soup.find_all('img', class_="tgme_page_photo_image")[0]["src"]

    
    # print(noOfMember)
    # print(imgUrl)

def findTitle(postlink):
    reqs = requests.get(postlink)
    Walinks = BeautifulSoup(reqs.text, 'html.parser').findAll("a")
    soup = BeautifulSoup(reqs.text, 'html.parser')
    return soup.find_all("h1")[0].text,Walinks

def loadposts():
    pass


def findlinks(sitemapUrl, sitemapIndex, postIndex,dataBase):
    postLinks = exract(sitemapUrl)[postIndex:]
    # postLinks = exract(sitemapUrl)[:2]

    for postlink in postLinks:
        # print(postlink)
        try:
            title,Walinks = findTitle(postlink)
            title = title.lower().split(" telegram")[0].capitalize()
        except:
            continue

        print(title)
        for i in Walinks:
            link = i.get_attribute_list("href")[0].replace("r.me","t.me")
            if(link.find("http")<0):
                link="https:"+link
            
            if(link.find(".me") != -1):
                # print(link)
                try:
                    groupName, groupCount, groupLogo, groupDescri, groupType = check(link)
                except Exception as e:
                    print(e)
                    print("reset Wifi and click enter!")
                    data = {}
                    data["lastSitemap"] = sitemapIndex
                    data["lastPost"] = postIndex
                    insertData("ScrapData", data, dataBase, format="patch")
                    print("WhatsApp limit")
                    return -1
                if(groupName == 0):
                    continue
                whatsappDic = {}
                whatsappDic["groupName"] = groupName
                whatsappDic["groupCount"] = groupCount
                whatsappDic["groupLogo"] = groupLogo
                whatsappDic["groupDescri"] = groupDescri
                whatsappDic["groupType"] = groupType
                if(link.find("/addstickers/")<0):
                    whatsappDic["groupLink"] = link.split("/")[-1]
                else:
                    whatsappDic["groupLink"] = link.split("https://t.me/")[-1]

                if(isdataexit(title.replace(".", ""), whatsappDic,dataBase)):
                    continue
                insertData(title.replace(".", ""), whatsappDic, dataBase)
                print("     "+str(sitemapIndex), str(postIndex) +"==>"+groupName, "===>>", link.split("/")[-1])
        postIndex += 1
        print("\n\n\n")
    return postIndex

def initialDatabase(databaseUrl):
    dataBase = firebase.FirebaseApplication(
        databaseUrl, None)
    return dataBase



def run():
    dataBase = initialDatabase(databaseUrl)
    dic = dataBase.get(databaseUrl, "ScrapData")

    try:                                   # if scrapdata table not exist then add it in database
        lastPost = dic['lastPost']
        lastSitemap = dic['lastSitemap']
    except:
        lastPost=0
        lastSitemap=0
        data={} 
        data["lastPost"]=lastPost
        data["lastSitemap"]=lastSitemap
        insertData("ScrapData", data, dataBase, format="patch")
    
    sitemaps = exract(mainSitemapUrl)   # extract all sitemaps form main sitemap

    for i in sitemaps[lastSitemap:-1]:  # ignore last sitemap its page sitemap
    # for i in sitemaps[:1]:
        # print(i)
        resuslt = findlinks(i, lastSitemap, lastPost, dataBase)
        lastSitemap += 1
        if(lastSitemap>=len(sitemaps)-2):
            lastSitemap=0
        lastPost = 0

        if(resuslt < 0):
            break
        print("finished a sitemap")
        data = {}
        data["lastSitemap"] = lastSitemap
        data["lastPost"] = lastPost
        insertData("ScrapData", data,dataBase, format="patch")


run()

# urlChanell = "https://t.me/testing111211"
# urlGroup = "https://t.me/SGCustom"
# print("chanell : ",check(urlChanell))
# print("Group   : ",check(urlGroup))

# dataBase=initialDatabase(databaseUrl)
# whatsappDic = {}
# whatsappDic["groupName"] = "TOSS KING RAJA RAJKOT™"
# whatsappDic["groupCount"] = "16 755"
# whatsappDic["groupLogo"] = "https://cdn5.telesco.pe/file/tsIhSoRdO-Sco0qzn3h8ud7EX5fAuDbUhUSEvqWbOzUMZZQAciP2EmochbufT1m15WE_qRfu-Ncg10YWZ2Tz7VHw-G4HAnBOQGcc-6Q5ujnJtyGQOOUSEYBMIQDhvbMNlqM_URz-EmYHcx1MA17oy3b-rcNNrQIFPytZBqFHQij7CRWsvfodDtvfpLsGXEOEjPe2ug5LkVAEJDOcRgqHyILE97F9-6ZDh9UvQ1O0ROKiTQwfRSgvbiHe70xEd0ApnTv0ZiEMIzinJzMpOWbkLnt8Gmn_swIpSQj3gmJmkj8pEYep26yCKWTa9YJZ9mYiPwwxfNHayUq4HV8jX9ybiQ.jpg"
# whatsappDic["groupDescri"] = "🔄Link: https://t.me/joinchat/AAAAAFdiM4WuLmVABmY-aQ🛃Admin : Specialization in cricket analysisSince - 2015📢  : ⤵️🏏 Cricket  ✔️_________________________________🔊NOTE : Channel only for those countries where betting is legal ✔️"
# whatsappDic["groupType"] = "Channel"
# whatsappDic["groupLink"] = "Raja_rajkot_toss_king"

# print(isdataexit("Rajkot", whatsappDic, dataBase))
