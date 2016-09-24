# coding: utf-8
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

import requests
import pandas as pd

from pandas import Series, DataFrame

# sets query and makes request to API
query = "kit painel solar"
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