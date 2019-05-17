from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from enum import Enum
import imageio as ImageIO
import sys
import os
import re

url = "http://pop-life.com/foursouls/"

class CardType(Enum):
    character = "CHARACTER CARD"
    treasure = "TREASURE CARD"
    loot = "LOOT CARD"
    monster = "MONSTER CARD"
    eternal = "STARTING ITEM"
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


def createFileImg(url_img, cardType):
    img_alt = os.path.basename(url_img)
    email = re.compile('\w+')
    result = email.findall(img_alt)
    result[0] = ''.join([i for i in result[0] if not i.isdigit()])
    if CardType.has_value(cardType):
        path = CardType(cardType).name + "/" + result[0] + "." + result[len(result) - 1]
        open(os.path.join(os.path.curdir, path), 'wb')
        return path
    else:
        return ""

def getData(driver):
    ret = []
    allElements = driver.find_elements(By.CLASS_NAME, 'single-team')
    for elm in allElements:
        cardType = elm.find_element(By.CLASS_NAME, 'team-info').find_element(By.TAG_NAME, 'h2').get_attribute('innerHTML')
        url_img = elm.find_element(By.CLASS_NAME, 'team-img').find_element(By.TAG_NAME, 'img').get_attribute('src')
        name = createFileImg(url_img, cardType)
        if url_img != "" and name != "":
            img = ImageIO.imread(url_img)
            ImageIO.imwrite(name,img, "png")
    return ret

driver = webdriver.Chrome() 

for card in CardType :
    os.makedirs(card.name)

for x in range(0, 44):    
    driver.get(url + "index.php?page=" + str(x))
    getData(driver)



