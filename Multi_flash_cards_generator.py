import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


# function to collect collect the source
def url_name():
    temp_pad = []
    links_list = int(input("\nHow many links are you using? "))
    while len(temp_pad) < links_list:
        url_link = input("\nPaste here your link >> ")
        temp_pad.append(url_link)
    return temp_pad


# count the amount of flash cards to process
def fc_amount(data):
    fc_amount = sum([1 if isinstance(data[x], (str, int))
                 else len(data[x]) 
                 for x in data])
    return int(fc_amount / 2)


# Source link
urls = url_name()

print("\nProcessing your flashcards...")

# All the flash card data will be store in this dictionary
data = {"Front":[],"Back":[]}

# Going thru every url
for url in urls:

    # Webscraper settings
    agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    my_url = requests.get(url, headers=agent )
    html = my_url.content
    soup = bs(html, 'html.parser')
    
    # Iterating throught every flash card
    for i, (question, answer) in enumerate(zip(soup.select('a.SetPageTerm-wordText'), soup.select('a.SetPageTerm-definitionText')), 1):
        data['Front'].append(question.get_text(strip=True, separator='\n'))
        data['Back'].append(answer.get_text(strip=True, separator='\n'))

print(f"\nAll the flash cards have been processed...\nThere were {fc_amount(data)} cards processed!")

# Createng the a dataframe with the data
df = pd.DataFrame(data)

print("\nNow let's create the csv file!")
file_name = input("How would you like to call the file?(remember to add .csv) >> ")

# Saving the dataframe to a csv file
df.to_csv(file_name, index=False, header=False)

print("\nThe csv file has been saved to the same directory as this script.\nHappy Learning!!\n")