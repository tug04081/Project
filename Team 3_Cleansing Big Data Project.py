# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:38:41 2019

@author: tug04
"""

import bs4 as bs
import requests
import numpy
import csv


#Import all the necessary data into individual lists which are name after the month and year that contain the data
#the mini lists end at line 2364

#2004
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2004'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

#2-len(death)-36 is the range that contain the data 
i = 2
Jan04 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan04 = Jan04 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2004'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb04 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb04 = Feb04 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2004'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar04 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar04 = Mar04 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2004'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr04 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr04 = Apr04 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2004'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May04 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May04 = May04 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2004'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun04 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun04 = Jun04 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2004'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul04 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul04 = Jul04 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2004'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug04 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug04 = Aug04 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2004'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep04 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep04 = Sep04 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2004'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct04 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct04 = Oct04 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2004'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov04 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov04 = Nov04 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2004'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec04 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec04 = Dec04 + observations
    i = i + 1
#
#2005
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2005'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan05 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan05 = Jan05 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2005'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb05 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb05 = Feb05 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2005'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar05 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar05 = Mar05 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2005'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr05 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr05 = Apr05 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2005'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May05 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May05 = May05 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2005'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun05 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun05 = Jun05 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2005'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul05 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul05 = Jul05 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2005'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug05 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug05 = Aug05 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2005'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep05 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep05 = Sep05 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2005'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct05 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct05 = Oct05 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2005'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov05 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov05 = Nov05 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2005'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec05 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec05 = Dec05 + observations
    i = i + 1
#
#2006
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2006'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan06 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan06 = Jan06 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2006'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb06 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb06 = Feb06 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2006'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar06 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar06 = Mar06 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2006'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr06 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr06 = Apr06 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2006'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May06 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May06 = May06 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2006'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun06 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun06 = Jun06 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2006'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul06 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul06 = Jul06 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2006'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug06 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug06 = Aug06 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2006'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep06 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep06 = Sep06 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2006'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct06 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct06 = Oct06 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2006'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov06 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov06 = Nov06 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2006'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec06 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec06 = Dec06 + observations
    i = i + 1
#
#2007
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2007'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan07 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan07 = Jan07 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2007'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb07 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb07 = Feb07 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2007'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar07 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar07 = Mar07 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2007'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr07 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr07 = Apr07 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2007'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May07 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May07 = May07 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2007'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun07 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun07 = Jun07 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2007'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul07 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul07 = Jul07 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2007'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug07 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug07 = Aug07 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2007'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep07 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep07 = Sep07 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2007'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct07 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct07 = Oct07 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2007'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov07 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov07 = Nov07 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2007'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec07 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec07 = Dec07 + observations
    i = i + 1
#
#2008
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2008'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan08 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan08 = Jan08 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2008'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb08 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb08 = Feb08 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2008'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar08 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar08 = Mar08 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2008'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr08 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr08 = Apr08 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2008'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May08 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May08 = May08 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2008'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun08 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun08 = Jun08 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2008'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul08 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul08 = Jul08 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2008'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug08 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug08 = Aug08 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2008'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep08 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep08 = Sep08 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2008'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct08 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct08 = Oct08 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2008'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov08 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov08 = Nov08 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2008'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec08 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec08 = Dec08 + observations
    i = i + 1
#
#2009
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2009'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan09 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan09 = Jan09 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2009'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb09 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb09 = Feb09 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2009'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar09 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar09 = Mar09 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2009'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr09 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr09 = Apr09 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2009'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May09 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May09 = May09 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2009'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun09 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun09 = Jun09 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2009'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul09 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul09 = Jul09 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2009'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug09 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug09 = Aug09 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2009'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep09 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep09 = Sep09 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2009'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct09 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct09 = Oct09 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2009'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov09 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov09 = Nov09 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2009'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec09 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec09 = Dec09 + observations
    i = i + 1
#
#2010
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2010'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan10 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan10 = Jan10 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2010'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb10 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb10 = Feb10 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2010'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar10 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar10 = Mar10 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2010'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr10 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr10 = Apr10 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2010'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May10 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May10 = May10 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2010'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun10 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun10 = Jun10 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2010'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul10 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul10 = Jul10 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2010'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug10 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug10 = Aug10 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2010'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep10 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep10 = Sep10 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2010'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct10 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct10 = Oct10 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2010'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov10 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov10 = Nov10 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2010'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec10 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec10 = Dec10 + observations
    i = i + 1
#
#2011
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2011'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan11 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan11 = Jan11 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2011'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb11 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb11 = Feb11 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2011'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar11 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar11 = Mar11 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2011'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr11 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr11 = Apr11 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2011'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May11 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May11 = May11 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2011'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun11 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun11 = Jun11 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2011'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul11 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul11 = Jul11 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2011'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug11 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug11 = Aug11 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2011'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep11 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep11 = Sep11 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2011'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct11 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct11 = Oct11 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2011'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov11 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov11 = Nov11 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2011'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec11 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec11 = Dec11 + observations
    i = i + 1
#
#2012
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2012'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan12 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan12 = Jan12 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2012'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb12 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb12 = Feb12 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2012'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar12 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar12 = Mar12 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2012'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr12 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr12 = Apr12 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2012'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May12 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May12 = May12 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2012'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun12 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun12 = Jun12 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2012'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul12 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul12 = Jul12 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2012'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug12 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug12 = Aug12 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2012'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep12 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep12 = Sep12 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2012'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct12 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct12 = Oct12 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2012'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov12 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov12 = Nov12 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2012'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec12 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec12 = Dec12 + observations
    i = i + 1
#
#2013
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2013'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan13 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan13 = Jan13 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2013'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb13 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb13 = Feb13 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2013'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar13 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar13 = Mar13 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2013'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr13 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr13 = Apr13 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2013'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May13 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May13 = May13 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2013'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun13 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun13 = Jun13 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2013'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul13 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul13 = Jul13 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2013'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug13 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug13 = Aug13 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2013'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep13 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep13 = Sep13 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2013'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct13 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct13 = Oct13 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2013'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov13 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov13 = Nov13 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2013'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec13 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec13 = Dec13 + observations
    i = i + 1
#
#2014
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2014'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan14 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan14 = Jan14 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2014'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb14 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb14 = Feb14 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2014'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar14 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar14 = Mar14 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2014'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr14 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr14 = Apr14 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2014'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May14 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May14 = May14 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2014'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun14 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun14 = Jun14 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2014'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul14 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul14 = Jul14 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2014'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug14 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug14 = Aug14 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2014'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep14 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep14 = Sep14 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2014'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct14 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct14 = Oct14 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2014'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov14 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov14 = Nov14 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2014'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec14 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec14 = Dec14 + observations
    i = i + 1
#
#2015
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2015'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan15 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan15 = Jan15 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2015'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb15 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb15 = Feb15 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2015'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar15 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar15 = Mar15 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2015'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr15 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr15 = Apr15 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2015'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May15 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May15 = May15 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2015'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun15 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun15 = Jun15 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2015'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul15 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul15 = Jul15 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2015'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug15 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug15 = Aug15 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2015'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep15 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep15 = Sep15 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2015'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct15 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct15 = Oct15 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2015'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov15 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov15 = Nov15 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2015'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec15 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec15 = Dec15 + observations
    i = i + 1
#
#2016
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2016'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan16 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan16 = Jan16 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2016'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb16 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb16 = Feb16 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2016'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar16 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar16 = Mar16 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2016'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr16 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr16 = Apr16 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2016'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May16 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May16 = May16 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2016'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun16 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun16 = Jun16 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2016'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul16 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul16 = Jul16 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2016'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug16 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug16 = Aug16 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2016'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep16 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep16 = Sep16 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2016'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct16 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct16 = Oct16 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2016'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov16 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov16 = Nov16 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2016'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec16 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec16 = Dec16 + observations
    i = i + 1
#
#2017
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2017'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan17 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan17 = Jan17 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2017'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb17 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb17 = Feb17 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2017'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar17 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar17 = Mar17 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2017'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr17 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr17 = Apr17 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2017'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May17 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May17 = May17 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2017'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun17 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun17 = Jun17 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2017'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul17 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul17 = Jul17 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2017'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug17 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug17 = Aug17 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2017'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep17 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep17 = Sep17 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2017'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct17 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct17 = Oct17 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2017'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov17 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Nov17 = Nov17 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_December_2017'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Dec17 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Dec17 = Dec17 + observations
    i = i + 1
#
#2018
url = 'https://en.wikipedia.org/wiki/Deaths_in_January_2018'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jan18 = []
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jan18 = Jan18 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_February_2018'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Feb18 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Feb18 = Feb18 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_March_2018'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Mar18 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Mar18 = Mar18 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_April_2018'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Apr18 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Apr18 = Apr18 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_May_2018'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
May18 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    May18 = May18 + observations
    i = i + 1
#


url = 'https://en.wikipedia.org/wiki/Deaths_in_June_2018'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jun18 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jun18 = Jun18 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_July_2018'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Jul18 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Jul18 = Jul18 + observations
    i = i + 1
#

url = 'https://en.wikipedia.org/wiki/Deaths_in_August_2018'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Aug18 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Aug18 = Aug18 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_September_2018'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Sep18 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Sep18 = Sep18 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_October_2018'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Oct18 = []    
while i < len(death)-36:
    observations = death[i].text.split('\n')
    Oct18 = Oct18 + observations
    i = i + 1
#
    
url = 'https://en.wikipedia.org/wiki/Deaths_in_November_2018'
re = requests.get(url)
soup = bs.BeautifulSoup(re.content, 'lxml')
death = soup.find_all('ul')

i = 2
Nov18 = []    
while i < len(death)-37:
    observations = death[i].text.split('\n')
    Nov18 = Nov18 + observations
    i = i + 1
#ListEnd




#I concatenate all the mini lists into a central list to work
    
NotableDeath = numpy.concatenate((Jan04,Feb04,Mar04,Apr04,May04,Jun04,Jul04,Aug04,Sep04,Oct04,Nov04,Dec04,Jan05,Feb05,Mar05,Apr05,May05,Jun05,Jul05,Aug05,Sep05,Oct05,Nov05,Dec05,Jan06,Feb06,Mar06,Apr06,May06,Jun06,Jul06,Aug06,Sep06,Oct06,Nov06,Dec06,Jan07,Feb07,Mar07,Apr07,May07,Jun07,Jul07,Aug07,Sep07,Oct07,Nov07,Dec07,Jan08,Feb08,Mar08,Apr08,May08,Jun08,Jul08,Aug08,Sep08,Oct08,Nov08,Dec08,Jan09,Feb09,Mar09,Apr09,May09,Jun09,Jul09,Aug09,Sep09,Oct09,Nov09,Dec09,Jan10,Feb10,Mar10,Apr10,May10,Jun10,Jul10,Aug10,Sep10,Oct10,Nov10,Dec10,Jan11,Feb11,Mar11,Apr11,May11,Jun11,Jul11,Aug11,Sep11,Oct11,Nov11,Dec11,Jan12,Feb12,Mar12,Apr12,May12,Jun12,Jul12,Aug12,Sep12,Oct12,Nov12,Dec12,Jan13,Feb13,Mar13,Apr13,May13,Jun13,Jul13,Aug13,Sep13,Oct13,Nov13,Dec13,Jan14,Feb14,Mar14,Apr14,May14,Jun14,Jul14,Aug14,Sep14,Oct14,Nov14,Dec14,Jan15,Feb15,Mar15,Apr15,May15,Jun15,Jul15,Aug15,Sep15,Oct15,Nov15,Dec15,Jan16,Feb16,Mar16,Apr16,May16,Jun16,Jul16,Aug16,Sep16,Oct16,Nov16,Dec16,Jan17,Feb17,Mar17,Apr17,May17,Jun17,Jul17,Aug17,Sep17,Oct17,Nov17,Dec17,Jan18,Feb18,Mar18,Apr18,May18,Jun18,Jul18,Aug18,Sep18,Oct18,Nov18), axis=0)

#Name
#Try statement to see if the second value in each line, which the age usually reside, is a title of the person.
# If yes then append both the name and the title to the name list. 
# The else and the exception clause is to catch the error if a line is only one value long.
i = 0
allname = []
while i < len(NotableDeath):
        
    nam = NotableDeath[i].split(",")
    try:
        if len(nam[1]) > 6:
            allname.append(",".join(nam[0:2]))
        else:
            allname.append(nam[0])
    except IndexError:
        allname.append(nam[0])
    i = i + 1
print(allname)

#name and tittle
# Replace the space with underscore for the Page Title
i = 0
underscore = []
while i < len(allname):
    try:
        name_ = allname[i].replace(" ", "_")
        underscore.append(name_)
    except AttributeError:
        underscore.append("error")
    i = i + 1
print(underscore)

#age
#Try statement to see if the lenth of the second value in each line, which the age usually reside
# Is less than 6. If yes then append that. If not then append the next value
# The else and the exception clause is to catch the error if a line is only one value long.
i = 0
allage = []

while i < len(NotableDeath):
        
    age = NotableDeath[i].split(",")
    try:
        if len(age[1]) < 6:
            allage.append(age[1])
        else:
            allage.append(age[2])
    except IndexError:
        allage.append(age[0])

    i = i + 1
print(allage)
#Age to interger    
newage = []
for s in allage:
    try:    
        age = int(s)
    except ValueError:
        age = -1 

    newage.append(age)
    
print(newage)

#Try statement to see if the third value in each line, which the value that contain the demonym usually reside,
# is correct of the person.
# If yes then append it to the list. 
# The else and the exception clause is to catch the error if a line is only one value long.
#Nationality    
i = 0
nation = []
while i < len(NotableDeath):
        
    nat = NotableDeath[i].split(",")

    try:
        if len(nat[2]) > 6:
            nation.append(nat[2])
        else:
            nation.append(nat[3])
    except IndexError:
        nation.append("error")

    i = i + 1
print(nation)

#Find the demonym
#find the first value where the demonym usually is
i = 0
demonym = []
while i < len(nation):
    nati = nation[i].split()
    try:
        demonym.append(nati[0])
    except IndexError:
        demonym.append("error")
    i = i + 1

print(demonym)


with open('NotableDeathProject.csv', 'w', newline='', encoding="utf-8") as csvfile:
    fieldnames = ['PAGE_TITTLE', 'NAME', 'AGE', 'DEMONYM_1', 'DESCRIPTION']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()


    for i in range(len(allname)):
        writer.writerow({'PAGE_TITTLE':underscore[i], 'NAME': allname[i], 'AGE': newage[i], 'DEMONYM_1': demonym[i], 'DESCRIPTION': NotableDeath[i]})
#    Take out the end and begining
    
    