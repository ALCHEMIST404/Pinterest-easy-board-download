# -*- coding: utf-8 -*-
"""
Created on Fri May 14 04:27:50 2021

@author: Ирина
"""

import time
import requests
import os
import json
import traceback
import sys


from progress_bar import progress_bar
#from progress.bar import IncrementalBar
from itertools import groupby
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class pin_import:
    
    def __init__(self, export_dir, html_tmp_name):
        """
        Call in a loop to create terminal progress bar
        @params:
            export_dir         - Required  : folder for exporting images (Str)
            html_tmp_name      - Required  : the name of the file generated during program execution (Str)
        """
        self.export_dir = export_dir
        self.html_tmp_name = html_tmp_name
        
        
        
    def download_pin_from_desk(self, image_url):
        """
        Loading images from the pinterest board
        @params:
            image_url   - Required  : list of links to board images (List)
        """
        
        print("Beginning of cleaning images.")
        
        
        pr_bar = progress_bar(prefix = 'Download progress:', suffix = 'Complete', length = 50)
        pr_bar.print_progress_bar(0, len(image_url))
        
        
        for i in range(len(image_url)):
            try:
                img_url = "https://i.pinimg.com/564x/"+ image_url[i].split("https://i.pinimg.com/236x/")[1]            
                p = requests.get(img_url)
                
                out = open(self.export_dir+image_url[i].split("/")[-1], "wb")
                out.write(p.content)
                out.close()
                
                
                pr_bar.print_progress_bar(i + 1, len(image_url))
               
            except:
                pr_bar.print_progress_bar(i, len(image_url))
                pass  
            
        print("Download completed successfully.")
        
    def image_search(self):
        """
        Search for images in the downloaded file
        """
        
        print("Collection of images from the board is completed.")
        
        f = open(self.html_tmp_name, 'r')
        html_doc = f.read()
        f.close() 
        
        soup = BeautifulSoup(html_doc,"lxml")
        
        l = []
        
        for img in soup.find_all('img'):
            l.append(img.get('src'))
        
        l = [el for el, _ in groupby(l)]
        
        return l
