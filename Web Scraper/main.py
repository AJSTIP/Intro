import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin

def scrape_fbi_most_wanted():
    # URL of the FBI Most Wanted page
    url = "https://www.fbi.gov/wanted/topten"
    
    # Send a GET request to the URL
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all wanted persons
    wanted_list = soup.find_all('div', class_='portal-type-person')
    
    # Create a directory to save the images
    os.makedirs("FBI_Most_Wanted", exist_ok=True)
    
    # Loop through each person and scrape their image and name
    for person in wanted_list:
        # Get the name of the person
        name = person.find('h3').text.strip()
        name = re.sub(r'[<>:"/\\|?*]', '_', name)  # Sanitize the name
        
        # Get the image URL
        img_tag = person.find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_url = urljoin(url, img_tag['src'])  # Handle relative URLs
            
            # Download the image
            try:
                img_response = requests.get(img_url, headers=headers, timeout=10)
                img_response.raise_for_status()
                # Save the image
                img_path = os.path.join("FBI_Most_Wanted", f"{name}.jpg")
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_response.content)
                print(f"Downloaded: {name}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download image for {name}: {e}")
        else:
            print(f"No image found for {name}")

if __name__ == "__main__":
    scrape_fbi_most_wanted()