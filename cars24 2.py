from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

car_info_list = []
edf = pd.DataFrame()
filename = 'cars'


def save_data(filename, data):
    f = open(fr'F:\data science\pandas\{filename}.json', 'w')
    json.dump(data, f, indent=2)


def convert_image(v):
    try:
        return fr'https://fastly-production.24c.in/{v["url"]}'
    except:
        return ''


for i in range(1,601):
    url = f'https://api-sell24.cars24.team/buy-used-car?sort=P&serveWarrantyCount=false&gaId=1656381752.1658676791&page={i}&storeCityId={i}&pinId=110001'

    response = requests.get(url)

    data = response.json()['data']['content']

    save_data(filename, data)

    df = pd.read_json(fr'F:\data science\pandas\{filename}.json')
    edf = pd.concat([edf, df])

edf['mainImage'] = edf['mainImage'].apply(convert_image)
edf['frontImage'] = edf['frontImage'].apply(convert_image)
edf['inspectionMainImage'] = edf['inspectionMainImage'].apply(convert_image)
edf=edf.reset_index()
edf.to_csv(fr'F:\data science\pandas\{filename}.csv')
edf.to_excel(fr'F:\data science\pandas\{filename}.xlsx')
print(edf)