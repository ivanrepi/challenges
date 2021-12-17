#Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup

#FUNCTIONS:

def html_parsing(url,parser):
    return BeautifulSoup(requests.get(url).content, parser) 


def get_titles(soup):
    titles=[i.text for i in soup.find("table",{"class":"wikitable"}).find_all("th")]
    if titles[0]==titles[int(len(titles)/2)]:
        titles= [i.replace("\n","").split("[")[0] for i in titles[0:int(len(titles)/2)]]
    else:
        titles= [i.replace("\n","").split("[")[0] for i in titles]
    return titles

def get_columns(soup):
    rows=[i.text.split("\n")[1::2] for i in soup.find("table",{"class":"wikitable"}).find_all("tr")[1:]]
    return rows

def get_df(columns,titles):
    return pd.DataFrame(columns,columns=titles)

def create_csv(df,csv_name):
    name='wikipedia_tables_scraper/data/'+csv_name+'.csv'
    df_csv=df.to_csv(name, index=False)
    return df_csv

