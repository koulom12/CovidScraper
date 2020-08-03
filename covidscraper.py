from bs4 import BeautifulSoup
import requests
import pandas as pd 

url = "https://www.worldometers.info/coronavirus/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'id':'main_table_countries_today'})
thead_rows= table.thead.find_all('tr')
tbody_rows = table.tbody.find_all('tr')
rows = table.find_all('tr')

columns = [v.text for v in thead_rows[0].find_all('th')]

df = pd.DataFrame(columns=columns)

def add_to_csv(df,tbody_rows):
    for i in range(1,len(tbody_rows)):
        tds = tbody_rows[i].find_all('td')
        values = [td.text for td in tds]
        df=df.append(pd.Series(values,index=columns),ignore_index=True)
        df.to_csv(r'C:\Users\Omesh\Desktop\CovidScraper'+'\coronavirus.csv',index=False)

add_to_csv(df,tbody_rows)