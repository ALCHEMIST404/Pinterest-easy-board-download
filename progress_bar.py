# -*- coding: utf-8 -*-
"""
Created on Fri May 14 04:28:35 2021

@author: Ирина
"""

class progress_bar:
    def __init__(self, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.printEnd = printEnd
        
        
        
    def print_progress_bar (self, iteration, total): # code from https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
        """
        percent = ("{0:." + str(self.decimals) + "f}").format(100 * (iteration / total))
        filledLength = int(self.length * iteration // total)
        bar = self.fill * filledLength + '-' * (self.length - filledLength)
        print(f'\r{self.prefix} |{bar}| {percent}% {self.suffix}', end = self.printEnd)
        # Print New Line on Complete
        if iteration == total: 
            print()    