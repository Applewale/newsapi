import requests
import pandas as pd

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2023-01-31&'
       'sortBy=popularity&'
       'apiKey=c60ed09b178748219133159415161db8')

def my_request(url):
    resp = requests.get(url)
    return resp.json()

def get_status(response):
    return response['status'] 

# Intrested in news titles and authors
def parse_json(response):
    articls_list = []
    for i in response['articles']:
        articls = { 'title' : i['title'], 'author' : i['author'] }
        articls_list.append(articls)
    return  articls_list

data =  my_request(url)
# checking the status of the response
print(get_status(data))

csv_df = pd.DataFrame(parse_json(data))

# Using Pandas to write json data as news.csv to Document folder on local drive 
csv_df.to_csv('/Users/apple/Documents/news.csv', index=False)
