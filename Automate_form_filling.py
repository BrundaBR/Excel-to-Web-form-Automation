#imports
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
#driver setup
browser = webdriver.Chrome(executable_path='./chromedriver')
browser.set_window_size(900,900)


#Work on excel
df=pd.read_excel('data.xlsx')


#get excel data


#enter in wesite form
browser.get('file:///home/brunda/Desktop/Projects/CMT_Automate/form.html')

for i in df.index:
    data=df.iloc[i]
    mkpl=browser.find_element("name","mkpl").send_keys(data[0])
    pl=browser.find_element("name","pl").send_keys(data[1])
    gl=browser.find_element("name","gl").send_keys(data[2])
    cp=browser.find_element("name","cp").send_keys(data[3])
    setup=browser.find_element("name","setup").send_keys(data[4])
    sd=browser.find_element("name","date").send_keys(str(data[5]))
    ed=browser.find_element("name","date1").send_keys(str(data[6]))
    url=browser.find_element("name","url").send_keys(data[7])
    code=browser.find_element("name","code").send_keys(data[8])
    offer=browser.find_element("name","offer").send_keys(data[9])
    match=browser.find_element("name","match").send_keys(data[10])
    rebate=browser.find_element("name","rebate").send_keys(data[11])


time.sleep(10) # Let the user actually see something!

browser.quit()