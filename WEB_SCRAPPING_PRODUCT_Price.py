#!/usr/bin/env python
# coding: utf-8

# In[ ]:



# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 03:16:06 2021

@author: Monish Bangera
"""

import time
import pandas as pd
from selenium import webdriver
temp1=[]
temp2=[]
Technology=[]
Announced=[]
Status=[]
Dimension=[]
Weight=[]
Build=[]
SIM=[]
USB=[]
Size=[]
Resolution=[]
Protection=[]
OS=[]
Chipset=[]
CPU=[]
GPU=[]
Card_slot=[]
Internal=[]
Jack=[]
Bluetooth=[]
GPS=[]
NFC=[]
Radio=[]
Charging=[]
Price=[]
Sensor=[]
Wlan=[]
Cardslot=[]
product=[]
executable_path = (r"C:\Users\Monish Bangera\Desktop\chromedriver_win32\chromedriver.exe")
p="SAMSUNG"

temp=[]
driver = webdriver.Chrome(executable_path=executable_path)
driver.get('https://www.gsmarena.com/')
link = driver.find_element_by_partial_link_text(p).click()
x=True
while x:
    
    a=driver.find_elements_by_xpath('//*[@id="review-body"]/div/ul/li/a/strong/span')
    product.extend(temp)
    temp.clear()

    for i,j in enumerate(a):
        temp.append(j.text)

    for i,z in enumerate(temp):
        time.sleep(5)
        try:
            driver.find_element_by_partial_link_text(z).click()
        except:
            continue
        for x in driver.find_elements_by_class_name("nfo"):
            temp1.append(x.text)

        for y in driver.find_elements_by_class_name("ttl"):
            temp2.append(y.text)
        d={'Key':temp2,'Value':temp1}
        products=pd.DataFrame(data=d)
        temp1=[]
        temp2=[]
        products=products.set_index(keys="Key")
        products.index.name=None
        try:
            Tech=products.loc['Technology']['Value']
            Technology.append(Tech)
        except:
            Technology.append(" ")
        try:
            Ann=products.loc['Announced']['Value']
            Announced.append(Ann)
        except:
            Announced.append(" ")
        try:
            status=products.loc['Status']['Value']
            Status.append(status)
        except:
            Status.append(" ")
        try:
            dimension=products.loc['Dimensions']['Value']
            Dimension.append(dimension)
        except:
            Dimension.append(" ")
        try:
            weight=products.loc['Weight']['Value']
            Weight.append(weight)
        except:
            Weight.append(" ")
        try:
            build=products.loc['Build']['Value']
            Build.append(build)
        except:
            Build.append(" ")
        try:
            sim=products.loc['SIM']['Value']
            SIM.append(sim)
        except:
            SIM.append(" ")
        try:
            usb=products.loc['USB']['Value']
            USB.append(usb)
        except:
            USB.append(" ")
        try:
            size=products.loc['Size']['Value']
            Size.append(size)
        except:
            Size.append(" ")
        try:
            resolution=products.loc['Resolution']['Value']
            Resolution.append(resolution)
        except:
            Resolution.append(" ")
        try:
            protection=products.loc['Protection']['Value']
            Protection.append(protection)
        except:
            Protection.append(" ")
        try:
            os=products.loc['OS']['Value']
            OS.append(os)
        except:
            OS.append(" ")
        try:
            chipset=products.loc['Chipset']['Value']
            Chipset.append(chipset)
        except:
            Chipset.append(" ")
        try:
            cpu=products.loc['CPU']['Value']
            CPU.append(cpu)
        except:
            CPU.append(" ")
        try:
            gpu=products.loc['GPU']['Value']
            GPU.append(gpu)
        except:
            GPU.append(" ")
        try:
            cardslot=products.loc['Card slot']['Value']
            Cardslot.append(cardslot)
        except:
            Cardslot.append(" ")
        try:
            internal=products.loc['Internal']['Value']
            Internal.append(internal)
        except:
            Internal.append(" ")
        try:
            jack=products.loc['3.5mm jack']['Value']
            Jack.append(jack)
        except:
            Jack.append(" ")
        try:
            bluetooth=products.loc['Bluetooth']['Value']
            Bluetooth.append(bluetooth)
        except:
            Bluetooth.append(" ")
        try:
            gps=products.loc['GPS']['Value']
            GPS.append(gps)
        except:
            GPS.append(" ")
        try:
            nfc=products.loc['NFC']['Value']
            NFC.append(nfc)
        except:
            NFC.append(" ")
        try:
            radio=products.loc['Radio']['Value']
            Radio.append(radio)
        except:
            Radio.append(" ")
        try:
            charging=products.loc['Charging']['Value']
            Charging.append(charging)
        except:
            Charging.append(" ")
        try:
            price=products.loc['Price']['Value']
            Price.append(price)
        except:
            Price.append(" ")
        try:
            wlan=products.loc['WLAN']['Value']
            Wlan.append(wlan)
        except:
            Wlan.append(" ")
        try:
            sensor=products.loc['Sensors']['Value']
            Sensor.append(sensor)
        except:
            Sensor.append(" ")
        driver.back()
    try:
        driver.find_element_by_xpath('//*[@id="body"]/div/div[3]/div[2]/a[2]').click()
    except:
        x=False
p={"Technology":Technology,"Announced":Announced,"Status":Status,"Dimension":Dimension,"Weight":Weight,"Build":Build,"SIM":SIM,"USB":USB,"Size":Size,"Resolution":Resolution,"OS":OS,"Chipset":Chipset,"CPU":CPU,"GPU":GPU,"Card_slot":Cardslot,"Internal":Internal,"Jack":Jack,"Bluetooth":Bluetooth,"GPS":GPS,"NFC":NFC,"Radio":Radio,"Charging":Charging,"Wlan":Wlan,"Sensor":Sensor,"Price":Price}
df=pd.DataFrame(data=p)
df.to_csv("project_final.csv")
driver.quit()

