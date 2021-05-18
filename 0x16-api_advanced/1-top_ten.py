#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

Requirements:

    Prototype: def top_ten(subreddit)
    If not a valid subreddit, print None.
    NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

"""
import requests


def top_ten(subreddit):
    if subreddit and type(subreddit) is str:
        api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        parameters = {'User-Agent': 'python:api_advanced-holberton:v1.0.0'
                      '(by /u/tomasgomezvelez)',}
        response = requests.get(api_url, params=parameters)

        if response.status_code == 200:
            posts = response.json().get('data').get('children')
            for post in posts:
                print(post.get('data').get('title'))
        else:
            print(None)
    else:
        print(None)
