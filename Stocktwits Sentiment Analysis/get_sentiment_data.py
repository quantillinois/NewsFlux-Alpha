import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver

# Modify stuff below using the path to your Chrome driver installation
cService = webdriver.ChromeService(executable_path='../utils/chromedriver-mac-arm64/chromedriver')
options = webdriver.ChromeOptions()
# options.add_argument('--profile-directory=Profile 3') # Set the path to Profile 3 (find profile that is logged into StockTwits by visiting chrome://version)
options.add_argument('--user-data-dir=/Users/blaineh2/Library/Application Support/Google/Chrome/Default')  # CHANGE to your path to Chrome profile (using default for now)
driver = webdriver.Chrome(service = cService, options=options)

#%%

data = [] 
stock = "META" # Define stock ticker 
"""
Below, plug in the JavaScript class names for elements you wish to scrape off of the StockTwits page.
Note that the last two class names are for the latest messages and the sentiment of each message. 
There is no predefined amount of posts rendered, so the number of these messages can vary.
Additionally, the message and the sentiment will alternate when it comes to extracted the text from the soup.
"""
class_names = [
    'SymbolPricing_updatedAmountFont__1uk1w text-[35px] font-normal SymbolPricing_updatedAmount__l65qv SymbolPricing_amount__xf2zd text-[35px] leading-10 font-light h-[36px]', #stock price today
    'Change_negative__uYjg2 Change_container__wg0u_ inline-flex gap-1 text-red', #amount the stock changed today
    'gauge_gagueNumber__my63f absolute text-[20px] top-[75%] left-[47.75%] z-10 font-semibold !text-white !top-[77%] text-[24px]', #sentiment for today on a scale from 1-100 (1 being negative, 100 being positive)
    'RichTextMessage_body__Fa2W1 whitespace-pre-wrap', #latest messages
    'StreamMessage_bullishText__RwLN0 StreamMessage_sentimentText__QN8J_ -ml-1 inline-block StreamMessage_regularFontWeight__cRmI5 !font-normal StreamMessage_WEB-2173__aMFOt', #sentiment for each message (here bullish)
    'StreamMessage_bearishText__1ajQJ StreamMessage_sentimentText__QN8J_ -ml-1 inline-block StreamMessage_regularFontWeight__cRmI5 !font-normal StreamMessage_WEB-2173__aMFOt' #sentiment for each message (here bearish)
]   
#%%
# Scrape data 
for _ in range(10): #try a max of 10 times
    stock_url = "https://stocktwits.com/symbol/" + stock
    driver.get(stock_url) # Web scraping
    sleep(1) # can also use randint() for the number of seconds

    # Getting a readable source with BeautifulSoup
    html = driver.page_source 
    soup = BeautifulSoup(html) 
    # Finding what we need 
    a = soup.findAll(class_ = class_names)
    if(len(a)==len(class_names)): # If stock does not have data
        break
    print(a)

if not a:
    print(f"Stock {a} not found")

else:
    with open("./stocktwits_data.txt", "w") as f:
        for item in a:
            f.write("%s\n" % item.text)


# Close driver
driver.quit()

# %%
