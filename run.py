# -*- coding: utf-8 -*-
"""

Created on Wed May 12 02:40:34 2021

@author: Irina Sokolova
"""
import time
import requests
import os
import json
import traceback
import sys

from pin_downloader import pin_downloader
from pin_import import pin_import
from progress.bar import IncrementalBar
from itertools import groupby
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


login = "test@gmail.com"  # The email you use for authorization
password = "password"       # The password you use for authorization

export_dir = "export_directory/" # Folder for exporting images
desk_url = "https://www.pinterest.ru/alchemist404/test_pin_down/" # The link to the Pinterest board you want to download

html_tmp_name = "temp.html" # HTML file adjusted automatically

delay_time = 15 # If Pinterest does not have time to log in before going to your board, change this parameter
scroll_delay_time = 3 # Page scrolling delay. If images fail to load, increase this parameter


def quick_settings():
    # Deleting old session data
    if os.path.exists(html_tmp_name) == True:
        os.remove(html_tmp_name)
        
    # Create a new folder for exporting images, if it has not been created yet
    os.makedirs(export_dir,exist_ok=True)

def main():    
    # Basic program settings
    quick_settings() 
    
    # Driver setting
    driver = webdriver.Chrome("Chrome Driver/chromedriver.exe")  
    driver.get("https://www.pinterest.com/") 
        
    # Сollection of images from pinterest
    pinterest_downloader = pin_downloader(driver, login,password,delay_time,desk_url,scroll_delay_time,html_tmp_name)
    pinterest_downloader.log_in()   
    pinterest_downloader.collection_of_html_file() 
    
    # Shutting down the driver    
    driver.close() 
    
    # Loading images
    pinterest_import_image = pin_import(export_dir, html_tmp_name)
    pinterest_import_image.download_pin_from_desk(pinterest_import_image.image_search())
    
    
if __name__ == "__main__":
    main()    
