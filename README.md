# Web Scraping Journey
# Author: Ahmad, github: https://github.com/Riasy7/

This read me just gives a general understanding of my program, throughout my program I place the necessary comments wherever I saw fit. 

Through this program I improved my web scraping skills using BeautifulSoup & requests Python libraries
There are two files, the code and the deals file to showcase writing and editing the mock up database for display purposes

## Main Function

The main menu is implemented with a while loop:

1. Display latest deals
2. Analyze deals per category
3. Find top stores
4. Log deal data
5. Exit

The user chooses a number to perform one of the following:

### Display latest deals

This option fetches the latest deals from the website and displays them. This is done using the `display_latest_deals()` function.

### Analyze deals per category

This option analyzes the deals per category and displays the results. This is done using the `analyze_deals_per_category()` function.

### Find top stores

This option finds the top stores based on the number of deals and displays them. This is done using the `find_top_stores()` function.

### Log deal data

This option logs the deal data for a selected category into a text file. This is done using the `log_deal_data()` function.

## Data Structure

The data scraped from the website is stored in a dictionary for easy access and manipulation. Each deal is a dictionary with keys representing different aspects of the deal (store, item, votes, etc.). This structure makes it easy to analyze and display the data.

## Constants

Constants are used to make the data scraping process easier and more readable. These constants represent the HTML tags and attributes used to locate the data on the website.

## Comments

Comments are used throughout the code to make it clearer and easier to understand. They explain what each part of the code is doing and why it is necessary.

## Functions

Here is a brief description of each function used in this program:

- `fetch_url(url)`: Fetches the URL and returns a BeautifulSoup object.
- `get_store(listing)`, `get_item(listing)`, `get_votes(listing)`, `get_username(listing)`, `get_timestamp(listing)`, `get_category(listing)`, `get_replies(listing)`, `get_views(listing)`, `get_url(listing)`: These functions extract specific data from a listing.
- `display_latest_deals()`: Fetches and displays the latest deals.
- `analyze_deals_per_category()`: Analyzes and displays the deals per category.
- `find_top_stores()`: Finds and displays the top stores based on the number of deals.
- `log_deal_data()`: Logs the deal data for a selected category into a text file.

## Thank you for your time :)