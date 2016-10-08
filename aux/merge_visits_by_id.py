# coding: utf-8
df = DataFrame(data[0]['results'])
df = df[['date', 'total']]
df.columns = ['date', data[0]['item_id']]
for item in data[1:]:
    results = item['results']
    item_id = item['item_id']
    df_temp = DataFrame(results)
    df_temp = df_temp[['date', 'total']]
    df_temp.columns = ['date', item_id]
    df = pd.merge(df, df_temp, on='date')
    
