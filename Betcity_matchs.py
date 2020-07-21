import urllib.request
import sys
import time
import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (presence_of_element_located)
from selenium.webdriver.support.wait import WebDriverWait


def betcity_matchs(driver, url):
    driver.get(url)
    time.sleep(5)
    Way = driver.find_elements_by_xpath("//*[@class='line__champ']/app-event-unit")

    for i in range(len(Way)):
        try:
            find_name = Way[i].find_element_by_class_name("line-event__name-team")
            find_coef =  Way[i].find_element_by_tag_name("app-main-dops-container")
            split_name = []
            split_coef_out = []

            if len((find_name).text) != 0: 
                split_name = find_name.text.split('\n')
                
            try:

                if len((find_coef).text) != 0:
                    split_coef = find_coef.text.split('\n')
                    str_plus1 = split_coef[0].startswith('+')
                    str_sub1 = split_coef[0].startswith('-')
                    str_plus2 = split_coef[1].startswith('+')
                    str_sub2 = split_coef[1].startswith('-')

                    if str_plus1 == False and str_sub1 == False and str_plus2 == False and str_sub2 == False:
                        split_coef_out.append(split_coef[0])
                        split_coef_out.append(split_coef[1])
                        print(split_name)
                        print(split_coef_out, '\n')

                    else:
                        pass  
                    
            except:
                pass
        except:
            pass
    print('Игр нет')
    driver.quit()


if __name__ == "__main__":
    print('Выберете дисциплину:\n1-киберспорт, 2-теннис, 3-настольный теннис,\n4-баскетбол, 5-волейбол')
    url_choose = input()
    url = ''

    if url_choose == '1': url = 'cybersport'
    elif url_choose == '2': url = 'tennis'
    elif url_choose == '3': url = 'table-tennis'
    elif url_choose == '4': url = 'basketball'
    elif url_choose == '5': url = 'volleyball'
    else:
        print('Неверный выбор.')
        sys.exit(0)   
    
    urlBet = 'https://betcity.ru/ru/live/' + url
    URL = urlBet
    
    driver = webdriver.Chrome(os.getcwd() + '\\chromedriver')
    betcity_matchs(driver, URL)
