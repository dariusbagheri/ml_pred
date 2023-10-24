import jsonlines
import requests
import pandas as pd
import time

future_days = 3


class market_analysis():
    def __init__(self):

        self.future_days = 4

    def get_prc_change(self, stock_data, period=5):

        # Ensure numeric values in the columns
        stock_data['adjusted_close'] = pd.to_numeric(
            stock_data['adjusted_close'])
        stock_data['volume'] = pd.to_numeric(stock_data['volume'])

        # make it
        stock_data = stock_data.sort_values(by='date', ascending=True)

        # Calculate the percentage change over 5 periods
        percentage_change = stock_data[[
            'adjusted_close', 'volume']].pct_change(periods=period)
        stock_data
        percentage_change['date'] = percentage_change.index
        return percentage_change

        # Print the result

    # Function to retrieve daily adjusted stock data

    def get_stock_data(self, symbol):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=full&apikey=0BIGTUQRYPFFQFHH'
        response = requests.get(url)
        data = response.json()
        # Extract the time series data from the response
        time_series = data['Time Series (Daily)']
        # Convert the time series data into a DataFrame
        df = pd.DataFrame.from_dict(time_series, orient='index')
        # Rename the columns
        df.columns = ['open', 'high', 'low', 'close', 'adjusted_close',
                      'volume', 'dividend_amount', 'split_coefficient']
        # Convert the date index to datetime
        df.index = pd.to_datetime(df.index)
        return df

    # Function to retrieve market news and sentiment data
    def get_news_data(self, tickers):
        url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={tickers}&limit=500&time_from=20230110T0130&apikey=0BIGTUQRYPFFQFHH'
        response = requests.get(url)
        data = response.json()

        # Extract the news articles data from the response
        print(data.keys())

        articles = data['feed']
        # Convert the articles data into a DataFrame
        df = pd.DataFrame(articles)

        # Convert the 'time_published' column to datetime
        df['time_published'] = pd.to_datetime(df['time_published'])
        return df

    def execute(self, stock_symbol='AAPL'):
        # Define the stock symbol and tickers for news
        stock_symbol = 'AAPL'

        # Get the stock data and news data
        stock_data = self.get_stock_data(stock_symbol)
        time.sleep(5)
        news_data = self.get_news_data(stock_symbol)
        stock_data['date'] = stock_data.index
        news_data['date'] = pd.to_datetime(
            pd.to_datetime(news_data['time_published']).dt.date)

        #
        percentage_change = self.get_prc_change(stock_data, period=future_days)
        percentage_change['date'] = percentage_change.index

        # Merge the stock data and news data based on the date
        merged_data = pd.merge(percentage_change, news_data,
                               left_on='date', right_on='date', how='inner')
        merged_data[f"next_{self.future_days}_days"] = merged_data['adjusted_close'].apply(
            lambda x: "Going up" if x > 0 else "bearish")
        return merged_data


stock_symbol = 'AAPL'
mrk_pred = market_analysis()


final_df = mrk_pred.execute(stock_symbol)
# Define the stock symbol and tickers for news

time.sleep(5)

# Get the stock data and news data
stock_data = mrk_pred.get_stock_data(stock_symbol)
time.sleep(5)
news_data = mrk_pred.get_news_data(stock_symbol)
stock_data['date'] = stock_data.index
news_data['date'] = pd.to_datetime(
    pd.to_datetime(news_data['time_published']).dt.date)

#
percentage_change = mrk_pred.get_prc_change(stock_data, period=future_days)
percentage_change['date'] = percentage_change.index

# Merge the stock data and news data based on the date
merged_data = pd.merge(percentage_change, news_data,
                       left_on='date', right_on='date', how='inner')
merged_data["next_{future_days}_days"] = merged_data['adjusted_close'].apply(
    lambda x: "Going up" if x > 0 else "bearish")

# Print the merged data
print("Merged Data:")

merged_data_copy = final_df[['title',
                             'authors', 'summary',
                             'category_within_source',  'overall_sentiment_label',
                             'ticker_sentiment']].copy()
training_str = ''
training_data_dict = {}
# with open('json_data.jsonl', 'w') as outfile:
list_lines = []
list_lines_validate = []
for i in merged_data_copy.iterrows():
    promt_text = i[1].to_dict().__str__()
    training_data_dict["prompt"] = promt_text.replace("{", "").replace("}", "")
    training_data_dict["completion"] = final_df["next_4_days"][i[0]]

    # cleaning the data
    promt_text = promt_text.replace(
        "{", "").replace("}", "")[0:2000]
    promt_text = promt_text.replace("\"", "").replace("[", "").replace("]", "")
    new_line = {"prompt": promt_text[0:2000], "completion": ""}

    new_line["completion"] = str(final_df["next_4_days"][i[0]])

    # training_str=new_line[0:300] + " \"completion\" : " +final_df["next_4_days"][i[0]] +"} \n""}"
    # outfile.write(new_line)
    list_lines.append(new_line)

    print("promot :" + promt_text.replace("{", "").replace("}", ""))
    print(final_df["next_4_days"][i[0]])


def create_jsonl_file(data, file_path):
    with jsonlines.open(file_path, mode='w') as writer:
        for line in data:
            writer.write(line)


jsonl_file_path = 'data.jsonl'
jsonl_file_validate_path = 'data_val.jsonl'

create_jsonl_file(list_lines[0:30], jsonl_file_path)
create_jsonl_file(list_lines[30:], jsonl_file_validate_path)
