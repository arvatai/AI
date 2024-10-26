import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def scrape_website_text(url, max_depth=1):
    scraped_content = {}

    def scrape_page(url, depth):
        if depth > max_depth:
            return

        try:
            response = requests.get(url)
            response.raise_for_status()  
            page_content = response.content

            soup = BeautifulSoup(page_content, 'html.parser')
            visible_texts = []
            hidden_texts = []

            for element in soup.find_all(string=True):
                parent = element.parent
                if parent.name not in ['script', 'style']:
                    # Check for hidden styles
                    is_hidden = False
                    if parent.has_attr('style'):
                        style = parent['style'].lower()
                        if 'display: none' in style or 'visibility: hidden' in style:
                            is_hidden = True

                    if is_hidden:
                        hidden_texts.append(element.strip())
                    else:
                        visible_texts.append(element.strip())

            visible_text = ' '.join(visible_texts)
            hidden_text = ' '.join(hidden_texts)

            cleaned_visible_text = re.sub(r'\s+', ' ', visible_text).strip()
            cleaned_hidden_text = re.sub(r'\s+', ' ', hidden_text).strip()

            # Save the content for this page
            scraped_content[url] = {
                'visible_text': cleaned_visible_text,
                'hidden_text': cleaned_hidden_text
            }

            # Find and follow links
            for link in soup.find_all('a', href=True):
                full_url = urljoin(url, link['href'])
                if full_url not in scraped_content:  # Avoid revisiting the same page
                    scrape_page(full_url, depth + 1)

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while scraping {url}: {e}")

    scrape_page(url, depth=1)
    return scraped_content

url = "https://adbrew.io/blog/"
scraped_data = scrape_website_text(url, max_depth=2)

for page_url, content in scraped_data.items():
    print(f"URL: {page_url}")
    print("Visible text:", content['visible_text'])
    print("Hidden text:", content['hidden_text'])
    print("\n" + "-"*80 + "\n")
