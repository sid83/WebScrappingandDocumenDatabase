# import dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd

# define the chromedriver path
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)

# define a dictionary to store results
scraped_data = {}

# define function to scrape data from five different websites
def mars_scrape():
    browser = init_browser()

    # 1. NASA latest Mars News
    url_1 = "https://mars.nasa.gov/news/"
    browser.visit(url_1)
    soup_1 = BeautifulSoup(browser.html,'html.parser')
    try:
        news_items = soup_1.find_all('li',class_='slide')
        news_title = news_items[0].find('div', class_='content_title').find('a').text
        news_p = news_items[0].find('div', class_='article_teaser_body').text
    except AttributeError as e1:
        print(e1)

    # 2. JPL Mars Space Images - Featured Image
    url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_2)
    soup_2 = BeautifulSoup(browser.html,'html.parser')
    image = soup_2.find('article', class_='carousel_item')
    image_url = image['style']
    img_url = image_url.split("'")[1]
    featured_image_url = url_2[:24] + img_url

    # 3. Mars Weather
    url_3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_3)
    soup_3 = BeautifulSoup(browser.html,'html.parser')
    mars_weather_tweets = soup_3.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")

    # filtering tweets to mars weather tweets and saving in a list "mars_weather"
    mars_weather = []
    for tw in mars_weather_tweets:
        tweet = tw.text
        if 'Sol' in tweet:
            mars_weather.append(tweet)
    weather = mars_weather[0]
    
    mars_weather_latest = weather

    # 4. Mars Facts  
    url_4 = "http://space-facts.com/mars/"
    tables = pd.read_html(url_4)
    df = tables[0]
    html_table = df.to_html(header=None, index=False)

    # 5. Mars Hemispheres
    url_5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_5)
    soup_5 = BeautifulSoup(browser.html,'html.parser')
    results = soup_5.find_all('div', class_='description')
    hemispheres_list = []
    for result in results:
        title = result.find('a',class_="itemLink product-item").text
        browser.click_link_by_partial_text(title)
        soup_6 = BeautifulSoup(browser.html,'html.parser')
        partialImgUrl = soup_6.find('img',class_="wide-image")["src"]
        img_url = url_5[ :29] + partialImgUrl
        dict_ = {"title": title,
                "img_url": img_url}
        hemispheres_list.append(dict_)
        browser.click_link_by_partial_text('Back')  

    scraped_data = {"Mars_News_Title": news_title,
                    "Mars_News_Details": news_p,
                    "Mars_Image_Url": featured_image_url,
                    "Mars_weather": mars_weather_latest,
                    "Mars_Facts": html_table,
                    "Mars_hemispheres": hemispheres_list }

    return scraped_data





