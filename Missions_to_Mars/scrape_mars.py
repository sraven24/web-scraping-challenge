# import necessary libraries
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    #define URL to scrape
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html

    #create soup
    soup = BeautifulSoup(html,'html.parser')

    #collect the latest News Title and Paragraph Text and assign them variables
    news_title = soup.find_all('div', class_='content_title')[0].text
    news_para = soup.find_all('div',class_='article_teaser_body')[0].text

    print(news_title)
    print(news_para)

    ###JPL Mars Space Images - Featured Image
    #define URL for the image scrape
    img_url = 'https://spaceimages-mars.com/'
    browser.visit(img_url)
    html = browser.html

    #create new soup
    soup = BeautifulSoup(html,'html.parser')


    image_src=soup.find_all('img', class_='headerimage fade-in')
    print(image_src)

    for element in image_src:
        print (element['src'])
        
    featured_image_url = img_url+element['src']

    ###Mars Facts

    #define URL to scrape
    url = 'https://galaxyfacts-mars.com/'
    all_tables = pd.read_html(url)
    all_tables[1]
    mars_specs = all_tables[1].to_html()

    ###Mars Hemispheres

    hemi_url = 'https://marshemispheres.com/'
    browser.visit(hemi_url)
    html = browser.html

    # create current soup
    soup = BeautifulSoup(html,'html.parser')

    # get the elements 
    hem_location = soup.find('div',class_='collapsible results')
    hem_items = hem_location.find_all('div',class_='item')

    # setup dictionary list to pick up each title and source
    hemisphere_image_urls = []

    # Use a for loop with error handling to find each pic title and src
    for item in hem_items:
        try:
                hem = item.find('div',class_='description')
                name = hem.h3.text
                hem_click = hem.a['href']
                browser.visit(hemi_url+ hem_click)
                html = browser.html
                soup = BeautifulSoup(html,'html.parser')
                img_source = soup.find('li').a['href']
                #img_source = soup.find('img',src)
                dictionary ={'title':name, 'image_url':img_source}
                hemisphere_image_urls.append(dictionary)
        except Exception as error:
                print(error)

    browserr.quit()

    scraped_info = {
          'NewsTitle':news_title,
          'NewsParagraph':news_para,
          'FeaturedImage':featured_image_url,
          'MarsTable': mars_specs,
          'Hemispheres': hemisphere_image_urls
          
    }

    return scraped_info

            

