from django.shortcuts import render

import analyzing_twitter_data


def get_tweet_data(screen_name):
    twitter_client = analyzing_twitter_data.TwitterClient()
    tweet_analyzer = analyzing_twitter_data.TweetAnalyzer()

    api = twitter_client.get_twitter_client_api()
    tweets = api.user_timeline(screen_name=screen_name)
    df1 = tweet_analyzer.tweets_to_data_frame(tweets)

    return df1


def index(request):
    screen_name_data = "byjus"
    df1 = get_tweet_data(screen_name=screen_name_data)
    data_dict = df1.to_dict('records')
    return render(request, 'index.html', {"df1": data_dict})

