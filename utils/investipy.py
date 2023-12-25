import requests
import pandas as pd
import yfinance as yf

def add_apac_volatility():
    apac = ["AXVI", "JNIV", "VHSI", "KSVKOSPI" ]
    for symbol in apac:
        url = f"http://api.scraperlink.com/investpy/?email=knitish1603@gmail.com&type=historical_data&product=indices&from_date=2021-01-01&to_date=2023-12-25&time_frame=Daily&symbol={symbol}"
        resp_dict = requests.get(url).json()
        vol_index = pd.DataFrame(resp_dict.get('data')).loc[:, ['rowDate', 'last_close']]
        vol_index["rowDate"] = vol_index['rowDate'].apply(lambda x: datetime.strptime(x, "%b %d, %Y"))
        vol_index["last_close"] = vol_index['last_close'].apply(pd.to_numeric, errors='coerce')
        vol_index["vol_scaled"] = vol_index["last_close"]/vol_index["last_close"].mean()
        # vol_index.to_csv(f"data/{symbol}.csv", index=False)
        return vol_index
    
def add_crypto_volatility():
    ticker = yf.Ticker('CVOL-USD')
    df = ticker.history(period='2y')
    # df.to_csv('data/CVI.csv')
    return df