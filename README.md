# 🕸 Web Scraping Journey
# Author: Ahmad
Github: https://github.com/Riasy7/

This read me just gives a general understanding of my program, throughout my program I place the necessary comments wherever I saw fit. 

This script is used to scrape data from the "Hot Deals" section of the RedFlagDeals forum (https://forums.redflagdeals.com/hot-deals-f9/). 

It uses the BeautifulSoup and requests libraries to fetch and parse the HTML of the website. 

The data scraped includes the store, item, votes, username, timestamp, category, replies, and views for each deal listed on the website. 

This data is then used for various purposes such as displaying the latest deals, analyzing deals per category, finding the top stores, and logging deal data.

There are two files, the code and the deals file to showcase writing and editing the mock up database for display purposes

## 📦 Technologies

  - `Python`
  - `Beautiful Soup`

## ✅ Main Function

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

## 📈 Data Structure

The data scraped from the website is stored in a dictionary for easy access and manipulation. Each deal is a dictionary with keys representing different aspects of the deal (store, item, votes, etc.). This structure makes it easy to analyze and display the data.
![Data Structures](https://miro.medium.com/v2/resize:fit:800/1*xGgaEhVE5dMD-R8krQG4PQ.gif)

## Constants

Constants are used to make the data scraping process easier and more readable. These constants represent the HTML tags and attributes used to locate the data on the website.

## Functions

Here is a brief description of each function used in this program:

- `fetch_url(url)`: Fetches the URL and returns a BeautifulSoup object.
- `get_store(listing)`, `get_item(listing)`, `get_votes(listing)`, `get_username(listing)`, `get_timestamp(listing)`, `get_category(listing)`, `get_replies(listing)`, `get_views(listing)`, `get_url(listing)`: These functions extract specific data from a listing.
- `display_latest_deals()`: Fetches and displays the latest deals.
- `analyze_deals_per_category()`: Analyzes and displays the deals per category.
- `find_top_stores()`: Finds and displays the top stores based on the number of deals.
- `log_deal_data()`: Logs the deal data for a selected category into a text file.


### 🤔🔑 Improvements

If we look at this from a larger scale, and this was a application hosted online with someone constantly using it. There would be serveral things that I learned that we could consider to improve this as if it were a large scale application.

  1. **Data Caching**: Currently, the program scrapes the website every time it runs. This could be inefficient and slow, especially if the data doesn't change frequently it will just slow down the whole process. To fix this, We could implement a caching mechanism where the data is stored locally and updated at regular intervals (up to programmer to decide intervalS). This way, we only scrape the website when necessary, reducing the load on both our program and the server we're scraping!
  
  2. **Modularization**: Right now the code is just 1 file, so the code could be split into more modules, each responsible for a specific task. For example, one module could handle fetching and parsing the data, another could handle analyzing the data, and another could handle displaying the data. This would make the code easier to maintain and test.
  
  3. **Error Handling**: While the `fetch_url` function does some error handling, we could improve this by adding more specific error messages and handling more types of exceptions.
  
  4. **Testing**: Currently, there are no tests for the code. Adding unit tests would help ensure that the code is working as expected and make it easier to catch and fix bugs. Using correct testing and debugging procedures is more "compliant".
  
  5. **Configuration**: The constants in the code could be moved to a configuration file. This would make it easier to change these values without modifying the code. For example, the base URL could be changed in the configuration file if the website changes its URL structure.
  
  6. **Documentation**: While the code is pretty well commented, we could add more detailed docstrings to the functions. This would make it easier for other developers to understand what each function does, what parameters it takes, and what it returns.
  
  7. **Performance**: If the program becomes slow with large amounts of data, we could look into performance optimizations. For example, we could use a faster parser or use multithreading to scrape multiple pages at once.
  
  8. **Data Storage**: If the amount of data becomes large, storing it in a dictionary might not be the most efficient solution. We could look into using a database to store the data, which would also make it easier to query and analyze the data.

At the end of the day this is a really simple implementation, but it gives us an idea on how a large scale application would consider doing things... Which is very interesting!
<br>
<img src="https://cdn.dribbble.com/users/962944/screenshots/14138307/media/ca3377660c3d2053c9d91ac175871429.gif" width="500" height="375">
<br>
## Thank you for your time :)
