import requests
import csv

eodapi = "your_eod_key"
vantagekey = "your_vantage_key"

def get_ticker_list(exchange_code, api_key):
    url = f"https://eodhistoricaldata.com/api/exchange-symbol-list/{exchange_code}?api_token={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["symbols"]
    else:
        print(f"Failed to retrieve ticker list for {exchange_code}")
        return []

nyse_tickers = get_ticker_list('NYSE', eodapi)
nq_tickers = get_ticker_list('NASDAQ', eodapi)
ca_tickers = get_ticker_list('TO', eodapi)
uk_tickers = get_ticker_list('LSE', eodapi)
germany_tickers = get_ticker_list('F', eodapi)
france_tickers = get_ticker_list('PA', eodapi)
italy_tickers = get_ticker_list('MI', eodapi)
holland_tickers = get_ticker_list('AS', eodapi)
swiss_tickers = get_ticker_list('SW', eodapi)
rus_tickers = get_ticker_list('MCX', eodapi)
turkey_tickers = get_ticker_list('IS', eodapi)
hkex_tickers = get_ticker_list('HK', eodapi)
shanghai_tickers = get_ticker_list('SHG', eodapi)
shenzhen_tickers = get_ticker_list('SHE', eodapi)
taiwan_tickers = get_ticker_list('TW', eodapi)
japan_tickers = get_ticker_list('TSE', eodapi)
korea_tickers = get_ticker_list('KO', eodapi)
kosdaq_tickers = get_ticker_list('KQ', eodapi)
india_tickers = get_ticker_list('NSE', eodapi)
aus_tickers = get_ticker_list('AU', eodapi)
brazil_tickers = get_ticker_list('SA', eodapi)
mexico_tickers = get_ticker_list('MX', eodapi)
arg_tickers = get_ticker_list('BA', eodapi)
crypto_tickers = get_ticker_list('CC', eodapi)


def get_intraday_data(tickers, api_key):
    for ticker in tickers:
        url = f"https://www.alphavantage.co/query?
function=TIME_SERIES_INTRADAY_EXTENDED&symbol={ticker}&interval=1min&slice=dynamic&apikey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"{ticker}.csv", "w", newline="") as f:
                writer = csv.writer(f)
                for line in csv.reader(response.text.strip().split('\n')):
                    writer.writerow(line)
        else:
            print(f"Failed to retrieve data for {ticker}")

get_intraday_data(nyse_tickers, vantagekey)
get_intraday_data(nq_tickers, vantagekey)
get_intraday_data(hkex_tickers, vantagekey)
get_intraday_data(shanghai_tickers, vantagekey)
get_intraday_data(shenzhen_tickers, vantagekey)
