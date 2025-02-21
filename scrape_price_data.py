import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json


def get_hotel_nextday_price_booking(hotel_url):
    # Define headers to mimic a real browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Calculate tomorrow's date
    tomorrow = datetime.now() + timedelta(days=1)
    checkin_date = tomorrow.strftime("%Y-%m-%d")
    checkout_date = (tomorrow + timedelta(days=1)).strftime("%Y-%m-%d")

    # Define the parameters for the search
    params = {
        "checkin": checkin_date,
        "checkout": checkout_date,
        "group_adults": 1,
        "group_children": 0,
        "no_rooms": 1,
        "selected_currency": "USD"
    }

    # Send a GET request to the hotel page
    response = requests.get(hotel_url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the price element (you may need to inspect the page to find the correct class or id)
        price_element = soup.find("span", {"class": "prco-valign-middle-helper"})

        if price_element:
            price = price_element.text.strip()
            print(f"At this {hotel_url}, \n The price for tomorrow night is: {price}")
        else:
            print("Price element not found on the page.")
            price = "nan"
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        price = "nan"

    return price


# Function to save the results as a JSON file
def save_results(results, path):
    # Get the current date and hour for the filename
    now = datetime.now()
    filename = now.strftime("%Y-%m-%d_%H.json")

    # Save the dictionary as a JSON file
    with open(path + filename, "w") as file:
        json.dump(results, file, indent=4)
    print(f"Results saved to {path + filename}")


# Main script
if __name__ == "__main__":
    # hotels
    hotels = {
        "iroquois": "https://www.booking.com/hotel/us/the-iroquois-new-york.en-gb.html",
        "margaritaville": "https://www.booking.com/hotel/us/margaritaville-resort-times-square.en-gb.html",
        "knickerbocker": "https://www.booking.com/hotel/us/the-knickerbocker.en-gb.html",
        "plaza": "https://www.booking.com/hotel/us/the-plaza.en-gb.html",
        "ritz": "https://www.booking.com/hotel/us/the-ritz-carlton-new-york-central-park.en-gb.html",
        "netherland": "https://www.booking.com/hotel/us/the-sherry-netherland.en-gb.html",
        "panorama": "https://www.booking.com/hotel/us/panorama-vista-1-bedroom-2-bathroom-kitchen-suite.en-gb.html",
        "jetluxury": "https://www.booking.com/hotel/us/jet-luxury-the-signature-condo.en-gb.html",
        "marriott": "https://www.booking.com/hotel/us/marriott-s-grand-chateau-1-las-vegas.en-gb.html",
    }

    # Scrape prices for all hotels
    prices = {}
    for hotel, url in hotels.items():
        price = get_hotel_nextday_price_booking(url)
        prices[hotel] = price

    # Save the results as a JSON file
    path = "/media/data/pricedata_cesare/data/"
    # path = ""
    save_results(prices, path)
