#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 01:16:28 2021

@author: Monish Bangera
"""


import pandas as pd
from selenium import webdriver
executable_path = (r"C:\Users\Monish Bangera\Desktop\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(executable_path=executable_path)
driver.get('https://www.gsmarena.com/samsung-phones-9.php')
#p="SAMSUNG"
#link = driver.find_element_by_partial_link_text(p).click()
product_list=[]
product_df=[]
reviews_temp=[]
reviews=[]
m=True
while m:
    a=driver.find_elements_by_xpath('//*[@id="review-body"]/div/ul/li/a/strong/span')
    for i in a:
        product_list.append(i.text)
    for i in product_list:
   
        try:
            x=driver.find_element_by_partial_link_text(i)
           
            x.click()
            
            driver.implicitly_wait(30)
            b=driver.find_element_by_partial_link_text('READ ALL OPINIONS')
            b.click()
            driver.implicitly_wait(30)
            c=True
            while c:
                for y in driver.find_elements_by_class_name("uopin"):
                    reviews_temp.append(y.text)
                for x in range(len(reviews_temp)):
                    product_df.append(i)
                    reviews.extend(reviews_temp)
                    reviews_temp.clear()
            
                try:
                    v=driver.find_element_by_partial_link_text('»')
                    v.click()
                except:
                    c=False
                    driver.back()
                    driver.back()
            
            
           
        except:
            pass
    try:
        driver.find_element_by_xpath('//*[@id="body"]/div/div[3]/div[2]/a[2]').click()
        product_list.clear()
    except:
        m=False
    
d={'Product':product_df,'Review':reviews}
products=pd.DataFrame(data=d)

print(products)
driver.quit()

