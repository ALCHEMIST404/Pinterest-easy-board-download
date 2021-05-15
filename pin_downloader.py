# -*- coding: utf-8 -*-
"""
Created on Fri May 14 04:15:19 2021

@author: Ирина
"""
import time
import requests
import os
import json
import traceback
import sys

from progress.bar import IncrementalBar
from itertools import groupby
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class pin_downloader:
    
    def __init__(self, driver, login,password,delay_time,desk_url,scroll_delay_time,html_tmp_name):
        """
        Call in a loop to create terminal progress bar
        @params:
            driver               - Required  : prefix string (Webdriver)
            login                - Required  : the email you use for authorization (Str)
            password             - Required  : the password you use for authorization (Str)
            delay_time           - Required  : delay between entering the password and pressing the login button (Int)
            desk_url             - Required  : link to downloadable whiteboard (Str)
            scroll_delay_time    - Required  : scroll delay (Int)
            html_tmp_name        - Required  : the name of the file generated during program execution (Str)
        """
        self.driver = driver
        self.login = login
        self.password = password
        self.delay_time = delay_time
        self.desk_url = desk_url
        self.scroll_delay_time = scroll_delay_time
        self.html_tmp_name = html_tmp_name
        
    def log_in(self):
        """
        Authorization on the pinterest.com
        """
        try:
            
            self.driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/button/div').click()
            self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.login)
            self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
            time.sleep(self.delay_time) 
            self.driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[5]/button/div').click()
            time.sleep(self.delay_time)
            
        except:
            print("Authorisation Error")
            pass
        
    
    def collection_of_html_file(self):
        """
        Creating an html file from a dynamically generated page
        """
        self.driver.get(self.desk_url) #переходим на доску
        
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # Wait to load page
            time.sleep(self.scroll_delay_time)
        
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            
            # Saving content to file        
            f = open(self.html_tmp_name , 'a')
            f.write(str(self.driver.page_source.encode('utf-8')))
            f.close() 
            
            # Scrolling the page
            if new_height == last_height:
                break
            last_height = new_height


