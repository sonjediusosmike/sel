import requests
from bs4 import BeautifulSoup

# ascii art
print(
        """
███████╗███████╗███████╗███████╗██╗   ██╗
██╔════╝██╔════╝██╔════╝██╔════╝██║   ██║
███████╗█████╗  █████╗  ███████╗██║   ██║
╚════██║██╔══╝  ██╔══╝  ╚════██║██║   ██║
███████║███████╗██║     ███████║╚██████╔╝
╚══════╝╚══════╝╚═╝     ╚══════╝ ╚═════╝ 
                                         """
    )

# URL of the page to scrape
URL = input("URL:")  # Replace with the actual URL
# Send an HTTP request to the URL
response = requests.get(URL)
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all occurrences of a key word.
    i = input("keyword:")
    text = soup.get_text()
    occurrences = text.lower().count(i)
    print(f"Number of occurrences of {i}: {occurrences}")

    # Print sentences containing the word "example"
    sentences = text.split(".")
    for sentence in sentences:
        if "example" in sentence.lower():
            print(sentence.strip())
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
