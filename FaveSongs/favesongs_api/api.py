import requests
def favesongs_api():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSCO.LON&outputsize=compact&apikey=AIUKC4OCZK7GZRVO'

    r = requests.get(url)
    data = r.json()

    print(data)


favesongs_api()
