import requests
from bs4 import BeautifulSoup
import os
import re

# Scrape the Walmart store locations from the specified URL
def scrape_walmart_locations(url_walmart):
    # Send a request to the Walmart store directory page
    response = requests.get(url_walmart)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the state sections
    state_sections = soup.find_all('div', class_='state-section')

    # Extract the store details from each state section
    store_details = []

    for section in state_sections:
        # Extract the state name
        state_name = section.find('h2', class_='state-name').text.strip()

        # Extract each store in the state
        store_listings = section.find_all('div', class_='store-listing')

        for store in store_listings:
            # Extract store details
            city_and_address = store.find('span', class_='city-address').text.strip()
            designation_and_info = store.find('span', class_='designation-info').text.strip()

            # Further processing to split city, address, designation, store number and opening date
            city, address = city_and_address.split(' - ')
            designation, store_num_and_date = designation_and_info.split(' (')
            store_num = re.search(r'store #(\d+)', store_num_and_date).group(1)
            open_date = re.search(r'opened (.+?)\)', store_num_and_date).group(1)

            store_details.append(f"{state_name} - {city} - {address} - {designation} (store #{store_num}, "
                                 f"opened {open_date})")

    return store_details

def save_to_file(data, file_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write the data to a file
    with open(file_path, 'w') as file:
        for line in data:
            file.write(line + '\n')

# URL of the Walmart store directory
url = 'https://www.walmart.com/store-directory'

# Scrape the Walmart store locations
store_data = scrape_walmart_locations(url)

# Save the scraped data to the specified file
output_path = '/data/raw/walmart_locations.raw.txt'
save_to_file(store_data, output_path)

print(f"Data scraped and saved to {output_path}")
