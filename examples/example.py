from pytrends.request import TrendReq

# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

# Get Google Real Time Trends data
trending_searches_df = pytrend.trending_realtime()
print(trending_searches_df.head())

# Get Google Top Daily
top_charts_df = pytrend.top_daily()
print(top_charts_df.head())

# Create payload and capture API tokens. Extract You Tube trends from last 30 days
pytrend.build_payload(kw_list=[], gprop='youtube', timeframe='today 1-m')

# Related Topics, returns a dictionary of dataframes
related_topics_dict = pytrend.related_topics()
print(related_topics_dict)

# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
print(related_queries_dict)

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=["Marvel Comics"])

# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df.head())

# Interest by Region
interest_by_region_df = pytrend.interest_by_region()
print(interest_by_region_df.head())

# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
print(related_queries_dict)

# Related Topics, returns a dictionary of dataframes
related_topics_dict = pytrend.related_topics()
print(related_topics_dict)

# Get Google Keyword Suggestions
suggestions_dict = pytrend.suggestions(keyword='Marvel Comics')
print(suggestions_dict)
