import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.shadowfox.in"

try:
    print("Connecting to ShadowFox . . .")
    response = requests.get(url)
    response.raise_for_status()
    print("Successfully connected !!!")
    print("Parsing the Website's Data . . .")

    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a')
    print("Extracting all links and saving them in spreadsheet . . .")

    with open('shadow_data.csv','w',newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Link Text','URL'])
        for link in links:
            text = link.text.strip()
            href = link.get('href')

            if text and href:
                writer.writerow([text,href])
    
    print("Successfully saved data in shadow_data.csv !!!")

except requests.exceptions.RequestException as error_message:
    print("Oh Oh !!!")
    print("Scraper Tool has successfully caught an error without crashing.")
    print("Error Message: ",error_message)