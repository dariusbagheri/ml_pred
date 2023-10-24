import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


#
# completion = openai.ChatCompletion.create(
#    model="fine_tuned",
#    messages=[
#        {"role": "system", "content": "Based on data trained on you tell me if a stock is going up"},
#        {"role": "user", "completion": ""}
#    ]
# )
#
# print(completion.choices[0].message)
#
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]


messages = [
    {'role': 'system', 'content': 'You are an analyst that predicts if a stock is going up or not.'},
    {"role": "user", "content": "'title': 'These are the best-performing stocks in the 2023 bull market - and the worst', 'authors': 'Philip van Doorn', 'summary': 'The cruise operators Carnival and Royal Caribbean have claimed spots alongside Nvidia, Meta Platforms and Tesla in the S&P 500 ranking of top five performers so far this year.', 'category_within_source': 'Top Stories', 'overall_sentiment_label': 'Somewhat-Bullish', 'ticker_sentiment': 'ticker': 'GOOG', 'relevance_score': '0.160633', 'ticker_sentiment_score': '0.147047', 'ticker_sentiment_label': 'Neutral', 'ticker': 'META', 'relevance_score': '0.160633', 'ticker_sentiment_score': '0.147047', 'ticker_sentiment_label': 'Neutral', 'ticker': 'AAPL', 'relevance_score': '0.160633', 'ticker_sentiment_score': '0.129761', 'ticker_sentiment_label': 'Neutral', 'ticker': 'IVZ', 'relevance_score': '0.080728', 'ticker_sentiment_score': '0.126338', 'ticker_sentiment_label': 'Neutral'", },
    {"role": "assistant", "content": "Going up"},
    {"role": "user", "content": "'title': 'Market Roars Back To Highs; Tesla Deliveries Due', 'authors': 'ED CARSON', Investor's Business Daily, 'summary': S&P 500 Rallies Back To Highs As Apple, Nvidia Lead, But Watch ... Investor's Business Daily ..., 'category_within_source': 'n/a', 'overall_sentiment_label': 'Neutral', 'ticker_sentiment': 'ticker': 'XPEV', 'relevance_score': '0.091248', 'ticker_sentiment_score': '0.035884', 'ticker_sentiment_label': 'Neutral', 'ticker': 'NVDA', 'relevance_score': '0.2035', 'ticker_sentiment_score': '-0.00964', 'ticker_sentiment_label': 'Neutral', 'ticker': 'AAPL', 'relevance_score': '0.11392', 'ticker_sentiment_score': '-0.003349', 'ticker_sentiment_label': 'Neutral', 'ticker': 'TSLA', 'relevance_score': '0.269033', 'ticker_sentiment_score': '0.020326', 'ticker_sentiment_label': 'Neutral', 'ticker': 'NIO', 'relevance_score': '0.11392', 'ticker_sentiment_score': '0.038579', 'ticker_sentiment_label': 'Neutral', 'ticker': 'JPM', 'relevance_score': '0.158968', 'ticker_sentiment_score': '-0.017667', 'ticker_sentiment_label': 'Neutral', 'ticker': 'HUBS', 'relevance_score': '0.181307', 'ticker_sentiment_score': '-0.008783', 'ticker_sentiment_label': 'Neutral', 'ticker': 'IVZ', 'relevance_score': '0.022859', 'ticker_sentiment_score': '0.145853', 'ticker_sentiment_label': 'Neutral', 'ticker': 'LI', 'relevance_score': '0.11392', 'ticker_sentiment_score': '0.068276', 'ticker_sentiment_label': 'Neutral', 'ticker': 'GE', 'relevance_score': '0.091248', 'ticker_sentiment_score': '0.119623', 'ticker_sentiment_label': 'Neutral', 'ticker': 'MAR', 'relevance_score': '0.068502', 'ticker_sentiment_score': '0.0', 'ticker_sentiment_label': 'Neutral'", },
    {"role": "assistant", "content": "Going up"},
    {"role": "user", "content": "'title': 'Stock Market Today: Stocks Pop on Upbeat Inflation Data; Apple Hits $3T Market Cap', 'authors': 'Karee Venema', 'summary': Stock Market Today: Stocks Pop on Upbeat Inflation Data. Apple Hits $3T Market Cap Kiplinger's Personal Finance ..., 'category_within_source': 'n/a', 'overall_sentiment_label': 'Somewhat-Bullish', 'ticker_sentiment': 'ticker': 'NKE', 'relevance_score': '0.174587', 'ticker_sentiment_score': '-0.146544', 'ticker_sentiment_label': 'Neutral', 'ticker': 'AAPL', 'relevance_score': '0.286864', 'ticker_sentiment_score': '0.361485', 'ticker_sentiment_label': 'Bullish', 'ticker': 'CME', 'relevance_score': '0.058615', 'ticker_sentiment_score': '-0.05598', 'ticker_sentiment_label': 'Neutral', 'ticker': 'WFC', 'relevance_score': '0.058615', 'ticker_sentiment_score': '-0.038031', 'ticker_sentiment_label': 'Neutral', 'ticker': 'BRK-A', 'relevance_score': '0.116914', 'ticker_sentiment_score': '0.269638', 'ticker_sentiment_label': 'Somewhat-Bullish'", },
    {"role": "assistant", "content": "Going up"},
    {"role": "user", "content": "'title': 'Apple clinches $3 trillion valuation, becoming first U.S. company to close at that mark', 'authors': 'Emily Bary', 'summary': 'Apple Inc. closed out the June quarter with a bang, clinching a $3 trillion valuation for the first time.', 'category_within_source': 'Top Stories', 'overall_sentiment_label': 'Somewhat-Bullish', 'ticker_sentiment': 'ticker': 'AAPL', 'relevance_score': '0.523202', 'ticker_sentiment_score': '0.241813', 'ticker_sentiment_label': 'Somewhat-Bullish', 'ticker': 'C', 'relevance_score': '0.187463', 'ticker_sentiment_score': '0.25279', 'ticker_sentiment_label': 'Somewhat-Bullish'", },
    {"role": "assistant", "content": "Going up"},
    {"role": "user", "content": "'title': 'S&P 500 Climbs On Cooler Inflation Data, Apple Reclaims $3-Trillion Market Cap, Biden Wants High-Speed Internet For Everybody - Comcast  ( NASDAQ:CMCSA ) , Cisco Systems  ( NASDAQ:CSCO ) , AT&T  ( NYSE:T ) , Micron Technology  ( NASDAQ:MU ) , Nike  ( NYSE:NKE ) ', 'authors': 'Natan Ponieman', 'summary': 'The S&P 500 and other major market indexes were ending the week on a high note Friday as the second quarter and first half of 2023 drew to a close.', 'category_within_source': 'General', 'overall_sentiment_label': 'Neutral', 'ticker_sentiment': 'ticker': 'NKE', 'relevance_score': '0.265859', 'ticker_sentiment_score': '-0.023724', 'ticker_sentiment_label': 'Neutral', 'ticker': 'AAPL', 'relevance_score': '0.349329', 'ticker_sentiment_score': '0.132432', 'ticker_sentiment_label': 'Neutral', 'ticker': 'CCZ', 'relevance_score': '0.090134', 'ticker_sentiment_score': '0.0', 'ticker_sentiment_label': 'Neutral', 'ticker': 'CSCO', 'relevance_score': '0.179121', 'ticker_sentiment_score': '0.0', 'ticker_sentiment_label': 'Neutral', 'ticker': 'T', 'relevance_score': '0.090134', 'ticker_sentiment_score': '0.0', 'ticker_sentiment_label': 'Neutral', 'ticker': 'RIDE', 'relevance_score': '0.179121', 'ticker_sentiment_score': '-0.136665', 'ticker_sentiment_label': 'Neutral'", },
    {"role": "assistant", "content": "Going up"},
    {"role": "user", "content": "'title': The SPY's 1H Rally: Will Apple, Microsoft, Amazon, Nvidia, Tesla Continue Pull The Market Higher In 2H? - SPDR S&P 500  ( ARCA:SPY ) , 'authors': 'Melanie Schaffer', 'summary': 'The S&P 500 gapped up 0.59% to start the trading day on Friday and continued to edge higher intraday to close out the first half of 2023 up about 16%. This run was led by Apple Inc AAPL, which crossed the $3 trillion market-cap level.', 'category_within_source': 'Trading', 'overall_sentiment_label': 'Neutral', 'ticker_sentiment': 'ticker': 'MSFT', 'relevance_score': '0.181819', 'ticker_sentiment_score': '0.093533', 'ticker_sentiment_label': 'Neutral', 'ticker': 'NVDA', 'relevance_score': '0.091509', 'ticker_sentiment_score': '0.067495', 'ticker_sentiment_label': 'Neutral', 'ticker': 'AAPL', 'relevance_score': '0.269776', 'ticker_sentiment_score': '0.103985', 'ticker_sentiment_label': 'Neutral', 'ticker': 'TSLA', 'relevance_score': '0.181819', 'ticker_sentiment_score': '0.093533', 'ticker_sentiment_label': 'Neutral'", },
    {"role": "assistant", "content": "Going up"},
    {'role': 'user', 'content': "' title': 'Apple Stock Has a Shot to Make History Today. Should Investors Be Excited or Worried?', 'authors': 'Keith Speights', 'summary': Say hello to the world's first $3 trillion company., 'category_within_source': 'n/a', 'overall_sentiment_label': 'Somewhat-Bullish', 'ticker_sentiment': 'ticker': 'AAPL', 'relevance_score': '0.649995', 'ticker_sentiment_score': '0.231205', 'ticker_setiment_label': 'Somewhat-Bullish'"},
]

response = get_completion_from_messages(messages, temperature=1)

print(response)