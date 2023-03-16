# web-scraping-challenge

For this project, flask was used to setup an html webpage that can perform a scrape of various websites for showing data for the planet Mars.  Flask was used to setup a connection to the website and allow the user to push a button and scrape the information from the sites in a webdriver process.  The data was then collected and passed onto a Mongo database and then relayed to the website.  

# Installation
Simply run the app.py within the command prompt to start the server, while making sure there is an open connection to your MongoDB via MongoSH.  Type in your local server address into the search bar to access the Mission to Mars app. Make sure that you have Beautiful Soup, pandas, and splinter installed on your system.  This program is setup to run on Google Chrome and uses ChromeDriverManager to execute its scrape function.  If you want to use another browser for scraping then you would need to adjust the code accordingly.  On the site, click the button in the center of the screen and it will scrape the latest news, images, stats, and hemisphere photos of the planet Mars.

# Resources

Most of the information needed to create this app were found from the activities of week 12: Web scraping.  Other additional sources were as follows:

-finding the first image available - https://www.scrapingbee.com/blog/python-web-scraping-beautiful-soup/
-capturing an image src - https://proxyway.com/knowledge-base/how-to-get-src-attribute-from-img-tag-using-beautifulsoup
-converting a df to html string - https://www.geeksforgeeks.org/how-to-render-pandas-dataframe-as-html-table/
-removing the index from an html table -https://stackoverflow.com/questions/40546119/pandas-dataframe-to-html-remove-index
