from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import imageio as ImageIO
import sys
import os

url = "http://pop-life.com/foursouls/"

def createFileImg(url_img):
    img_alt = os.path.basename(url_img)
    open(os.path.join(os.path.curdir, img_alt), 'wb')
    print(img_alt)
    return img_alt # for now..

def getData(driver):
    ret = []
    elements = driver.find_elements(By.CLASS_NAME, 'team-img')
    for elm in elements:
        elm = elm.find_element(By.TAG_NAME, 'img')
        url_img = elm.get_attribute('src')
        if url_img != "":
            img = ImageIO.imread(url_img)
            ImageIO.imwrite(createFileImg(url_img),img, "png")
    return ret

driver = webdriver.Chrome() 
data = []

for x in range(33, 44):    
    driver.get(url + "index.php?page=" + str(x))
    data.append(getData(driver))

print(data)



