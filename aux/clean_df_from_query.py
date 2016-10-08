# coding: utf-8
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

import requests
import pandas as pd

from pandas import Series, DataFrame

# sets query and makes request to API
#query = "kit painel solar"
query = input('Qual a query desejada? ')
url = "https://api.mercadolibre.com/sites/MLB/search?q="+query
data = requests.get(url).json()

# saves content from json in variable
results = data["results"]

# converts to a pandas df
df = DataFrame(results)

# gets only main columns
df = df[["id", "title", "price", "sold_quantity", "available_quantity"]]

# sorts items by sold quantity and deletes duplicates with less sales (assuming they'd be 0)
df = df.sort_values(by="sold_quantity", ascending=False)
df = df.drop_duplicates(subset=['title'], keep='first')

# gets top 10 sold items ML ids in a list
ids = df.id.values[0:10]

# makes comma-separated string from list to use in URL
ids_string = ','.join(ids)

#### Get visits by days from items in ids_string

days = 365 # from 365 days ago
url = 'https://api.mercadolibre.com/items/visits/time_window?ids=' + ids_string +'&last=' + str(days) + '&unit=day'

data = requests.get(url).json()

# initialize a df with the first item out of 10 (top ten in ids_string)
df = DataFrame(data[0]['results'])

# gets only main columns
df = df[['date', 'total']]

# renames 'total' to item's ID
df.columns = ['date', data[0]['item_id']]

# iterates over data items to merge all 'total' columns into same df
for item in data[1:]:
    results = item['results']
    df_temp = DataFrame(results)
    df_temp = df_temp[['date', 'total']]
    df_temp.columns = ['date', item['item_id']]
    df = pd.merge(df, df_temp, on='date')













