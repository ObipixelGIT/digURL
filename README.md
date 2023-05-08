# digURL
DigURL is a hyperlink scraper

## How the script works?

- DigURL scrapes a webpage and returns a set of unique hyperlinks found on the webpage.
- The hyperlinks are saved to an HTML file named after the domain name in the URL.
- The script uses the requests library to make a request to the website, the BeautifulSoup library to parse the HTML content of the website, and the urllib library to parse the URL.
- The script also includes error handling for exceptions that may occur during the request process.

## Preparation

The following Python modules must be installed:
```bash
pip3 install requests, beautifulsoup4
```

## Permissions

Ensure you give the script permissions to execute. Do the following from the terminal:
```bash
sudo chmod +x digURL.py
```

## What to do next?

After installing the necessary libraries, and giving the script permissions to execute, you can run this script by executing the script file in your terminal or IDE. When prompted, enter a URL or the letter "x" to exit the program. The script will then print the unique hyperlinks found on the webpage and save them to an HTML file named after the domain name in the URL.

## Usage
```bash
sudo python3 digURL.py

Enter a URL (eg. https://www.domain.com) or press the [x] key to Exit::
```

## Sample script
```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

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

```

## Sample output
```
sudo python3 digURL.py

python3 digURL.py                                                                                          

░█▀▄░█░▄▀▒░█▒█▒█▀▄░█▒░
▒█▄▀░█░▀▄█░▀▄█░█▀▄▒█▄▄


Enter a URL (eg. https://www.domain.com) or press the [x] key to Exit: https://www.obipixel.com
Requesting website...
Website received.
Parsing website content...
Website content parsed.
Finding hyperlinks...

10 hyperlinks found.
----------------------------
.....
```

## Disclaimer
"The scripts in this repository are intended for authorized security testing and/or educational purposes only. Unauthorized access to computer systems or networks is illegal. These scripts are provided "AS IS," without warranty of any kind. The authors of these scripts shall not be held liable for any damages arising from the use of this code. Use of these scripts for any malicious or illegal activities is strictly prohibited. The authors of these scripts assume no liability for any misuse of these scripts by third parties. By using these scripts, you agree to these terms and conditions."

## License Information

This library is released under the [Creative Commons ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/). You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to use our code, you email us with a link to the product being created and/or sold. We want bragging rights that we helped (in a very small part) to create your 9th world wonder. We would like the opportunity to feature your work on our homepage.
