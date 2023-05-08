# -*- coding: utf-8 -*-
# Author : Dimitrios Zacharopoulos
# All copyrights to Obipixel Ltd
# 08 May 2023

#/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


# Print ASCII art
print("""
░█▀▄░█░▄▀▒░█▒█▒█▀▄░█▒░
▒█▄▀░█░▀▄█░▀▄█░█▀▄▒█▄▄
""")


def get_hyperlinks(url):
    """
    Given a URL, returns a set of unique hyperlinks found on the webpage.
    """
    try:
        # Make a request to the website
        print("Requesting website...")
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for 4xx or 5xx status codes
        print("Website received.")

        # Parse the HTML content of the website
        print("Parsing website content...")
        soup = BeautifulSoup(response.content, 'html.parser')
        print("Website content parsed.")

        # Find all unique hyperlinks
        print("Finding hyperlinks...\n")
        hyperlinks = set()
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and (href.startswith('http') or href.startswith('https')) and ('@2x.png' not in href) and ('@2x.png.webp' not in href):
                hyperlinks.add(href)
        print(f"{len(hyperlinks)} hyperlinks found.")
        return hyperlinks

    except (requests.exceptions.HTTPError, requests.exceptions.RequestException) as e:
        print(f"An error occurred: {e}")
        return set()

def save_links_to_file(links, url):
    """
    Given a set of links and a URL, writes the links to an HTML file named after the domain name in the URL.
    """
    domain = urlparse(url).netloc
    file_name = f"digURL-{domain}.html"
    with open(file_name, 'w') as f:
        # Write the HTML header and body tags
        f.write("<html><head><title>CheckWeb Report</title></head><body>\n")

        # Write the links as clickable hyperlinks
        for link in links:
            f.write(f'<a href="{link}">{link}</a><br>\n')

        # Write the HTML footer tag
        f.write("</body></html>")
    print(f"\nLinks saved to {file_name}")

def main():
    while True:
        # Prompt the user for a URL or the letter x to exit
        url = input('\nEnter a URL (eg. https://www.domain.com) or press the [x] key to Exit: ')
        if url.lower() == 'x':
            break

        # Get the unique hyperlinks
        hyperlinks = get_hyperlinks(url)

        # Print the unique hyperlinks
        print("----------------------------")
        for link in hyperlinks:
            print(link)

        # Save the links to an HTML file named after the domain name in the URL
        save_links_to_file(hyperlinks, url)

if __name__ == "__main__":
    main()
