import timeit
import os
import sys
import time
import urlexract
import postToblogger
import ScrapTable



noOfPost = 50

accNO = 0
if(len(sys.argv) > 1):
    accNO = int(sys.argv[1])
# read first line


def read():
    file = open("./data/topost.txt", "r")
    firLi = file.readline().replace("\n", "")
    file.close()
    return firLi

# delete first line


def delete():
    file = open("./data/topost.txt", "r")
    firLi = file.readlines()
    file.close()
    file = open("./data/topost.txt", "w")
    file.write("".join(firLi[1:]))
    file.close()

# last post link


def posted(posted_link):
    file = open("./data/posted.txt", "a")
    file.write(posted_link+"\n")
    file.close()




# print(time.time())
# print(type(time.time()))X
# print()
def Run():
    count = 0

    for i in range(noOfPost):

        postTitle = read()
        #print(postTitle)
        if(postTitle == ""):
            urlexract.addTableNameIntotxt()
            postTitle = read()
            if(postTitle == ""):
                print("No new posts")
                break
        
        try:
            title, tag, descri, content = ScrapTable.getdata(postTitle)
        except Exception as e:
            print(e)
            break

        if(i == 0):
            # pass
            postToblogger.start(
                "https://draft.blogger.com/blog/posts/8069754486747573131", accNO)

        if(i < 9):
            print(" ", end="")

        print(i+1, end=">>>")
        print(postTitle, end="")
        print("-"*(45-len(postTitle)), end="status:")
        #postnow(driver,ptitle,ptag,pdescri,pcontent,pimage):

        alt = title.split(" |")[
            0]+" image front back and side view with model,release year,top speed,fuel capacity,reserve capacity,millage and power Details"

        postdate, posttime = ('Jul 8, 2019', '7:10 PM')
        # postnow(driver,ptitle,ptag,pdescri,pcontent,pimage,alt,postdate,posttime,isImg=True):
        # print(title, tag, descri, content)
        status = postToblogger.postnow(
            driver=postToblogger.driver, ptitle=title, ptag=tag, pdescri=descri, pcontent="", pimage="delete.png",alt="", postdate=postdate, posttime=posttime)
        # status=0





        # postToblogger.postnow()
        if(status == 0):
            print("Exit!")
            break
        print("")

        posted(postTitle)
        delete()
        count = i+1

    postToblogger.close(postToblogger.driver)

    print(count, " post posted")


def start():
    postToblogger.start(
        "https://draft.blogger.com/blog/posts/8069754486747573131", 1)


Run()
