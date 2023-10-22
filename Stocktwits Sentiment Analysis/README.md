
Blaine Hill
Newsflux Alpha, Quant @ Illinois
Fall 2023

Description:
Website scraper for [StockTwits](https://stocktwits.com/) to extract sentiment of tweets and of stock tickers over time.
This website has lots of valuable natural language tweets along with human labeled sentiment (the person who posts a tweet clicks if their tweet is bullish or bearish) to finetune a general language model for momentum trading/financial language modeling.

Todos:
1. Convert output from text files into pd dataframe and save as csv
2. Solve selenium + macos bug either utilizing a linux server
    1. Scrape more sentiments by logging in
3. Extract more messages other than from the latest tab
    1. This will require figuring out how to "click" or move to another part of the webpage to get these.
4. Run this scraper on many stocks.

Bugs:
* Cannot open link with [logged in chrome profile on mac](https://stackoverflow.com/questions/60117232/selenium-google-login-block) on macos only. Need this to look at previous sentiment milestones.

Notes:

In order to run, you will need to install chromedriver with the latest version of chrome. This allows selenium to work.
The included chromedriver-mac-arm64 folder is for M1 Mac users (like me).