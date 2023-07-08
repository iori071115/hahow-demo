from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time 
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def how_many_contributors_are_there():
    s = Service('chromedriver')
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("detach", True)
    chrome = webdriver.Chrome(service = s ,options= chrome_options )

    chrome.get("https://github.com/hahow/hahow-recruit")
    time.sleep(2)

    soup = BeautifulSoup(chrome.page_source, 'html.parser')
    contributors = []
    data = soup.find_all('li',{'class' : 'mb-2 mr-2'})
    for item in data:
        item = item.find('a').get('href')
        contributor = item.split('/')
        contributors.append(contributor[-1])
    print("There are a total of", len(contributors))
    print(contributors)
    chrome.close()


def do_the_images_of_wireframe_exist():
    s = Service('chromedriver')
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("detach", True)
    chrome = webdriver.Chrome(service = s ,options= chrome_options )

    chrome.get("https://github.com/hahow/hahow-recruit")
    time.sleep(2)
    frontend = chrome.find_element(By.CSS_SELECTOR,"a[title='frontend.md']")
    frontend.click()
    time.sleep(2)

    soup = BeautifulSoup(chrome.page_source, 'html.parser')
    wfphotos = soup.select('a[target="_blank"]>img')
    if wfphotos is not None :
        print("Images for Wireframe exists")
        for item in wfphotos:
            wfphoto = item.get('src')
            print("https://github.com" + wfphoto)
    else:
        print("Image for Wireframe does not exist")
    chrome.close()


def the_last_commenter():
    s = Service('chromedriver')
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("detach", True)
    chrome = webdriver.Chrome(service = s ,options= chrome_options )

    chrome.get("https://github.com/hahow/hahow-recruit")
    time.sleep(2)
    # comm = chrome.find_element(By.CSS_SELECTOR,"a[data-pjax='#repo-content-pjax-container']")
    comm = chrome.find_element(By.XPATH,'//*[@id="repo-content-pjax-container"]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[4]/ul/li/a')
    comm.click()
    time.sleep(2)

    soup = BeautifulSoup(chrome.page_source, 'html.parser')
    x = soup.find_all('div',{'class' : 'TimelineItem-body'})
    result = x[0].find('a',{'class' : 'commit-author user-mention'}).text
    print("The last commenter is ",result)
    chrome.close()