from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs 
import os

directory = 'C:\Python\projects\instagram\chromedriver'
xpath_dict_login = {
    'xpath_login_ID' : '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input',
    'xpath_login_PW' : '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input', 
    'xpath_login_button' : '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button',
    'xpath_notification_close_button' : '/html/body/div[4]/div/div/div[3]/button[2]', 'xpath_deeper' : '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[2]/button', 
    'xpath_right_buttons' : ['//*[@id="react-root"]/section/main/div/div[1]/div[2]/div/button','//*[@id="react-root"]/section/main/div/div[1]/div[2]/div/button[2]','//*[@id="react-root"]/section/main/div/div[2]/div[2]/div/button[1]','//*[@id="react-root"]/section/main/div/div[2]/div[2]/div/button[2]'], 
    'xpath_slider_sample' : ['//*[@id="react-root"]/section/main/div/div[1]/div[2]/div/div/div/div/ul/li[1]','//*[@id="react-root"]/section/main/div/div[2]/div[2]/div/div/div/div/ul/li[1]']
    } 
xpath_dict = {
    "xpath_right_buttons" : ['//*[@id="react-root"]/section/main/div/div[3]/div/div[2]/div/button','//*[@id="react-root"]/section/main/div/div[3]/div/div[2]/div/button[2]','//*[@id="react-root"]/section/main/div/div[3]/div/div[2]/div/button','//*[@id="react-root"]/section/main/div/div[3]/div/div[2]/div/button[2]'], 
    "xpath_slider_sample" : ['//*[@id="react-root"]/section/main/div/div[2]/div/div[2]/div/div/div/div/ul/li[1]','//*[@id="react-root"]/section/main/div/div[3]/div/div[2]/div/div/div/div/ul/li[1]']
    }

def webWait(xpath):
    WebDriverWait(driver,10).until(lambda x: x.find_element_by_xpath(xpath))

def checkLogin():
    login_check = input("do you want to scrape data using your login data?   y/n?")
    if login_check == "y":
        return True
    elif login_check =="n":
        return False
    else:
        print("WTF in checkLogin()")

def checkLoginInfo():
    #checking ID existence
    ID = 'woogieboogie.jl@gmail.com'
    PW = 'Jwl.73016589'
    if ID:
        pass
    elif not ID:
        ID = input('need ID info for login purposes...')
    else:
        pass
    #checking PW existence
    if PW:
        pass
    elif not PW:
        PW = input(f'need PW info for account : {ID}...')
    else:
        pass
    return ID, PW

def checkDatapoolInfo():
    #checking datapool categorization info
    datapool_type = input(f"the requested account '{target}' is related to which datapool category?, please insert the right categorization information...")
    return datapool_type

def targetInfo():
    target = input('who to target?')
    return target

def instaLogin(ID,PW):
    driver.get('https://www.instagram.com/')
    webWait(xpath_keys['xpath_login_ID'])
    driver.find_element_by_xpath(xpath_keys['xpath_login_ID']).send_keys(ID)
    driver.find_element_by_xpath(xpath_keys['xpath_login_PW']).send_keys(PW)
    driver.find_element_by_xpath(xpath_keys['xpath_login_button']).click()

    webWait(xpath_keys['xpath_notification_close_button'])
    driver.find_element_by_xpath(xpath_keys['xpath_notification_close_button']).click()

def suggestedScrape():
    try:
        driver.find_element_by_class_name('_4bSq7')
        webWait(xpath_keys['xpath_slider_sample'][1])
        # stories = True
    except NoSuchElementException:
        webWait(xpath_keys['xpath_slider_sample'][0])
        # stories = False
    suggested = []
    i = 0
    k = 1
# 여기서 해야하는 것 : 시간을 끌어줘서 xpath를 찾을 수 있게끔(로그인 하지 않아도)
    try:
        driver.find_element_by_xpath(xpath_keys['xpath_right_buttons'][i])
        block = driver.find_element_by_class_name('YlNGR')
        while True:
            try:
                user = block.find_element_by_xpath(f'.//li[{k}]/div/div/div/div[2]/a') 
                print(user.get_attribute('title') + f'  extracting {str(k)}th profile')
                suggested.append(user.get_attribute('title'))
                k += 1
            except NoSuchElementException:
                try :
                    driver.find_element_by_xpath(xpath_keys['xpath_right_buttons'][i]).click()
                    i = 1
                except NoSuchElementException:
                    break

    except NoSuchElementException:
        driver.find_element_by_xpath(xpath_keys['xpath_right_buttons'][i+2])
        block = driver.find_elements_by_class_name('YlNGR')[1]
        while True:
            try:
                user = block.find_element_by_xpath(f'.//li[{k}]/div/div/div/div[2]/a') 
                print(user.get_attribute('title') + f'  extracting {str(k)}th profile')
                suggested.append(user.get_attribute('title'))
                k += 1
            except NoSuchElementException:
                try:
                    driver.find_element_by_xpath(xpath_keys['xpath_right_buttons'][i+2]).click()
                    i = 1
                except NoSuchElementException:
                    break

    finally:
        related = list(set(suggested))
        print(related)
    return related

def printer(print_list):
    profile_text = ''
    for profile in print_list:
        profile_text = profile_text + '\n' + profile
    return profile_text[1:]

def dataRead(datapool_type):
    os.makedirs("datapool",exist_ok=True)
    if os.path.isfile(f"datapool/{datapool_type}.txt") is True:
        pass
    elif os.path.isfile(f"datapool/{datapool_type}.txt") is False:
        with open(f"datapool/{datapool_type}.txt", 'wt') as template:
            template.write('')
    else:
        print('WTF in dataRead()')
        pass
    with open(f"datapool/{datapool_type}.txt",mode='rt') as datapool_txt:
        datapool_read = datapool_txt.read().splitlines()
        print(datapool_read)
    return datapool_read

def dataWrite(datapool_type,related,datapool_read):
        datapool_write = list(set(related + datapool_read))
        datapool_ntxt = printer(datapool_write)
        with open(f"datapool/{datapool_type}.txt",mode='wt') as datapool_txt:
            datapool_txt.write(datapool_ntxt)

def targetSave(target, related_text):
    os.makedirs("target",exist_ok=True)
    with open(f"target/{target}_related.txt",mode='wt') as target_data:
        target_data.write(related_text)




if __name__ == "__main__":
    driver = webdriver.Chrome(directory)
    login_value = checkLogin()
    if login_value is False:
        xpath_keys = xpath_dict
        target = targetInfo()
        driver.get(f'https://www.instagram.com/{target}')
    else:
        xpath_keys = xpath_dict_login
        ID, PW = checkLoginInfo()
        instaLogin(ID,PW)
        target = targetInfo()
        driver.get(f'https://www.instagram.com/{target}')        
        webWait(xpath_keys['xpath_deeper'])
        driver.find_element_by_xpath(xpath_keys['xpath_deeper']).click()
    related = suggestedScrape()
    related_text = printer(related)
    targetSave(target,related_text)
    datapool_type = checkDatapoolInfo()
    datapool_read = dataRead(datapool_type)
    dataWrite(datapool_type,related,datapool_read)