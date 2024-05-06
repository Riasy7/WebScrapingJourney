import requests
from bs4 import BeautifulSoup

# constants to facilitate the web scraping
BASE_URL = "https://forums.redflagdeals.com/"
HOT_DEALS_URL = f"{BASE_URL}hot-deals-f9/"

# function to fetch the url
def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# all functions to get the data from the website
def get_store(listing):
    element = listing.select_one('.topictitle_retailer') # select the element
    return element.text.strip() if element else "N/A" # return the text of the element if it exists, otherwise return "N/A"

def get_item(listing):
    element = listing.select_one('.topic_title_link') # repeat same for every function after, only changing the class name and the content we are scraping
    return element.text.strip() if element else "N/A"

def get_votes(listing):
    element = listing.select_one('.total_count_selector')
    return element.text.strip() if element else "N/A"

def get_username(listing):
    element = listing.select_one('.thread_meta_author')
    return element.text.strip() if element else "N/A"

def get_timestamp(listing):
    element = listing.select_one('.first-post-time')
    return element.text.strip() if element else "N/A"

def get_category(listing):
    element = listing.select_one('.thread_category a')
    return element.text.strip() if element else "N/A"

def get_replies(listing):
    element = listing.select_one('.posts')
    return element.text.strip() if element else "N/A"

def get_views(listing):
    element = listing.select_one('.views')
    return element.text.strip() if element else "N/A"

def get_url(listing):
    element = listing.select_one('.topic_title_link')
    return BASE_URL + element['href'] if element else "N/A"


# function that displays the latest deals
def display_latest_deals():
    soup = fetch_url(HOT_DEALS_URL) # fetch the url
    listings = soup.find_all("li", class_="row topic") # find all the listings
    print(f"Total deals found: {len(listings)}") # print the total number of deals

    # loop over the listings and print the data
    for listing in listings:
        store = get_store(listing)
        item = get_item(listing)
        votes = get_votes(listing)
        username = get_username(listing)
        timestamp = get_timestamp(listing)
        category = get_category(listing)
        replies = get_replies(listing)
        views = get_views(listing)
        url = get_url(listing)

        # print the data
        print(f"Store: {store}")
        print(f"Item: {item}")
        print(f"Votes: {votes}")
        print(f"Username: {username}")
        print(f"Timestamp: {timestamp}")
        print(f"Category: {category}")
        print(f"Replies: {replies}")
        print(f"Views: {views}")
        print(f"URL: {url}")
        print("-" * 50)

# function to analyze the deals per category
def analyze_deals_per_category():
    soup = fetch_url(HOT_DEALS_URL) # like before fetch the url

    category_counts = {} # create a dictionary to store the category counts

    # loop over the listings and get the category
    for listing in soup.find_all("li", class_="row topic"):

        category = get_category(listing) # get the category

        # if the category is already in the dictionary, increment the count
        if category in category_counts:
            category_counts[category] += 1

        # if not, add the category to the dictionary with a count of 1
        else:
            category_counts[category] = 1

    # print the results
    print("Deals by category:\n")

    # loop over the dictionary and print the category and the count
    for category, count in category_counts.items():
        print(f"{category.ljust(30)}: {str(count).rjust(2)} deals")


# function to find the top stores
def find_top_stores():
    number_of_stores = int(input("Enter the number of top stores to display: ")) # get the number of top stores from the user
    soup = fetch_url(HOT_DEALS_URL) # like before fetch the url

    store_counts = {} # create a dictionary to store the store counts
    listings = soup.find_all("li", class_="row topic") # find all the listings

    # loop over the listings and get the store
    for listing in listings:
        store = get_store(listing)
        if store in store_counts:
            store_counts[store] += 1
        else:
            store_counts[store] = 1

    top_stores = sorted(store_counts.items(), key=lambda item: item[1], reverse=True)[:number_of_stores]
    
    print("Top Stores:")
    for store, count in top_stores: # loop over the top stores and print the store and the count
        print(f"{store}: {count} deals")
    print("-" * 50) # print the results

# function to log the deal data
def log_deal_data():
    soup = fetch_url(HOT_DEALS_URL) # like before fetch the url
    base_url = HOT_DEALS_URL # set the base url

    category_counts = {} # create a dictionary to store the category counts

    # loop over the listings and get the category
    listings = soup.find_all("li", class_="row topic")
    for listing in listings:
        category_element = listing.select_one('.thread_category a')
        category_name = category_element.text.strip() if category_element else "N/A"
        if category_name in category_counts:
            category_counts[category_name] += 1
        else:
            category_counts[category_name] = 1

    # print the categories
    categories = sorted(category_counts.keys())
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    category_choice = int(input("Pick the number associated with the category: ")) # get the category choice from the user
    selected_category = categories[category_choice - 1]

    # log the deal data
    with open('deals_log.txt', 'w') as file:

        # loop over the listings and get the category
        for listing in listings:
            category_element = listing.select_one('.thread_category a')
            category = category_element.text.strip() if category_element else "N/A"
            if category == selected_category:
                deal_url_element = listing.select_one('.topic_title_link')
                if deal_url_element:
                    deal_url = base_url + deal_url_element['href']
                    file.write(deal_url + '\n')
    print("All links have been logged successfully.")


# main function to run the program
def main():

    # this is a smart way to run the menu by creating a dict that maps the options to the functions
    menu_options = {
        '1': display_latest_deals,
        '2': analyze_deals_per_category,
        '3': find_top_stores,
        '4': log_deal_data,
        '5': exit
    }

    # display
    while True:
        print("***** Web Scraping Journey *****")
        print("1. Display latest deals")
        print("2. Analyze deals per category")
        print("3. Find top stores")
        print("4. Log deal data")
        print("5. Exit")

        option = input("Choose an option: ")
        if option in menu_options:
            menu_options[option]()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
