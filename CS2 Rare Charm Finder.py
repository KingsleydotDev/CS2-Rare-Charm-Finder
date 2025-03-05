import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import urllib.parse

# Charm array
CHARMS = [
    "Charm | Baby Karat CT", "Charm | Baby Karat T", "Charm | Hot Howl", "Charm | Hot Wurst", "Charm | Diamond Dog",
    "Charm | Diner Dog", "Charm | Lil' Monster", "Charm | Lil' Squirt", "Charm | Semi-Precious", "Charm | Titeenium AWP",
    "Charm | Chicken Lil'", "Charm | Die-cast AK", "Charm | Disco MAC", "Charm | Glamour Shot", "Charm | Hot Hands",
    "Charm | Lil' Sandy", "Charm | Lil' Squatch", "Charm | Lil' Teacup", "Charm | Lil' Whiskers", "Charm | POP Art",
    "Charm | That's Bananas", "Charm | Baby's AK", "Charm | Backsplash", "Charm | Big Kev", "Charm | Hot Sauce",
    "Charm | Lil' Ava", "Charm | Lil' Cap Gun", "Charm | Lil' Crass", "Charm | Lil' SAS", "Charm | Pinch O' Salt",
    "Charm | Pocket AWP", "Charm | Stitch-Loaded", "Charm | Whittle Knife"
]

# Function to send webhook notifications
def send_webhook(message, webhook_url):
    data = {"content": message}
    requests.post(webhook_url, json=data)

# Function to scrape charm templates from the Steam Market page
def scrape_charm_template(charm_name, min_value, max_value, page_number, webhook_url):
    # URL encoded charm name for search
    encoded_charm_name = urllib.parse.quote(charm_name)
    url = f"https://steamcommunity.com/market/listings/730/{encoded_charm_name}?page={page_number}"
    
    # Send GET request to the page
    response = requests.get(url)
    
    if response.status_code != 200:
        send_webhook(f"Failed to fetch the webpage for {charm_name}. Status code: {response.status_code}", webhook_url)
        return []

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all div elements with the class 'market_listing_row_details_attribute'
    charm_template_elements = soup.find_all('div', class_='market_listing_row_details_attribute')

    # List to hold valid results
    results = []

    for element in charm_template_elements:
        # Check if "Charm Template:" is in the text of the div
        if "Charm Template:" in element.text:
            # Extract the number after "Charm Template:"
            charm_value = element.text.strip().replace("Charm Template:", "").strip()
            
            if charm_value.isdigit():
                charm_number = int(charm_value)
                
                # Check if the charm number is within the specified range
                if min_value <= charm_number <= max_value:
                    results.append(f"Found charm with value: {charm_number}")
    
    return results

# Function to search charms on Steam Market
def search_charms():
    webhook_url = webhook_url_entry.get()  # Get the webhook URL from the input field
    charm_name = charm_combobox.get()
    pages = pages_entry.get()
    try:
        pages = int(pages)
    except ValueError:
        send_webhook("Invalid page number entered.", webhook_url)
        return

    template_min = template_min_entry.get()
    template_max = template_max_entry.get()

    try:
        template_min = int(template_min)
        template_max = int(template_max)
    except ValueError:
        send_webhook("Invalid template number entered.", webhook_url)
        return

    send_webhook(f"Searching for charm '{charm_name}' on pages {pages} with template range {template_min}-{template_max}...", webhook_url)

    for page in range(1, pages + 1):
        # Scrape charm templates for the specified charm
        results = scrape_charm_template(charm_name, template_min, template_max, page, webhook_url)

        if results:
            for result in results:
                # Construct the page URL
                charm_url = f"https://steamcommunity.com/market/listings/730/{urllib.parse.quote(charm_name)}?page={page}"
                # Send the discord webhook with the charm listing, template number, and the page link
                message = f"{result} - [View Listing on Page {page}]({charm_url})"
                send_webhook(message, webhook_url)
        else:
            send_webhook(f"No listings found for {charm_name} on page {page}.", webhook_url)

    send_webhook(f"Finished searching for {charm_name}.", webhook_url)

# GUI setup
root = tk.Tk()
root.title("Kingsley Charm Finder")

# Webhook URL textbox
webhook_url_label = tk.Label(root, text="Discord Webhook URL:")
webhook_url_label.grid(row=0, column=0, padx=10, pady=5)
webhook_url_entry = tk.Entry(root, width=20)
webhook_url_entry.grid(row=0, column=1, padx=10, pady=5)
webhook_url_entry.insert(0, "discord webhook url")  # Default value

# Charm dropdown
charm_label = tk.Label(root, text="Select Charm:")
charm_label.grid(row=1, column=0, padx=10, pady=5)
charm_combobox = ttk.Combobox(root, values=CHARMS, width=20)
charm_combobox.grid(row=1, column=1, padx=10, pady=5)
charm_combobox.set(CHARMS[0])  # Set default charm

# Pages textbox
pages_label = tk.Label(root, text="Pages:")
pages_label.grid(row=2, column=0, padx=10, pady=5)
pages_entry = tk.Entry(root, width=10)
pages_entry.grid(row=2, column=1, padx=10, pady=5)
pages_entry.insert(0, "1")  # Default value

# Template number range
template_min_label = tk.Label(root, text="Min Template Number:")
template_min_label.grid(row=3, column=0, padx=10, pady=5)
template_min_entry = tk.Entry(root, width=10)
template_min_entry.grid(row=3, column=1, padx=10, pady=5)
template_min_entry.insert(0, "1")  # Default value

template_max_label = tk.Label(root, text="Max Template Number:")
template_max_label.grid(row=4, column=0, padx=10, pady=5)
template_max_entry = tk.Entry(root, width=10)
template_max_entry.grid(row=4, column=1, padx=10, pady=5)
template_max_entry.insert(0, "100000")  # Default value

# Search button
search_button = tk.Button(root, text="Search", command=search_charms)
search_button.grid(row=5, column=0, columnspan=2, pady=10)

# "By KingsleydotDev" text
credits_label = tk.Label(root, text="By KingsleydotDev", font=("Arial", 8), fg="gray")
credits_label.grid(row=6, column=0, columnspan=2, pady=5)

# Run the GUI
root.mainloop()
