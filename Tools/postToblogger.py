import importlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyperclip
from selenium.webdriver.common.keys import Keys
import timeit
import traceback

newpostcount = 0
# currentUrl=""
# driver = webdriver.Chrome('./chromedriver')


def refresh(driver):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > c-wiz > div > div.LYkI7 > div.vAOvBb > div.U26fgb.O0WRkf.zZhnYe.e3Duub.C0oVfc.jPVgtf.ScshYd.M9Bg4d.RDPZE")))
    driver.refresh()
    time.sleep(10)


def start(blogLink, accNo):
    file = open("C:/Users/smart/Desktop/dontdelete/techfarm.txt", "r+")
    accountSet = file.readlines()
    text = accountSet[accNo].split(":")
    mail = text[0]
    password = text[1].split("\n")[0]
    file.close()

    try:
        global driver
        path = os.path.abspath(
            "./chromedriver.exe").split("TechFarm")[0]+"TechFarm\\tools\\chromedriver.exe"
        driver = webdriver.Chrome(
            'C:\\Users\\smart\\Desktop\\TechFarm\\tools\\chromedriver.exe')
        driver.get("https://stackoverflow.com/users/login?ssrc=head")
        driver.maximize_window()
        driver.find_element_by_xpath(
            "//*[@id='openid-buttons']/button[1]").click()
        email = driver.find_element_by_xpath("//*[@id='identifierId']")
        email.send_keys(mail)
        email.send_keys(Keys.RETURN)
        time.sleep(10)
        passw = driver.find_elements_by_xpath("//input[@type='password']")[0]
        passw.send_keys(password)
        passw.send_keys(Keys.RETURN)
        time.sleep(10)
        # input("press Enter")
        driver.get(blogLink)
    except Exception as e:

        print("cant start chrome")
        pass


def newpost(driver, newpostcount):
    # global newpostcount
    if(newpostcount > 2):
        print("Exit!")
        return(1)
    try:
        WebDriverWait(driver, 30).until(
            lambda d: d.find_element_by_class_name("MIJMVe"))
        time.sleep(1)
        driver.find_element_by_class_name("MIJMVe").click()
        driver.find_element_by_class_name("MIJMVe").click()

        Wait = WebDriverWait(driver, 30)
        Wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*/span/c-wiz/div/div[2]/div[5]/div/span/div/div")))

        driver.refresh()
        return("hello")  # dont delete

    except Exception:
        # print(traceback.format_exc())

        print(newpostcount, end="/")
        driver.refresh()
        newpostcount += 1
        newpost(driver, newpostcount)

        # refresh(driver)


def title(driver, ptitle):
    # print("ptitle")
    try:
        #Title insert
        # time.sleep(10)
        # driver.implicitly_wait(6)
        # driver.refresh()
        WebDriverWait(driver, 30).until(
            lambda d: d.find_elements_by_xpath("//input[@jsname='YPqjbf']")[0])
        driver.find_elements_by_xpath(
            "//input[@jsname='YPqjbf']")[0].send_keys(ptitle)
    except Exception:

        print(traceback.format_exc())
        refresh(driver)
        title(driver, ptitle)


def content(driver, pcontent):
    try:
        #Post content insert
        WebDriverWait(driver, 10).until(
            lambda d: d.find_elements_by_xpath("//iframe")[1])
        driver.find_element_by_class_name("CodeMirror-scroll").click()
        iframe = driver.find_elements_by_xpath("//iframe")[1]
        driver.switch_to.frame(iframe)
        pyperclip.copy(pcontent)
        i = driver.find_element_by_tag_name("p")
        i.send_keys(Keys.CONTROL, 'v')
        driver.switch_to.default_content()
    except Exception:

        print(traceback.format_exc())
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > c-wiz > div > div.LYkI7 > div.vAOvBb > div.U26fgb.O0WRkf.zZhnYe.e3Duub.C0oVfc.jPVgtf.ScshYd.M9Bg4d.RDPZE")))
        refresh(driver)
        content(driver, pcontent)


def tag(driver, ptag):
    try:
        #tag insert
        WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_xpath(
            "//textarea[@jsname='YPqjbf'][@aria-label='Separate labels by commas']")[0])
        driver.find_elements_by_xpath(
            "//textarea[@jsname='YPqjbf'][@aria-label='Separate labels by commas']")[0].send_keys(ptag)
    except Exception:

        print(traceback.format_exc())
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > c-wiz > div > div.LYkI7 > div.vAOvBb > div.U26fgb.O0WRkf.zZhnYe.e3Duub.C0oVfc.jPVgtf.ScshYd.M9Bg4d.RDPZE")))
        refresh(driver)
        tag(driver, ptag)


def schedule(driver, date, time):
    try:
        #descripe insert
        WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath(
            "//*/span/c-wiz/div/div[2]/div[5]/div/span/div/div"))
        driver.find_elements_by_xpath(
            "//*[@id='i4']/span/c-wiz/div/div[2]/div[2]/div/span/div/div[1]")[0].click()

        i = driver.find_elements_by_xpath(
            "//*[@id='i7']/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/input")[0]
        driver.implicitly_wait(5)
        i.click()
        i.click()
        i.send_keys(Keys.CONTROL, 'a')
        i.send_keys(Keys.CONTROL, 'x')
        code = pyperclip.paste()
        pyperclip.copy(date)
        i.send_keys(Keys.CONTROL, 'v')

        i = driver.find_elements_by_xpath(
            "//*[@id='i7']/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input")[0]
        driver.implicitly_wait(1)
        i.click()
        i.click()
        i.send_keys(Keys.CONTROL, 'a')
        i.send_keys(Keys.CONTROL, 'x')
        code = pyperclip.paste()
        pyperclip.copy(time)
        i.send_keys(Keys.CONTROL, 'v')

    except Exception as e:

        refresh(driver)
        schedule(driver, date, time)


def descri(driver, pdescri):
    try:
        #descripe insert
        # global currentUrl
        # currentUrl=driver.current_url

        WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath(
            "//*/span/c-wiz/div/div[2]/div[5]/div/span/div/div"))
        driver.find_elements_by_xpath(
            "//*/span/c-wiz/div/div[2]/div[5]/div/span/div/div")[0].click()
        WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_xpath(
            "//*/div/div[1]/div[1]/div[2]/textarea")[0])
        driver.find_elements_by_xpath(
            "//textarea[@jsname='YPqjbf'][@aria-label='Enter search description']")[0].send_keys(pdescri)
    except Exception:

        print(traceback.format_exc())
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > c-wiz > div > div.LYkI7 > div.vAOvBb > div.U26fgb.O0WRkf.zZhnYe.e3Duub.C0oVfc.jPVgtf.ScshYd.M9Bg4d.RDPZE")))
        refresh(driver)
        descri(driver, pdescri)


def image(driver, pimage):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > c-wiz > div > div.LYkI7 > div.vAOvBb > div.U26fgb.O0WRkf.zZhnYe.e3Duub.C0oVfc.jPVgtf.ScshYd.M9Bg4d.RDPZE")))
        WebDriverWait(driver, 10).until(
            lambda d: d.find_elements_by_xpath("//span[@class='vde74d']")[2])
        driver.find_elements_by_xpath("//span[@class='ytEBO']")[0].click()
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element_by_class_name("qjTEB"))
        # WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath("//div[@data-command='imageUploadPicker'][@jsname='xw1cm']/div[@class='jO7h3c']"))
        clicker = driver.find_elements_by_xpath(
            "//div[@data-command='imageUploadPicker'][@jsname='xw1cm']/div[@class='jO7h3c']")[0]
        clicker.click()
        driver.implicitly_wait(1)
        clicker.click()
        actionChains = ActionChains(driver)
        actionChains.double_click(clicker).perform()
        clicker.click()
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element_by_xpath("//iframe[@allow='camera']"))
        iframe = driver.find_element_by_xpath("//iframe[@allow='camera']")
        driver.switch_to.frame(iframe)
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element_by_xpath("//input[@type='file']"))
        upload = driver.find_element_by_xpath("//input[@type='file']")
        upload.send_keys(os.path.abspath(pimage))
        WebDriverWait(driver, 60).until(
            lambda d: d.find_element_by_class_name("ee-tb-hf-enabled"))
        driver.find_element_by_xpath("//*[@id='picker:ap:0']").click()
        WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath(
            "//*[@id='yDmH0d']/div[4]/div/div[2]/span/div/div[1]/span/div[5]/label/div/div[3]"))
        driver.find_element_by_xpath(
            "//*[@id='yDmH0d']/div[4]/div/div[2]/span/div/div[1]/span/div[5]/label/div/div[3]").click()
        driver.find_element_by_xpath(
            "//*[@id='yDmH0d']/div[4]/div/div[2]/span/div/div[2]/span/div[3]/label/div/div[3]").click()
        driver.find_element_by_xpath(
            "//*[@id='yDmH0d']/div[4]/div/div[2]/div[3]/div[2]/span/span").click()

    except Exception:

        print(traceback.format_exc())
        driver.refresh()
        image(driver, pimage)


def addAlt(driver, Ialt, Ititle):
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element_by_class_name("CodeMirror-scroll"))
    driver.find_element_by_class_name("CodeMirror-scroll").click()
    iframe = driver.find_elements_by_xpath("//iframe")[1]
    driver.switch_to.frame(iframe)
    #pyperclip.copy(pcontent)
    i = driver.find_element_by_tag_name("p")
    i.send_keys(Keys.CONTROL, 'a')
    i.send_keys(Keys.CONTROL, 'x')
    code = pyperclip.paste()
    text = "alt=\""+Ialt+"\" title=\""+Ititle+"\""
    code = code.replace("alt=\"\"", text)
    pyperclip.copy("")
    i.send_keys(Keys.CONTROL, 'v')
    driver.switch_to.default_content()


def publish(driver):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > c-wiz > div > div.LYkI7 > div.vAOvBb > div.U26fgb.O0WRkf.zZhnYe.e3Duub.C0oVfc.jPVgtf.ScshYd.M9Bg4d.RDPZE")))

        # findElement(By.cssSelector("#yDmH0d > c-wiz:nth-child(18) > div > c-wiz > div > div.LYkI7 > div.vAOvBb > div.U26fgb.O0WRkf.zZhnYe.e3Duub.C0oVfc.jPVgtf.ScshYd.M9Bg4d.RDPZE"))
        # time.sleep(10)
        # driver.back()
        driver.find_elements_by_xpath(
            "//*[@id='yDmH0d']/c-wiz/div/c-wiz/div/div[1]/div[2]/div[4]/span/span/div/span")[0].click()
        # time.sleep(5)
        WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_xpath(
            "//*[@id='yDmH0d']/div[4]/div/div[2]/div[3]/div[2]/span/span")[0])
        driver.find_elements_by_xpath(
            "//*[@id='yDmH0d']/div[4]/div/div[2]/div[3]/div[2]/span/span")[0].click()
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".MIJMVe")))
        driver.refresh()
    # time.sleep(10)

    # Wait = WebDriverWait(driver, 30)
    # # WebDriverWait(driver, 30).until(lambda d: d.find_element_by_class_name("MIJMVe"))
    # Wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='gb']/div[1]/div/div[2]/c-wiz/div[2]/div/div/span/span/span[2]")))

        # if(currentUrl==driver.current_url):
        #     time.sleep(10)
        #     publish(driver)
    except Exception:

        print(traceback.format_exc())
        publish(driver)


def close(driver):
    driver.quit()


def postnow(driver, ptitle, ptag, pdescri, pcontent, pimage, alt, postdate, posttime):

    start = timeit.default_timer()
    global newpostcount
    try:
        # time.sleep(4)
        status = newpost(driver, newpostcount)
        if(status == None):
            print("To many posted!")
            return 0
        # time.sleep(4)
        title(driver, ptitle)
        # time.sleep(4)
        tag(driver, ptag)
        # time.sleep(4)
        schedule(driver, postdate, posttime)
        # time.sleep(4)
        descri(driver, pdescri)

        # time.sleep(4)
        image(driver, pimage)

        # time.sleep(4)
        addAlt(driver, alt, ptitle)
        # time.sleep(4)
        content(driver, pcontent)
        # time.sleep(4)
        publish(driver)
        # time.sleep(10)
        print("posted", end=" >>>")
        newpostcount = 0
    except Exception:

        print(traceback.format_exc())
        print("posting failed", end=" >>")
        # print(e)

        stop = timeit.default_timer()
        # print('Time: ', stop - start)
        return 0

    stop = timeit.default_timer()
    filetime = open("time.txt", "a")
    filetime.write(str(stop-start)+"\n")
    filetime.close()

    print('Time: ', stop - start)


def test():
    postnow(driver, "title", "tag", "descri", "content",
            "./hello.png", "alt", "May 20, 2021", "10:41 AM")
    postnow(driver, "title", "tag", "descri", "content",
            "./hello.png", "alt", "May 20, 2021", "10:41 AM")


def begain():
    start("https://draft.blogger.com/blog/posts/596040241612557528", 1)


# def make():
#     importlib.reload(postToblogger)


if __name__ == "__main__":
    start("https://draft.blogger.com/blog/posts/596040241612557528", 1)
    postnow(driver, "title", "tag", "descri", "content",
            "./hello.png", "alt", "May 30, 2021", "10:41 AM")


# import importlib
# importlib.reload(postToblogger0)
#postnow(driver,"Title1","content1","tags1","description1","./test/a.webp")
# python
# import postToblogger0
# postToblogger0.start("https://draft.blogger.com/blog/posts/596040241612557528",1)
# postToblogger0.newpost(postToblogger0.driver,0)
# postToblogger0.title(postToblogger0.driver,"Title")
# postToblogger0.tag(postToblogger0.driver,"tag")
# postToblogger0.schedule(postToblogger0.driver,"May 26, 2021","10:41 AM")
# postToblogger0.descri(postToblogger0.driver,"descri")
# postToblogger0.publish(postToblogger0.driver)
# def postnow(driver,ptitle,ptag,pdescri,pcontent,pimage,alt,postdate,posttime):
# dateformat="May 4, 2021"
# timeformat="10:41 AM"

# postToblogger0.postnow(postToblogger0.driver,"title","tag","descri","content","./hello.png","alt","May 20, 2021","10:41 AM")
# postToblogger0.postnow(postToblogger0.driver,"title","tag","descri","content","./hello.png","alt","May 20, 2021","10:41 AM")
# postToblogger0.postnow(postToblogger0.driver,"title","tag","descri","content","./hello.png","alt","May 20, 2021","10:41 AM")

# postToblogger0.schedule(postToblogger0.driver,"May 26, 2021","10:41 AM")
# postToblogger0.publish(postToblogger0.driver)
# print(postToblogger0.newpost(postToblogger0.driver,0))
