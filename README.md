# MissionToMars

 In this project, I have built a web application that scrapes various websites for data related to Mars and displays all the information in a single HTML page.
 The initial scraping was conducted using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. The following five websites were scraped for data related to Mars:
 1. NASA Mars News : https://mars.nasa.gov/news/
 2. JPL Mars Space Images : https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
 3. Mars Weather Twitter Account : https://twitter.com/marswxreport?lang=en
 4. Mars Facts : http://space-facts.com/mars/
 5. Mars Hemispheres : https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
 Once all the required information was scraped from the web, I created a new HTML page that displays all the information. For this purpose, I used MongoDB with Flask templating, HTML and BootStrap. 
 The newly-built application contains a button which scrapes real-time data and displays it on the HTML page.
