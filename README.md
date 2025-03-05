
# Kingsley Charm Finder

## Description

The **Kingsley Charm Finder** is a Python application with a GUI that allows users to search for specific charms listed on the Steam Market. It allows users to search by charm name, specify a range of template numbers, and scrape data from multiple pages of the Steam Market. The results are then sent via a Discord webhook with a link to the listing and the template number, making it easy to track and monitor specific charms.

The application is built using `tkinter` for the GUI, `requests` for HTTP requests, and `BeautifulSoup` for scraping the Steam Market pages.

![](https://i.imgur.com/xgamHhX.png)

## Features

- **Search for Charms**: Choose a charm from a dropdown menu, input a page range, and specify template number ranges.
- **Discord Webhook**: Results are sent to a Discord channel via a webhook, including a clickable link to the Steam Market listing and the charm's template number.
- **Multi-page Scraping**: Specify how many pages of the Steam Market you want to search.
- **Customizable Webhook**: You can set your own Discord Webhook URL for sending notifications.

## Installation

To run the application, follow the steps below:

### Prerequisites

Make sure you have Python 3 installed. You will also need to install the following libraries:

- `requests` for making HTTP requests.
- `beautifulsoup4` for parsing HTML content.
- `tkinter` for the graphical user interface.

### Step-by-step Installation

1. Clone or download the repository:
   ```bash
   git clone https://github.com/yourusername/kingsley-charm-finder.git
   ```

2. Navigate to the project directory:
   ```bash
   cd kingsley-charm-finder
   ```

3. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

4. Run the Python script:
   ```bash
   CS2 Rare Charm Finder.py
   ```

## How to Use

1. **Discord Webhook URL**: 
   - Paste your Discord webhook URL in the text box at the top. The default is `discord webhook url`, which you need to replace with your actual webhook URL.
   
2. **Select a Charm**:
   - Use the dropdown menu to select the charm you want to search for.

3. **Set Page Range**:
   - Enter the number of pages to search in the "Pages" textbox.

4. **Set Template Number Range**:
   - Enter the minimum and maximum template numbers to search within.

5. **Start Searching**:
   - Press the "Search" button to start the search. The results will be sent to the specified Discord webhook URL, showing each listing's charm template number and a link to the listing.

6. **Results**:
   - The application will scrape the Steam Market for listings matching your charm name and template number range. Each matching listing will be sent to the Discord channel with a clickable link.

## Example Output

When a charm is found within the specified range, you will receive a message in your Discord channel like:

```
Found charm with value: 12345 - [View Listing on Page 1](https://steamcommunity.com/market/listings/730/Charm%20%7C%20Baby%20Karat%20CT?page=1)
```

## Credits

- **KingsleyDotDev** – Developer of this project.

## License

This project is open-source and available under the [MIT License](LICENSE).
