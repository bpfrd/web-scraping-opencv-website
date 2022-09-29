#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import pdfkit

browser = webdriver.Chrome('~/Downloads/chromedriver_linux64/chromedriver')

start_url = f'https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html'
browser.get(start_url)
all_links = []

def crawler():

    _ = browser.find_elements(by=By.CSS_SELECTOR, value='body > div.contents > div > ul > li > p > a')
    links = [ (i.get_property('text'), i.get_property('href')) for i in _]
    for name, link in links:
        print(name, ' ==> ', link)
        all_links.append((name, link))
        browser.get(link)
        crawler()

crawler()

for i, (name, link) in enumerate(all_links):

    fname = f'opencv/{i:04d}--{name.replace(" ", "-")}.pdf'
    pdfkit.from_url(link, fname)

