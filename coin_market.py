from bs4 import BeautifulSoup
import requests
import pandas as pd

# Let's find some data.
page = requests.get('https://coinmarketcap.com')
soup = BeautifulSoup(page.content, 'html.parser')
c_table = soup.find(class_='col-xl-10 padding-top-1x')
the_currencies = c_table.find(class_='table-fixed-column-mobile compact-name-column') 
name = the_currencies.find_all(class_='currency-name-container link-secondary') ## find all coin names.
price = the_currencies.find_all(class_='price') ## find all price names.
market_cap = the_currencies.find_all(class_='no-wrap market-cap text-right') ## find all market_caps
volume24h = the_currencies.find_all(class_='volume') ## find volume (24h)
circulatingSupply = the_currencies.find_all(class_='no-wrap text-right circulating-supply')

## They return lists. That means, they're useful for us now. We can use them like name[23].get_text ... It returns Dogecoin.

## Our coin information lists. We will put elements into them.
coinName_list = []
price_list = []
marketCap_list = []
volume24h_list = []
circulatingSupply_list = []

## For getting all names and price and the other data.
for k in range(0,100):

    name_element = name[k].get_text()
    price_element = price[k].get_text()
    marketCap_element = market_cap[k].get_text().replace("\n","") ## clear that "\n"
    volume24h_element = volume24h[k].get_text()
    circulatingSupply_element = circulatingSupply[k].get_text()
    
    ## append data into the list.
    coinName_list.append(name_element)
    price_list.append(price_element)
    marketCap_list.append(marketCap_element)
    volume24h_list.append(volume24h_element)
    circulatingSupply_list.append(circulatingSupply_element)
    
## using pandas, dataframe. That way, we can see our data more neat.
dataframe_coinName = pd.DataFrame(coinName_list, columns= ['Name'])
dataframe_price = pd.DataFrame(price_list, columns = ['Price'])
dataframe_marketcap = pd.DataFrame(marketCap_list, columns=['Market Cap'])
dataframe_volume24h = pd.DataFrame(volume24h_list, columns=['Volume (24h)'])
dataframe_circulatingSupply = pd.DataFrame(circulatingSupply_list, columns=['Circulating Supply'])

## 'Concat' associate columns. In box brackets, you can see that we give first column (coin names) and then second column (prices) and the others.
myCurrencyTable = pd.concat([dataframe_coinName, dataframe_price, dataframe_marketcap, dataframe_volume24h, dataframe_circulatingSupply], axis = 1)

## Let's see our beautiful data.
print(myCurrencyTable)

## Maybe you cannot see that output clearly. Because there are many data, your IDE can't show it clearly. Use Spyder,
## you can see myCurrencyTable dataframe in Value Explorer box. Click on it. You will see myCurrencyTable dataframe.
